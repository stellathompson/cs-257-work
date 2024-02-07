import flask

app = flask.Flask(__name__)

#returns the sum of two numbers
@app.route('/add/<number1>/<number2>')
def addition(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    result = number1 + number2
    result = str(result)
    return result

if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 
