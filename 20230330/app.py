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

conn=pymysql.connect(
    host=defaults["DB_HOST"],
    port=defaults["DB_PORT"],
    database=defaults["DB_NAME"],
    user=defaults["DB_USER"],
    password=defaults["DB_PASSWD"]
)

cursor=conn.cursor()

nev="Józsi"
kor=45
magassag=200

sql=f"""INSERT INTO `{defaults['DB_TABLE']}`
    (`név`, `kor`, `magasság`) VALUES 
    ('{nev}', '{kor}', '{magassag}');"""

cursor.execute(sql)
conn.commit()
conn.close()
