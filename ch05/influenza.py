import csv
import pymysql

HOST_NAME = 'localhost'
USER = 'root'
PASSWORD = ''
DB_NAME = "influenza"
TABLE_NAME = "influenza"

db = pymysql.connect(host=HOST_NAME,user=USER,password=PASSWORD,database=DB_NAME,charset="utf8")
cursor = db.cursor()

csvfile = "RODS_Influenza_like_illness.csv"
with open(csvfile, 'r', encoding='utf8') as fp:
    reader = csv.reader(fp)
    for idx, row in enumerate(reader):
        if idx != 0:
            sql = """INSERT INTO `{5}`
                    (`year`, `week`, `age`, `city`, `people_count`)
                    VALUES ({0},{1},'{2}','{3}','{4}')"""
            sql = sql.format(row[0], row[1], row[2], row[3], row[4], TABLE_NAME)
            try:
                cursor.execute(sql)
                db.commit()
                print('新增資料成功: ', row)
            except:
                db.rollback()
                print('新增記錄失敗: ', row)
db.close()


