import psycopg2


def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="thompsons",
        user="thompsons",
        password="paper876stars")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None


def create_tables():

    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="thompsons",
    user="thompsons",
    password="paper876stars")

    cur = conn.cursor()

    sql = """DROP TABLE IF EXISTS cities; CREATE TABLE cities (city text, state text, population integer, lat real, lon real);
            DROP TABLE IF EXISTS abbreviations; CREATE TABLE abbreviations (state text, abbreviation text);"""
    
    cur.execute( sql )

    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()

test_connection()
create_tables()