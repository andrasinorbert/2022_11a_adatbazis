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
    
CREATE TABLE 11a.ValamiTable` (`id` INT NOT NULL AUTO_INCREMENT , `név` VARCHAR(50) NOT NULL , `kor` INT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
    
    
    
createDB("tesztdb")
dropDB("tesztdb")
    
#insertDB("Sanyi", 14, 150)

#updateDB("magasság", 1500, "id=2")

#deleteDB("id=2")
#truncateTable("szemelyek")


#sorok=selectDB("*")

#for i in sorok:
#    print(i)
