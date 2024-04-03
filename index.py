from PIL import ImageGrab
import time

def take_screenshot():
    # Get the current timestamp to use it as part of the screenshot file name
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the file name for the screenshot
    filename = "screenshot_{}.png".format(timestamp)
    
    # Take the screenshot and save it
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    print("Screenshot saved as {}".format(filename))

def main():
    try:
        while True:
            # Take a screenshot every 5 seconds
            take_screenshot()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program terminated by user")

if __name__ == "__main__":
    main()
