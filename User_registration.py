import sqlite3
connect = sqlite3.connect('test_database.db')

cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
   name TEXT,
   surname TEXT,
   city TEXT,
   birthday TEXT,
   place_of_study TEXT);
""")
connect.commit()


def insert_to_data(user_name,user_surname,user_city,user_birthday,user_place_of_study):
    cursor.execute("""INSERT INTO users(name, surname, city, birthday, place_of_study) VALUES (?, ?, ?, ? ,?)""", (user_name,user_surname,user_city,user_birthday,user_place_of_study))
    connect.commit()

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_city = input('Город: ')
user_birthday = input('День рождения: ')
user_place_of_study = input('ВУЗ: ')

insert_to_data(user_name,user_surname,user_city,user_birthday,user_place_of_study)

connect.commit()

cursor.execute("SELECT * FROM users;")
all_results = cursor.fetchall()
print(all_results)

# Сохраняем изменения
connect.commit()
cursor.close()
connect.close()
