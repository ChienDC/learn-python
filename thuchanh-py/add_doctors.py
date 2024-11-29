def insert_doctors(conn):
    cursor = conn.cursor()

    for i in range(5):
        full_name = input(f"Nhập tên bác sĩ {i + 1}: ")
        specialization = input(f"Nhập chuyên môn của bác sĩ {i + 1}: ")
        phone_number = input(f"Nhập số điện thoại của bác sĩ {i + 1}: ")
        email = input(f"Nhập email của bác sĩ {i + 1}: ")
        years_of_experience = int(input(f"Nhập số năm kinh nghiệm của bác sĩ {i + 1}: "))
        cursor.execute("""
            INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) 
            VALUES (%s, %s, %s, %s, %s)
        """, (full_name, specialization, phone_number, email, years_of_experience))
    conn.commit()
    print("Đã thêm 5 bác sĩ vào cơ sở dữ liệu.")
