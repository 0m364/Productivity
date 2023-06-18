import requests

def get_camera_list():
  """Gets a list of all cameras on the network."""
  response = requests.get("http://192.168.1.1/api/cameras/")
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("Could not get camera list")

def link_cameras(camera_list):
  """Links all cameras in the list together."""
  for camera in camera_list:
    if camera["admin_group"] == "admin":
      for other_camera in camera_list:
        if other_camera["admin_group"] == "admin":
          requests.post("http://192.168.1.1/api/cameras/link/", data={
            "camera_id": camera["id"],
            "other_camera_id": other_camera["id"]
          })

if __name__ == "__main__":
  camera_list = get_camera_list()
  link_cameras(camera_list)