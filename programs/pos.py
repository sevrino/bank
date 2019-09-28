import pymysql.cursors
import os

try:
    connection = pymysql.connect(host='xxx',
                                 port=3306,
                                 user='root',
                                 passwd='xxx',
                                 db='bank',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
except pymysql.err.OperationalError:
    print("ConnectionSetting error. Retry please.")
    os.system("Pause")
except RuntimeError:
    print("Connection Error. Retry please.")
    os.system("Pause")
except:
    print("Undefined error. Retry please")
    os.system("Pause")

total = int(99999)
pos = int(input("Please insert posid : "))
num = int(input("Please insert is : "))
bal = int(input("Please insert price : "))

if bal <= 0:
    print("You can't enter a value lower than zero.")
    os.system("Pause")
try:
    with connection.cursor() as cursor:
        # Reduction in Value
        cursor.execute("UPDATE member SET usrbal=usrbal - %s WHERE id=%s", (bal, num))
        # Add User Useage Value
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=%s", (bal, num))
        # Add PosTotal Value
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=%s", (bal, pos))
        # Add Total Value
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=99999", (bal)) 
        connection.commit()
        cursor.execute("SELECT * FROM bank.member WHERE id=%s" % (num))
        result = cursor.fetchone()
        print("Compulete. Now your balance is %s.(Please check usrbal)" % (result))
except:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM bank.member WHERE id=%s" % (num))
        result = cursor.fetchone()
        print("Balance is low. now balance is %s.(usrbal). Please add your balance." % (result))
finally:
    connection.close()
    os.system("Pause")
