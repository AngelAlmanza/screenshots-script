import pyautogui
import time
import os

def create_directory(directory_name):
  if not os.path.exists(directory_name):
    os.makedirs(directory_name)

def take_screenshot(directory_name, base_name):
  screenshot = pyautogui.screenshot()
  screenshot.save(f"{directory_name}/{base_name}.png")

def take_screenshots_in_loop(directory_name, base_name, time_interval, time_duration):
    finish_time = False
    i = 0
    initial_time = time.time()
    while not finish_time:
        take_screenshot(directory_name, f"{base_name}_{i}")
        i += 1
        time.sleep(time_interval)
        if time.time() - initial_time > time_duration:
          finish_time = True

def main():
  directory_name = input("Enter the directory name: ")
  base_name = input("Enter the base name: ")
  time_interval = int(input("Enter the time interval: "))
  time_duration = int(input("Enter the time duration: "))

  create_directory(directory_name)
  take_screenshots_in_loop(directory_name, base_name, time_interval, time_duration)

if __name__ == "__main__":
  main()