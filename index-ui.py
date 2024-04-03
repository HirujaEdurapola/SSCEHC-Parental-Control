from PIL import ImageGrab
import time
import threading

class ParentalControlApp:
    def __init__(self):
        self.is_running = False
        self.thread = None

    def take_screenshot(self):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = "screenshot_{}.png".format(timestamp)
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        print("Screenshot saved as {}".format(filename))

    def take_screenshots(self):
        while self.is_running:
            self.take_screenshot()
            time.sleep(5)

    def start_screenshots(self):
        self.is_running = True
        self.thread = threading.Thread(target=self.take_screenshots)
        self.thread.start()
        print("Taking screenshots...")

    def stop_screenshots(self):
        self.is_running = False
        self.thread.join()
        print("Screenshot process stopped.")

def main():
    app = ParentalControlApp()
    try:
        app.start_screenshots()
        input("Press Enter to stop...")
        app.stop_screenshots()
    except KeyboardInterrupt:
        app.stop_screenshots()
        print("Program terminated by user")

if __name__ == "__main__":
    main()
