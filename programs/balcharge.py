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
    print("연결오류. 다시 시도하십시오.")
    os.system("Pause")

except RuntimeError:
    print("암호화 문제/연결오류(서버가 열리지 않았을 수 있습니다.). 다시 시도하십시오.")
    os.system("Pause")

except:
    print("알 수 없는 오류가 발생하였습니다. 다시 시도해 주세요.")
    os.system("Pause")

num = int(input("충전할 ID를 입력하십시오 : "))
bal = int(input("충전할 금액을 입력하십시오 (예시 : 1000원의 경우, 1000) : "))

if bal <= 0:
    print("0원 이하는 충전하실 수 없습니다. 처음부터 다시 시도해 주세요.")
    os.system("Pause")

try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE member SET usrbal=usrbal + %s WHERE id = %s", (bal, num))
        cursor.execute("UPDATE member SET usrbal=usrbal + %s WHERE id = 99999", (bal))
        connection.commit()
        print("완료되었습니다.")
except:
    print("알 수 없는 오류가 발생하였습니다. 처음부터 다시 시도해 주세요.")

finally:
    connection.close()
    os.system("Pause")
