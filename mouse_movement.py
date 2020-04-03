import pyautogui
import sys
import time
import os


if __name__ == "__main__":

    """
    #1: the *minutes* between every mouse movement.
    #2: how many minutes the script will be running
    """
    max_time = 30
    sleep_time = 0.5 

    if (len(sys.argv) == 3):
        max_time = sys.argv[1]
        sleep_time = sys.argv[2] 
    else:
        print("Default values are asserted")

    sleep_time_in_minutes = sleep_time * 60
    time_passed = 0
    up = True

    while(time_passed < max_time):
        time_passed += sleep_time

        if (up):
            pyautogui.moveRel(0, -10)  # move mouse 10 pixels up
            up = False
        else:
            pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
            up = True

        time.sleep(sleep_time_in_minutes)
        print("Elapsed: %.1f minute(s). Remaining: %.1f minute(s). Press Ctrl+C to terminate on terminal." % (time_passed,(max_time-time_passed)))
