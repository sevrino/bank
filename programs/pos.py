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

total = int(99999)
pos = int(input("pos용 id를 입력하십시오(1학년 1반의 경우, 101이 pos용 id입니다.) : "))
num = int(input("학번을 입력하십시오 : "))
bal = int(input("사용할 금액을 입력하십시오 : "))

if bal <= 0:
    print("0원 이하는 입력하실 수 없습니다. 다시 시도하십시오.")
    os.system("Pause")
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE member SET usrbal=usrbal - %s WHERE id=%s", (bal, num)) # 값 차감(정산)
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=%s", (bal, num)) # 게스트 사용값 증가
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=%s", (bal, pos)) # pos 사용값 증가
        cursor.execute("UPDATE member SET usruse=usruse + %s WHERE id=99999", (bal)) # 토탈(총매출) 값 증가
        connection.commit()
        cursor.execute("SELECT * FROM bank.member WHERE id=%s" % (num))
        result = cursor.fetchone()
        print("완료되었습니다. 잔액은 %s원 남았습니다(usrbal이 잔액입니다.)." % (result))
except:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM bank.member WHERE id=%s" % (num))
        result = cursor.fetchone()
        print("잔액이 부족합니다. 현재 잔액은 %s원입니다(usrbal항목이 잔액입니다.). 충전 후 다시 이용해 주세요." % (result))
finally:
    connection.close()
    os.system("Pause")
