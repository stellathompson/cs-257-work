import psycopg2

def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    cur = conn.cursor()

    sql = " SELECT * FROM cities WHERE city = 'Northfield' "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Sorry, Northfield is not in the database.")
    else:
        print("latitude is: " + row[3] + " and longitude is: " + row[4])

    conn.commit()

def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    cur = conn.cursor()

    sql = " SELECT * FROM cities ORDER BY population DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "has a population of", row[2], "(the biggest in the dataset).")

    conn.commit()

def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    cur = conn.cursor()

    sql = " SELECT * FROM cities WHERE state = 'Minnesota' ORDER BY population ASC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "has a population of", row[2], "(the smallest in Minnesota).")

    conn.commit()

def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    cur = conn.cursor()

#North
    sql = " SELECT * FROM cities ORDER BY lat DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "is furthest North.")

#South
    sql = " SELECT * FROM cities ORDER BY lat ASC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "is furthest South.")    

#East
    sql = " SELECT * FROM cities ORDER BY lon DESC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "is farthest East.")

#West
    sql = " SELECT * FROM cities ORDER BY lon ASC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "is farthest West.")
        
    conn.commit()
    

def test_query_five():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    cur = conn.cursor()
    state = input("What is the name of the state you are looking for?")
    
    if len(state_name) == 2:
        sql = "SELECT * FROM abbreviations WHERE abbreviation =", state_name
        cur.execute(sql)
        row = cur.fetchone()
        state_name = row[0]
    else:
        state_name = state

    #if length of string is 2, then go to abbreviation table and find the state
    #turn the state into variable that is then used in the SQL call
    #else, put the state directly into the SQL command
    sql = " SELECT * FROM cities WHERE state =", state_name
    
    cur.execute( sql )

    row = cur.fetchall()
    total_population = 0
    for i in row:
        total_population += row[2]


    if row == None:
        print("Something went wrong...")
    else:
        print("Total population of", state_name, "is", total_population)

    conn.commit()

test_query_one()
test_query_two()
test_query_three()
test_query_four()
test_query_five()
