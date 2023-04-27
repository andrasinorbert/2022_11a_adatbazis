# pip install pymysql

import pymysql

defaults={
    "DB_HOST": "127.0.0.1",
    "DB_NAME": "11a",
    "DB_TABLE": "szemelyek",
    "DB_PORT": 3306,
    "DB_USER": "11a_user",
    "DB_PASSWD":"11a_user"
}

def connectDB(_host, _port, _database, _user, _password):
    return pymysql.connect(
            host=_host,
            port=_port,
            database=_database,
            user=_user,
            password=_password
        )

def insertDB(nev, kor, magassag):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    sql=f"""INSERT INTO `{defaults['DB_TABLE']}`
        (`név`, `kor`, `magasság`) VALUES 
        ('{nev}', '{kor}', '{magassag}');"""
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
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

def updateDB(mit, mire, szuresfelt=1):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    sql=f""" UPDATE szemelyek
            SET {mit}={mire}
            WHERE {szuresfelt};"""
    cursor.execute(sql)
    conn.commit()
    conn.close()

def deleteDB(felt=0):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    sql=f""" DELETE FROM `szemelyek` WHERE {felt};"""
    cursor.execute(sql)
    conn.commit()
    conn.close()

def truncateTable(tablename):
    conn=connectDB(
        _host=defaults["DB_HOST"],
        _port=defaults["DB_PORT"],
        _database=defaults["DB_NAME"],
        _user=defaults["DB_USER"],
        _password=defaults["DB_PASSWD"]
    )
    cursor=conn.cursor()
    sql=f"""TRUNCATE TABLE {tablename};"""
    cursor.execute(sql)
    conn.commit()
    conn.close()

#insertDB("Sanyi", 14, 150)

sorok=selectDB("név")

for i in sorok:
    print(i)
