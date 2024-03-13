import pyautogui
import time

def move_mouse():
    # Get the current mouse position
    original_position = pyautogui.position()
    
    # Move the mouse a large distance
    pyautogui.moveRel(100, 100, duration=0.25)
    
    # Move the mouse back to its original position
    pyautogui.moveTo(original_position)

if __name__ == "__main__":
    try:
        while True:
            move_mouse()
            time.sleep(10)  # Wait for 10 seconds
    except KeyboardInterrupt:
        print("Mouse movement stopped.")
