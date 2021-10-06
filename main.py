import pyautogui
import time

if __name__ == '__main__':
    print("Starting mouse wiggler...")
    print("Press 'ctrl+c' to exit")

    # Getting screen size
    screenWidth, screenHeight = pyautogui.size()

    # This script will move the mouse to these points at the set time intervals
    #   (0,0)                                           (X, 0)
    #   |----------------------------------------------------|
    #   |   TL(25%, 25%)                      TR(75%, 25%)   |
    #   |                                                    |
    #   |                                                    |
    #   |                                                    |
    #   |   BL(25%, 75%                       BR(75%, 75%)   |
    #   |----------------------------------------------------|
    #   (0, Y)                                           (X,Y)

    # Denoting the position on the screen to move the mouse to
    pos_TL = [screenWidth * 0.25, screenHeight * 0.25]
    pos_TR = [screenWidth * 0.75, screenHeight * 0.25]
    pos_BL = [screenWidth * 0.25, screenHeight * 0.75]
    pos_BR = [screenWidth * 0.75, screenHeight * 0.75]

    # Time between mouse moves (seconds)
    WAIT_TIME = 5
    MOUSE_SPEED = 2

    # Looping program till keyboard interupt
    try:
        while True:
            pyautogui.moveTo(pos_TL[0], pos_TL[1], MOUSE_SPEED)
            time.sleep(WAIT_TIME)

            pyautogui.moveTo(pos_TR[0], pos_TR[1], MOUSE_SPEED)
            time.sleep(WAIT_TIME)

            pyautogui.moveTo(pos_BL[0], pos_BL[1], MOUSE_SPEED)
            time.sleep(WAIT_TIME)

            pyautogui.moveTo(pos_BR[0], pos_BL[1], MOUSE_SPEED)
            time.sleep(WAIT_TIME)

    except KeyboardInterrupt:
        print("\nClosing mouse wiggler...")

