from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    welcome_message = "Welcome to my random number generator! Click the button to get a new random number."
    return render_template("homepage.html", someText = welcome_message)

def numberGenerator():
    randomNumber = random.randint(0, 10000)
    randomNumber = str(randomNumber)
    return randomNumber

if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 
