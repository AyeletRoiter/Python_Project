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

# דוגמה לבדיקה של פונקציה
if __name__ == "__main__":
    # הגדרת שם לבדיקה
    landlord_name_to_check = "ליאור"

    # קריאה לפונקציה
    is_landlord = Is_landLord(landlord_name_to_check)

    # הדפסת התוצאה
    if is_landlord:
        print(f"השם {landlord_name_to_check} קיים במערכת")
    else:
        print(f"השם {landlord_name_to_check} לא קיים במערכת")
