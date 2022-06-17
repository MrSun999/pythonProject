# -- ** -- UTF-8
import pymysql

def connect_DB(database,content):
    db = pymysql.Connection(host="localhost",user="root",password="123456",database=database)
    cursor = db.cursor()
    cursor.execute(content)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data


if __name__ == '__main__':
    database = "vaccine-test"
    cd =  connect_DB(database=database,content="SELECT * FROM user_info WHERE user_name = '123';")