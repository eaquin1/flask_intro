from flask import Flask, request

app = Flask(__name__)
@app.route('/welcome')
def welcome():
    """Returns 'welcome'"""
    return """
        <h1>Welcome</h1>
    """

@app.route('/welcome/home')
def welcome_home():
    """Returns 'welcome'"""
    return """
        <h1>welcome home</h1>
    """

@app.route('/welcome/back')
def welcome_back():
    """Returns 'welcome'"""
    return """
        <h1>welcome back</h1>
    """    