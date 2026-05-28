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

def update_data(field, new_value, u_field, payload):
    sql = f"UPDATE ZOOMANAGE SET {field} = {new_value} WHERE {u_field} = {payload}"
    try:
        dbCursor.execute(sql)
        dataBase.commit()
        print("Success!")
    except:
        print("ERROR")

def delete_where(field, payload):
    sql = f"DELETE FROM ZOOMANAGE WHERE {field} = {payload}"
    try:
        dbCursor.execute(sql)
        dataBase.commit()
        print("Deleted!")
    except:
        print("Error!")

create_db()
create_table()


## MAIN FRONTEND:
print("="*35)
print("WELCOME TO ZOO MANAGEMENT SYSTEM V1")
print("="*35)
print("")
print("Choose An Operation From Below:")
print("")
print("1. Fetch All The Data From The Database")
print("2. Fetch With A Specific Constraint")
print("3. Insert Single Record")
print("4. Insert Multiple Records")
print("5. Update Data")
print("6. Delete Data")
print("")

choice = int(input("Enter A Choice (1-6): "))
if choice == 1:
    fetch_all()
elif choice == 2:
    field = input("Enter Cnstraint Field: ")
    op = input("Enter Constraint Operation: ")
    payload = input("Enter Target Value: ")
    fetch_where(field, op, payload)
elif choice == 3:
    create_single_record()
elif choice == 4:
    create_multiple_records()
elif choice == 5:
    field = input("Enter Updation Field: ")
    new_value = input("Enter new value (for string it must be 'value'): ")
    u_field = input("Enter contraint field: ")
    payload_1 = input("Enter contraint payload: ")
    update_data(field, new_value, u_field, payload_1)
elif choice == 6:
    field = input("Enter contraint field for deletion: ")
    payload_2 = input("Enter contraint payload for deletion: ")
    delete_where(field, payload_2)

dataBase.close()

