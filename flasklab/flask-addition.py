import flask

app = flask.Flask(__name__)

#returns the sum of two numbers
@app.route('/display/<number1>/<number2>')
def my_display(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    result = number1 + number2
    return result

if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 
