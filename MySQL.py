__author__ = 'Toso'
import MySQLdb

def MySQLData(data):
    sql="insert into user VALUES('"+data+"','"+data+"')"
    print(sql)
    db=MySQLdb.connect('127.0.0.1','root','123456','Toso')
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()