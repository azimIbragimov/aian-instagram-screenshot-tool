import pyautogui
import json
from datetime import datetime
import mss
import time
import os
from PIL import ImageGrab
from PIL import Image


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        data = json.load(f)

    print("Configuration")
    print(data)

    storage_folder = data["storage_folder"]
    time_format = data["time_format"]
    crop_box = data["crop_box"]

    with mss.mss() as sct:
        while True:
            now = datetime.now()
            # Replace colons with dashes or remove them to make the filename valid
            current_time = now.strftime("%H-%M-%S_%d-%m-%Y")  # Format: hour-minute-second_day-month-year
            file_path = os.path.join(storage_folder, f"{current_time}.png")

            # Capture the screen
            screenshot = ImageGrab.grab()
            cropped_screenshot = screenshot.crop(crop_box)
            cropped_screenshot.save(file_path)

            print(f"Saved screenshot: {file_path}")
