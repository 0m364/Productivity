"""
Mouse Mover with Key Strokes Script
===================================

This script moves the mouse cursor to a random position and presses a key at regular intervals.
Useful for keeping the computer awake or simulating activity.

Prerequisites:
    pip install pyautogui

Usage:
    python3 Mouse-mover-with-key-strokes.py [--interval SECONDS] [--keys KEY1 KEY2 ...]
"""

import pyautogui
import random
import time
import argparse

def move_mouse_and_type(interval, keys):
    """
    Moves the mouse to a random position and presses a random key at regular intervals.

    Args:
        interval (int): Time in seconds to wait between actions.
        keys (list): List of keys to choose from for pressing.
    """
    print(f"Moving mouse and pressing keys {keys} every {interval} seconds. Press Ctrl+C to stop.")
    screen_width, screen_height = pyautogui.size()

    try:
        while True:
            # Mouse movement
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y, duration=0.5)

            # Keystrokes
            key = random.choice(keys)
            pyautogui.press(key)

            print(f"Moved to ({x}, {y}) and pressed '{key}'")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping mouse mover and typer.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move the mouse and press keys randomly to simulate activity.")
    parser.add_argument("--interval", type=int, default=30, help="Interval between actions in seconds (default: 30)")
    parser.add_argument("--keys", nargs="+", default=["shift"], help="List of keys to press (default: shift)")

    args = parser.parse_args()

    move_mouse_and_type(args.interval, args.keys)
