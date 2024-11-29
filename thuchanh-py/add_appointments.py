def insert_appointments(conn):
    cursor = conn.cursor()

    for i in range(3):
        patient_id = int(input(f"Nhập ID của bệnh nhân {i + 1}: "))
        doctor_id = int(input(f"Nhập ID của bác sĩ cho bệnh nhân {i + 1}: "))
        appointment_date = input(f"Nhập ngày giờ cuộc hẹn của bệnh nhân {i + 1} (YYYY-MM-DD HH:MM:SS): ")
        reason = input(f"Nhập lý do cuộc hẹn của bệnh nhân {i + 1}: ")
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) 
            VALUES (%s, %s, %s, %s)
        """, (patient_id, doctor_id, appointment_date, reason))
    conn.commit()
    print("Đã thêm 3 cuộc hẹn cho 3 bệnh nhân.")
