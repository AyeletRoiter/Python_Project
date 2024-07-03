from models.config import connection

def Update_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = """
                UPDATE Zimmers
                SET 
                    NameZim = ?,
                    LocationZim = ?,
                    Area = ?,
                    IsPool = ?,
                    IsJacuzzi = ?,
                    MidweekPrice = ?,
                    EndWeekPrice = ?,
                    TypeZim = ?,
                    NumRoom = ?,
                    GeneralSpecific = ?
                WHERE
                    NameZim = ?
            """
            cursor.execute(query, (NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, NameZim))
            conn.commit()
            print("The Zimmer updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()

