import flask
import psycopg2

app = flask.Flask(__name__)

@app.route('/pop/<abbrev>')
def getPopulation(abbrev):
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="thompsons",
    user="thompsons",
    password="paper876stars")

    cur = conn.cursor()

    sql = "SELECT * FROM abbreviations WHERE abbreviation = '" + abbrev + "'"
    cur.execute(sql)
    row = cur.fetchone()
    state_name = row[0]

    sql = " SELECT * FROM cities WHERE state = '" + state_name + "'"
    
    cur.execute( sql )

    rows = cur.fetchall()
    total_population = 0
    for row in rows:
        total_population += row[2]

    return str(total_population)


if __name__ == '__main__':
    my_port = 5135
    app.run(host='0.0.0.0', port = my_port) 
