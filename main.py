import mysql.connector

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
        print("Database exists!")

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
                    FEEDING_QUANTITY VARCHAR(30) NOT NULL,
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
        print("Table Already Exists!")

def create_single_record():
    pass

def create_multiple_records():
    pass

create_db()
create_table()

dataBase.close()

