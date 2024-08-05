"""
Good Luck Trying To Read This Code ;)
"""

from flask import Flask, render_template, send_from_directory, redirect, url_for
from PIL import ImageGrab
import time
import threading
import os
import webview
import multiprocessing
import webbrowser
import colorama


app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'screenshots'

print(colorama.Fore.RESET)

class ParentalControlApp:
    def __init__(self):
        self.is_running = False
        self.thread = None

    def take_screenshot(self):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = "screenshot_{}.png".format(timestamp)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        screenshot = ImageGrab.grab()
        screenshot.save(filepath)
        print("Screenshot saved as {}".format(filepath))

    def take_screenshots(self):
        while self.is_running:
            self.take_screenshot()
            time.sleep(3)

    def start_screenshots(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.take_screenshots)
            self.thread.start()
            print("Taking screenshots...")
        else:
            print("Screenshot process is already running")

    def stop_screenshots(self):
        if self.is_running:
            self.is_running = False
            self.thread.join()
            print("Screenshot process stopped")
        else:
            print("Screenshot process is not running")

parental_control_app = ParentalControlApp()

@app.route('/')
def index():
    return render_template('index.html', is_running=parental_control_app.is_running)

@app.route('/start', methods=['POST'])
def start():
    parental_control_app.start_screenshots()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    parental_control_app.stop_screenshots()
    return redirect(url_for('index'))

@app.route('/activity')
def activity():
    screenshots = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('activity.html', screenshots=screenshots)

@app.route('/screenshots/<path:filename>')
def get_screenshot(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def startserver():
    # app.run(debug=False, port=5000, use_reloader="False")
    webview.create_window("Parental Control Software", "http://127.0.0.1:5000")
    webview.start()
    print()
    print(colorama.Fore.GREEN, "Copyright 2024. Hiruja Edurapola.")
    # print("Main Window Closed")
    print()
    print(colorama.Fore.LIGHTYELLOW_EX,"App Window Closed By The User")
    print(colorama.Fore.LIGHTRED_EX, "App will still run in the background until this window is closed.")
    print()
    print()
    print(colorama.Fore.LIGHTMAGENTA_EX, "Press Ctrl + C to terminate without relaunching")
    print(colorama.Fore.RESET)
    
    


if __name__ == '__main__':
    # threading.Thread(target=startserver).start()
    server_process = multiprocessing.Process(target=startserver)
    server_process.start()
    app.run(debug=True)
    
    # webview.create_window("Parental Control Software", "http://127.0.0.1:5000")
    # webview.start()
    # startserver()

    
    

    # webview.create_window("Parental Control Software", "http://127.0.0.1:5000")
    # webview.start()

    # server_process.terminate()

    
    # webbrowser.open("http://127.0.0.1:5000")
    # print("Loading...")
    # print("Hiruja is the G.O.A.T.")
    # app.run(debug=True)


