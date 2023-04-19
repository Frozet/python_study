import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ivan",
    password="Megaf0n+",
    database="testdb"
)
cursor = mydb.cursor()

for _ in range(1000):
    phone_number = '+79' + random.choice(['02', '05', '24', '29', '34', '50', '52', '55', '64', '69', '84', '90', '95', '99']) + str(random.randint(1000000, 9999999))
    date_begin = '2023-' + '04-' + str(random.randint(11, 18)) + ' ' + str(random.randint(10, 22)) + ':' + str(random.randint(10, 45)) + ':' + str(random.randint(10, 59))
    call_time = random.randint(5, 600)
    hours, minutes, seconds = int(date_begin[11:13]), int(date_begin[14:16]), int(date_begin[17:])
    seconds += call_time
    if seconds > 59:
        minutes += seconds // 60
        seconds = seconds % 60
        if seconds < 10:
            seconds = '0' + str(seconds)
    date_end = date_begin[:11] + str(hours) + ':' + str(minutes) + ':' + str(seconds)

    sql = "INSERT INTO calls (numbers, date_begin, date_end, call_time) VALUES (%s, %s, %s, %s)"
    val = (phone_number, date_begin, date_end, call_time)

    # Выполнение SQL-запроса и сохранение изменений в базе данных
    cursor.execute(sql, val)
    mydb.commit()

print("Данные успешно добавлены в таблицу movies!")
    #print(phone_number)
    #print(date_begin)
    #print(date_end)
    #print(call_time)