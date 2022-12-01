from django.conf import settings

def db_redistribute():
    import sqlite3
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        print("-----------------------------------------------------")
        # sqlite_select_Query = "select * from sklad_core_product;"
        query = "update sklad_core_product set yest_left = left, quantity = 0, total_quantity = 0, left = 0, quantity_sold = 0, summ = 0;"
        cursor.execute(query)
        sqliteConnection.commit()
        record = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
      print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            print("-----------------------------------------------------")
            print('another print with cron')
