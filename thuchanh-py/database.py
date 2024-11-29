import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="medical_service"
        )
        if conn.is_connected():
            print("Đã kết nối tới cơ sở dữ liệu.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
