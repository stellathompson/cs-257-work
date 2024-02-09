from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #  are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)

    num = random.randint(low_int, high_int)

    cityNum = random.randint(0, 3000)

    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="thompsons",
    user="thompsons",
    password="paper876stars")

    cur = conn.cursor()

    sql = " SELECT city FROM cities WHERE city IS NOT null"
    
    cur.execute( sql )

    for i in range (cityNum):
        city = cur.fetchone()

    return render_template("random-fun-fact.html", randNum = num, randCity = city)

if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 