from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    welcome_message = "Welcome to my random number generator! Click the button to get a new random number."
    number = random.randint(0, 10000)
    number = str(number)
    return render_template("homepage.html", someText = welcome_message, randomNumber = number)

if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 
