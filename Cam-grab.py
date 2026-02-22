"""
Camera Linker Script
====================

This script connects to a camera API and links all cameras in the 'admin' group together.

Prerequisites:
    pip install requests

Usage:
    python3 Cam-grab.py [--url BASE_URL]
"""

import requests
import argparse
import sys

def get_camera_list(base_url):
    """
    Gets a list of all cameras on the network.

    Args:
        base_url (str): The base URL of the camera API.

    Returns:
        list: A list of camera objects (dicts).
    """
    url = f"{base_url}/api/cameras/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching camera list: {e}")
        return []

def link_cameras(camera_list, base_url):
    """
    Links all cameras in the list together if they belong to the 'admin' group.

    Args:
        camera_list (list): List of camera objects.
        base_url (str): The base URL of the camera API.
    """
    url = f"{base_url}/api/cameras/link/"

    # Filter for admin cameras first to avoid repeated checks
    admin_cameras = [cam for cam in camera_list if cam.get("admin_group") == "admin"]

    if not admin_cameras:
        print("No admin cameras found to link.")
        return

    print(f"Found {len(admin_cameras)} admin cameras. Starting linking process...")

    count = 0
    for camera in admin_cameras:
        for other_camera in admin_cameras:
            if camera["id"] != other_camera["id"]:
                try:
                    response = requests.post(url, data={
                        "camera_id": camera["id"],
                        "other_camera_id": other_camera["id"]
                    })
                    if response.status_code == 200:
                        print(f"Linked Camera {camera['id']} with Camera {other_camera['id']}")
                        count += 1
                    else:
                        print(f"Failed to link Camera {camera['id']} with Camera {other_camera['id']}: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error linking cameras: {e}")

    print(f"Finished. Total links created: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Link cameras in the admin group.")
    parser.add_argument("--url", default="http://192.168.1.1", help="Base URL of the camera API (default: http://192.168.1.1)")

    args = parser.parse_args()

    # Remove trailing slash if present for consistency
    base_url = args.url.rstrip("/")

    cameras = get_camera_list(base_url)
    if cameras:
        link_cameras(cameras, base_url)
    else:
        sys.exit(1)
