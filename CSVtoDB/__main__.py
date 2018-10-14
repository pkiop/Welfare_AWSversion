import csv
import pymysql
import json
import os

#paas-ta에 있는 'VCAP_SERVICES에서 DB 접속 정보를 받아와 pymysql로 접속한다'


mydb = pymysql.connect( host='tempdb.cv6hktv7u8ad.us-east-2.rds.amazonaws.com', port=3306, user='root', passwd='11111111', db='tempdb', charset='utf8mb4')
cur = mydb.cursor()
tablename = "nationalcost"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('nationalcost.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "bokjiro"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")

cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('bokjiro.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "toyouth"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('toyouth.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "health"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('health.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "cityhall"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('cityhall.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()

cur = mydb.cursor()
tablename = "public"
cur.execute("CREATE TABLE IF NOT EXISTS " + tablename + "(ID INT PRIMARY KEY NOT NULL, \
                    TITLE TEXT, \
                    CONTENTS TEXT, \
                    DATE TEXT, \
                    TARGET TEXT, \
                    LINK TEXT, \
                    REGION TEXT, \
                    ASK TEXT, \
                    CONTACT TEXT, \
                    ORIGIN TEXT, \
                    CATEGORY TEXT)")
cur.execute("ALTER TABLE " + tablename + " CONVERT TO character SET utf8mb4")
mydb.commit()

f = open('public.csv','r', encoding='utf-8')
csv_data = csv.reader(f)

i = 0
for row in csv_data:
    if i == 0:
        i+=1
        continue
    print(row)
    cur.execute("INSERT INTO " + tablename + " (ID, TITLE, CONTENTS, DATE, TARGET, LINK, REGION, ASK, CONTACT, ORIGIN, CATEGORY ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))

mydb.commit()
cur.close()






mydb.close()
