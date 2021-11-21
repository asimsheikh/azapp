from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'The goal it to test the next deploy'
