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


def insert_patients(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (full_name, date_of_birth, gender, address) VALUES (%s, %s, %s, %s)",
                   ('Nguyen A', '2010-01-01', 'Male', 'Ha Noi'))
    cursor.execute("INSERT INTO patients (full_name, date_of_birth, gender, address) VALUES (%s, %s, %s, %s)",
                   ('Nguyen B', '1990-01-01', 'Female', 'Ha Noi'))
    conn.commit()
    print("Đã thêm bệnh nhân thành công.")


def insert_doctors(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doctors (full_name, specialization, years_of_experience) VALUES (%s, %s, %s)",
                   ('Nguyen Si', 'General Medicine', 10))
    cursor.execute("INSERT INTO doctors (full_name, specialization, years_of_experience) VALUES (%s, %s, %s)",
                   ('Tran Binh', 'Surgery', 5))
    conn.commit()
    print("Đã thêm bác sĩ thành công.")


def insert_appointments(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT patient_id FROM patients WHERE full_name = %s", ('Nguyen A',))
    patient_id = cursor.fetchone()
    if not patient_id:
        print("Bệnh nhân Nguyen A không tồn tại.")
        return

    cursor.execute("SELECT doctor_id FROM doctors WHERE full_name = %s", ('Nguyen Si',))
    doctor_id = cursor.fetchone()
    if not doctor_id:
        print("Bác sĩ Nguyen Si không tồn tại.")
        return

    cursor.fetchall()

    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)",
                   (patient_id[0], doctor_id[0], '2024-11-29 10:00:00', 'Regular check-up'))
    conn.commit()
    print("Đã thêm cuộc hẹn thành công.")


def main():
    conn = connect_to_database()

    if conn:
        insert_patients(conn)
        insert_doctors(conn)
        insert_appointments(conn)

        conn.close()
        print("Kết nối đã được đóng. Chương trình kết thúc.")


if __name__ == "__main__":
    main()
