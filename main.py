import mysql.connector


## MAIN BACKEND PROGRAM
dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "asia4046",
)

if dataBase.is_connected():
    print("[DB]: Successfully Connected To Database at localhost")

dbCursor = dataBase.cursor()

def create_db():
    try:
        dbCursor.execute("CREATE DATABASE biodiv_zoo")
    except:
        pass

def create_table():
    biodiv_table = """
                    CREATE TABLE ZOOMANAGE (
                    SPECIES_ID INT PRIMARY KEY,
                    SPECIES_NAME VARCHAR(50) NOT NULL,
                    SCIENTIFIC_NAME VARCHAR(50) NOT NULL,
                    GENERIC_NAME VARCHAR(50) NOT NULL,
                    ZOO_COUNT INT NOT NULL,
                    GLOBAL_COUNT INT NOT NULL,
                    ORIGIN_COUNTRY VARCHAR(30) NOT NULL,
                    DIET_TYPE VARCHAR(30) NOT NULL,
                    ENDANGERED_RATE VARCHAR(30),
                    FEEDING_QUANTITY INT NOT NULL,
                    HABITAT_TYPE VARCHAR(30) NOT NULL,
                    LIFE_SPAN_IN_YEARS INT NOT NULL,
                    BIRTH_RATE INT NOT NULL,
                    DEATH_RATE VARCHAR(30) NOT NULL
                    )
    
                   """
    try:
        dbCursor.execute("use biodiv_zoo")
        dbCursor.execute(biodiv_table)
    except:
        pass

def create_single_record():
    sql = "INSERT INTO ZOOMANAGE (SPECIES_ID, SPECIES_NAME, SCIENTIFIC_NAME, GENERIC_NAME, ZOO_COUNT, GLOBAL_COUNT, ORIGIN_COUNTRY, DIET_TYPE, ENDANGERED_RATE, FEEDING_QUANTITY, HABITAT_TYPE, LIFE_SPAN_IN_YEARS, BIRTH_RATE, DEATH_RATE)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    spec_id = int(input("Enter Species ID(integer): "))
    spec_name = input("Enter Species Name: ")
    scien_name = input("Enter Scientific Name: ")
    gen_name = input("Enter Generic Name: ")
    zoo_count = int(input("Enter Zoo Count: "))
    global_count = int(input("Enter Global Count: "))
    origin = input("Enter Origin Country: ")
    diet_type = input("Enter Diet Type: ")
    endangered_status = input("Enter Endangered Status: ")
    feed_qunt = int(input("Enter Feeding Quantity: "))
    habitat_type = input("Enter Habitat Type: ")
    life_span = int(input("Enter Life Span (in years): "))
    birth_rate = int(input("Enter Birth Rate (no/year): "))
    death_rate = input("Enter Death Rate Status: ")

    val = (spec_id, spec_name, scien_name, gen_name, zoo_count, global_count, origin, diet_type, endangered_status, feed_qunt, habitat_type, life_span, birth_rate, death_rate)

    try:
        dbCursor.execute(sql, val)
        print("success")
    except:
        print("error")
    dataBase.commit()

def create_multiple_records():
    data = []

    sql = "INSERT INTO ZOOMANAGE (SPECIES_ID, SPECIES_NAME, SCIENTIFIC_NAME, GENERIC_NAME, ZOO_COUNT, GLOBAL_COUNT, ORIGIN_COUNTRY, DIET_TYPE, ENDANGERED_RATE, FEEDING_QUANTITY, HABITAT_TYPE, LIFE_SPAN_IN_YEARS, BIRTH_RATE, DEATH_RATE)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    count = int(input("How many records do you want to enter?: "))
    for i in range(count):
        print("")
        spec_id = int(input("Enter Species ID(integer): "))
        spec_name = input("Enter Species Name: ")
        scien_name = input("Enter Scientific Name: ")
        gen_name = input("Enter Generic Name: ")
        zoo_count = int(input("Enter Zoo Count: "))
        global_count = int(input("Enter Global Count: "))
        origin = input("Enter Origin Country: ")
        diet_type = input("Enter Diet Type: ")
        endangered_status = input("Enter Endangered Status: ")
        feed_qunt = int(input("Enter Feeding Quantity: "))
        habitat_type = input("Enter Habitat Type: ")
        life_span = int(input("Enter Life Span (in years): "))
        birth_rate = int(input("Enter Birth Rate (no/year): "))
        death_rate = input("Enter Death Rate Status: ")
        print("")

        val = (spec_id, spec_name, scien_name, gen_name, zoo_count, global_count, origin, diet_type, endangered_status, feed_qunt, habitat_type, life_span, birth_rate, death_rate)
        data.append(val)

    try:
        dbCursor.executemany(sql, data)
        dataBase.commit()
        print("Success")
    except:
        print("Error!")

def fetch_all():
    sql = "SELECT * FROM ZOOMANAGE"
    dbCursor.execute(sql)

    fetched_data = dbCursor.fetchall()
    for i in fetched_data:
        print(i)

def fetch_where(field, op, payload):
    sql = f"SELECT * FROM ZOOMANAGE WHERE {field} {op} {payload}"
    dbCursor.execute(sql)

    fetched_data = dbCursor.fetchall()
    for i in fetched_data:
        print(i)
        

create_db()
create_table()

dataBase.close()

