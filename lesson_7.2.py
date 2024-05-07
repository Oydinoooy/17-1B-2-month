"""
git clone -b master

git add Для заливки в гидхаб

git commit - m "name"

git puss

"""

#  СУБД и БД
# Расширение база данных - db
# Посредник - cursor 
# Запрсы на языке SQLite Тип данных пишем с заглавной, а название с маленькой
# Не ограниченное кол-во  - TEXT
#Текст с ограничением, то есть можно задать кол-во символов - VARCHAR
 # Отправлем запрос с помощью - execute
# DEFAULL - по умолчанию 
# NOT NULL - обязательное поле
# FLOAT = DOUBLE



import sqlite3
connect = sqlite3.connect("Geeks.db") 
cursor = connect.cursor() 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
               id INT PRIMARY KEY, 
               full_name VARCHAR (25) NOT NULL, 
               hobby TEXT DEFAULL NOT, 
               phone_number INT NOT NULL DEFAULL 966, 
               birth_date DATE,
               mark DOUBLE (7, 3) DEFAULL 0.0,
               agreement BOOLEAN DEFAULL FALSE
)
;""")





class Geeks:
    def __init__(self):
        self.full_name = None 
        self.hobby = None 
        self.phone_number = 0
        self.birth_date = None
        self.mark = 0
        self.agreement = False

    def register(self, full_name, hobby, phone_number, birth_date):
        self.full_name = full_name 
        self.hobby = hobby
        self.phone_number = phone_number
        self.birth_date = birth_date

        cursor.execute(f"""INSERT INTO students (full_name, hobby, phone_nomber, birth_date)
                       VALUES('{full_name}', '{hobby}', {phone_number}, '{birth_date}')""")
        cursor.execute(f"""INSERT INTO students (full_name, hobby, phone_nomber, birth_date)
                       VALUES('?', '?', ?, '>')""", full_name, hobby, phone_number, birth_date)
        
        connect.commit()

geeks_students = Geeks()
geeks_students.register("Usmanova Oydinoy", "coding", +996554033030, "31.05.2002")