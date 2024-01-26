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

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()

    if row == None:
        print("Sorry, Northfield is not in the database.")
    else:
        print("latitude is: " + row[3] + " and longitude is: " + row[4])


    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

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

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print(row[0], "has a population of", row[2], "(the biggest in the dataset).")


    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()

test_query_one()
test_query_two()
