def insert_patients(conn):
    cursor = conn.cursor()

    # Thêm 3 bệnh nhân
    for i in range(3):
        full_name = input(f"Nhập tên đầy đủ của bệnh nhân {i + 1}: ")
        date_of_birth = input(f"Nhập ngày sinh của bệnh nhân {i + 1} (YYYY-MM-DD): ")
        gender = input(f"Nhập giới tính của bệnh nhân {i + 1}: ")
        address = input(f"Nhập địa chỉ của bệnh nhân {i + 1}: ")
        cursor.execute("""
            INSERT INTO patients (full_name, date_of_birth, gender, address) 
            VALUES (%s, %s, %s, %s)
        """, (full_name, date_of_birth, gender, address))
    conn.commit()
    print("Đã thêm 3 bệnh nhân vào cơ sở dữ liệu.")
