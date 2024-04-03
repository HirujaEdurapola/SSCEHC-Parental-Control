from flask import Flask, render_template
from PIL import ImageGrab
import time
import threading

app = Flask(__name__)

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

parental_control_app = ParentalControlApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    parental_control_app.start_screenshots()
    return 'Screenshots started'

@app.route('/stop')
def stop():
    parental_control_app.stop_screenshots()
    return 'Screenshots stopped'

if __name__ == '__main__':
    app.run(debug=True)
