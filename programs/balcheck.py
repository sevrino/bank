import pymysql.cursors
import os

try:
     connection = pymysql.connect(host='xxx',
                            user='root',
                            password='xxx',
                            db='bank',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)

except pymysql.err.OperationalError:
    print("연결오류. 다시 시도하십시오.")
    os.system("Pause")

except RuntimeError:
    print("암호화 문제/연결오류/비밀번호 오류. 다시 시도하십시오.")
    os.system("Pause")

num = int(input("조회할 ID(학번)을 적어주십시오 : "))

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM bank.member WHERE id=%s"%(num))
    result = cursor.fetchone()
    print("입력하신 %s의 잔액은 %s원입니다(usrbal이 잔액입니다.)."%(num, result))
except:
    print("알 수 없는 오류가 발생하였습니다. 처음부터 다시 시도해 주세요.")
finally:
    with connection.cursor() as cursor:
        connection.close()
        os.system("Pause")
