from flask import Flask
import webview

server = Flask(__name__, static_folder='./templates', template_folder='./templates')
webview.create_window('SSCEHCC Parental Control', 'http://127.0.0.1:5000/')
webview.start()