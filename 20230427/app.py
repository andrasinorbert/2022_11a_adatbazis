# pip install pymysql

import pymysql

defaults={
    "DB_HOST": "127.0.0.1",
    "DB_NAME": "11a",
    "DB_TABLE": "szemelyek",
    "DB_PORT": 3306,
    "DB_USER": "root", #"11a_user",
    "DB_PASSWD":""  #"11a_user"
}

def connectDB(_host, _port, _database, _user, _password):
    return pymysql.connect(
            host=_host,
            port=_port,
            database=_database,
            user=_user,
            password=_password
        )

def selectDB(oszlopnevek, where=1):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    sql=f"""SELECT {oszlopnevek}
            FROM`{defaults['DB_TABLE']}`
            WHERE {where};"""
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.close()
    return rows

def doItDB(sql):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insertDB(tablename, nev, kor, magassag):
    sql=f"""INSERT INTO `{tablename}`
        (`név`, `kor`, `magasság`) VALUES 
        ('{nev}', '{kor}', '{magassag}');"""
    doItDB(sql)
    
def updateDB(tablename, mit, mire, szuresfelt=1):
    sql=f"""UPDATE {tablename}
            SET {mit}={mire}
            WHERE {szuresfelt};"""
    doItDB(sql)

def deleteRows(tablename, felt=0):
    sql=f"DELETE FROM {tablename} WHERE {felt};"
    doItDB(sql)

def truncateTable(tablename):
    sql=f"TRUNCATE TABLE {tablename};"
    doItDB(sql)

def dropTable(tablename):
    sql=f"DROP TABLE {tablename};"
    doItDB(sql)

def createDB(dbname):
    sql=f"CREATE DATABASE IF NOT EXISTS {dbname};"
    doItDB(sql)

def dropDB(dbname):
    sql=f"DROP DATABASE IF EXISTS {dbname};"
    doItDB(sql)

class Oszlop:
    def __init__(self, nev, tipus, megszoritas):
        self.name=nev
        self.type=tipus
        self.constraints=megszoritas
        
    def __str__(self):
        return f"{self.name} {self.type} {self.constraints}"
    
#x=Oszlop("név", "varchar(50)", "not null")
#x.name="Zolika"
#print(x)

def createTable(tablename, rowlist):
    sql=f"CREATE TABLE {tablename}("
    
    for i in rowlist:
        sql+= f"{i},"
    #sql=sql[:len(sql)-1]
    sql+=f"PRIMARY KEY ({rowlist[0].name})"
    sql+= ");"
    doItDB(sql)
    
lista=[]
lista.append(Oszlop("id", "INT", "NOT NULL AUTO_INCREMENT"))
lista.append(Oszlop("név", "VARCHAR(50)", "NOT NULL"))
lista.append(Oszlop("kor", "INT", "NOT NULL"))

createTable("adatok_v2", lista)

# CREATE TABLE Megszoritások:
    #NOT NULL - nem lehet NULL
        # Ensures that a column cannot have a NULL value
    #UNIQUE - egyediségi kényszer
        # Ensures that all values in a column are different
        # create table dolgozok (
        #     az int not null primary key auto_increment,
        #     ig varchar(10) unique,
        #     nev varchar(50)
        # );
    #PRIMARY KEY - kulcs
        # A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
        # create table osztalyok(
        #     az int not null primary key auto_increment,
        #     nev varchar(50)
        # );
        # ez ugyanaz, viszont ha több mint 1 attributum van, csak igy lehet:
        # create table osztalyok(
        #     az int not null auto_increment,
        #     nev varchar(50),
        #     primary key(az)
        # );
    #FOREIGN KEY - idegen kulcs
        # Prevents actions that would destroy links between tables
        # create table osztalyok(
        #     az int not null primary key auto_increment,
        #     nev varchar(50)
        # );
        # 
        # create table dolgozok(
        #     az int not null primary key auto_increment,
        #     nev varchar(50),
        #     osztalyAz int,
        #     foreign key (osztalyAz) references osztalyok (az)
        # );
    #CHECK - ellenőrzés
        # Ensures that the values in a column satisfies a specific condition
        # create table szamok (
        #     szam1 int check (szam1 >= 5),
        #     szam2 int check (szam2 >= 5),
        #     constraint nagyobb check (szam1>szam2)
        # );
    #DEFAULT - alapértelmezett érték
        # Sets a default value for a column if no value is specified
        # CREATE TABLE Persons (
        #     ID int NOT NULL,
        #     LastName varchar(255) NOT NULL,
        #     FirstName varchar(255),
        #     Age int,
        #     City varchar(255) DEFAULT 'Sandnes'
        # );
    #CREATE INDEX - indexelje az értékeket
        # ez azt jelenti, hogy gyorsabban tudunk keresni a megadottak közt
        # Used to create and retrieve data from the database very quickly
        


#insertDB("Sanyi", 14, 150)

#updateDB("magasság", 1500, "id=2")

#deleteDB("id=2")
#truncateTable("szemelyek")


#sorok=selectDB("*")

#for i in sorok:
#    print(i)

