from models.config import connection

# Login page - Checking if the lessor's name exists in the system

def Is_landLord(name_land):
    # Get the connection object
    conn = connection()

    # Use the connection object to create a cursor
    with conn.cursor() as cursor:
        query = f"SELECT nameLand FROM landlords WHERE nameLand = '{name_land}';"
        cursor.execute(query)
        res = cursor.fetchone()  # Getting the first row of the result (if any)
        if res:
            return True
        return False

