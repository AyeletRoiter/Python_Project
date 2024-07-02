from models.config import connection

def get_all_zimers():
    # Get the connection object
    conn = connection()

    try:
        with conn.cursor() as cursor:
            # Query to retrieve all the Zimmers and the phone of the landlord from landlords table by using Join method
            query = """
            SELECT z.NameZim, z.LocationZim, z.IsPool, z.IsZacuzzi, z.MidweekPrice, z.TypeZim, l.Phone
            FROM zimers z
            JOIN landlords l ON z.LandID = l.LandID;
            """
            cursor.execute(query)
            res = cursor.fetchall()

            # Insert the result into a list variable
            zimers_list = []
            for row in res:
                zimers_list.append({
                    "NameZim": row[0],
                    "LocationZim": row[1],
                    "IsPool": row[2],
                    "IsZacuzzi": row[3],
                    "MidweekPrice": row[4],
                    "TypeZim": row[5],
                    "Phone": row[6]
                })

            return zimers_list

    finally:
        conn.close()  # Close the connection when done

# Example usage of the function
if __name__ == "__main__":
    zimers = get_all_zimers()

    # Print the retrieved zimers list
    for zimer in zimers:
        print(f"Name: {zimer['NameZim']}, Location: {zimer['LocationZim']}, IsPool: {zimer['IsPool']}, IsZacuzzi: {zimer['IsZacuzzi']}, MidweekPrice: {zimer['MidweekPrice']}, Type: {zimer['TypeZim']}, Phone: {zimer['Phone']}")
