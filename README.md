# Bank ![python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg) 
![license](https://img.shields.io/github/license/sevrino/bank.svg) 
![[ver](https://img.shields.io/github/release/sevrino/back.svg)
![issue](https://img.shields.io/github/issues/sevrino/bank.svg)

학교 축제용(미니 벼륙시장용) 뱅킹 시스템

학교 축제(미니 벼룩시장 등)의 종이 화폐를 변경하여 분실의 위험 및 합계 계산의 오류를 줄이기 위함.
웹으로 연동시켜 완전한 페이 시스템 구현 

## Installation
Python 3.5 이상 설치

MySQL 8.0 이상 설치 

### pip로 필요 라이브러리 설치 
```
pip3 install pymysql
```

## Usage
### MySQL 설정
mysql server 실행
mysql/mysql_TBL_setup.sql(예제파일, 수정 후 사용바람)을 실행하여 데이터베이스 설정
### 프로그램 배포
programs 폴더의 pos.py는 판매자, balcharge.py는 잔액 충전소, balcheck.py는 잔액 확인소에 배포(Python이 설치되지 않은 컴퓨터거나 PymySQL이 설치되지 않은 컴퓨터는 Installation 단계를 따르십시오.)  
* pos.py 실행시 지불할 학번(id) 입력, 지불 금액 입력, 완료/실패시 잔액, 실패 사유 표시됨.
* balcharge.py 실행시 충전할 학번(id) 입력, 충전 금액 입력, 완료/실패시 잔액, 실패 사유 표시됨.
* balcheck.py 실행시 잔액조회할 학번(id) 입력, 잔액 표시됨.
