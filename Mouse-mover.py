"""
Mouse Mover Script
==================

This script moves the mouse cursor to a random position on the screen at regular intervals.
Useful for keeping the computer awake or simulating activity.

Prerequisites:
    pip install pyautogui

Usage:
    python3 Mouse-mover.py [--interval SECONDS] [--duration SECONDS]
"""

import pyautogui
import random
import time
import argparse

def move_mouse(interval, duration):
    """
    Moves the mouse to a random position on the screen at regular intervals.

    Args:
        interval (int): Time in seconds to wait between movements.
        duration (float): Duration of the mouse movement animation.
    """
    print(f"Moving mouse every {interval} seconds. Press Ctrl+C to stop.")
    screen_width, screen_height = pyautogui.size()

    try:
        while True:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y, duration=duration)
            print(f"Moved to ({x}, {y})")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping mouse mover.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move the mouse randomly to simulate activity.")
    parser.add_argument("--interval", type=int, default=10, help="Interval between movements in seconds (default: 10)")
    parser.add_argument("--duration", type=float, default=0.5, help="Duration of mouse movement in seconds (default: 0.5)")

    args = parser.parse_args()

    move_mouse(args.interval, args.duration)
