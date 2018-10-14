from flask import Flask, request
import pymysql
import json
import os

#paas-ta DB 접속정보 받아와서 접속

# if 'VCAP_SERVICES' in os.environ:
#     print("do")
#     vcap_services = json.loads(os.environ['VCAP_SERVICES'])
#
#     if 'Mysql-DB' in vcap_services:
#         mysql_srv = vcap_services['Mysql-DB'][0]
#         mysql_cred = mysql_srv['credentials']

mysql_cred = { 'hostname' : 'korean.cv6hktv7u8ad.us-east-2.rds.amazonaws.com' , 'port' : 3306, 'username' : 'root', 'password' : '11111111','name' : 'tempdb'}


app = Flask(__name__)
lists = ['ID', 'TITLE', 'CONTENTS', 'DATE', 'TARGET', 'LINK', 'REGION', 'ASK', 'CONTACT', 'ORIGIN', 'CATEGORY']

#main 화면
@app.route("/")
def main():
    return "<a href='http://localhost:8080/health_all'>/health_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/health?ID=12'>/health?ID=12</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/bokjiro_all'>/bokjiro_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/bokjiro?ID=12'>/bokjiro?ID=</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/toyouth_all'>/toyouth_all</>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/toyouth?ID=12'>/toyouth?ID=</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/nationalcost_all'>/nationalcost_all</a>\
            <p>\
            <a href='http://testdb.paas-ta.co.kr/nationalcost?ID=12'>/nationalcost?ID=</h2>\
            "

#DB데이터 모두 출력
@app.route("/health_all", methods=["GET"])
def health_all():
    i=0
    #ERROR나면 10번 다시 시도
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from temp")
            result = []

            #json 형식으로 만들기
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            #list 2 json , ensure_ascii = False => 한글 제대로 출력
            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    #10번 다시시도해도 실패하면 ERROR
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/health",methods=["GET"])
def health():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from bokjiro where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from bokjiro where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/bokjiro_all", methods=["GET"])
def bokjiro_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from bokjiro")
            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/bokjiro",methods=["GET"])
def bokjiro():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from bokjiro where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from bokjiro where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/toyouth_all", methods=["GET"])
def toyouth_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from toyouth")
            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/toyouth",methods=["GET"])
def toyouth():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from toyouth where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from toyouth where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/nationalcost_all", methods=["GET"])
def nationalcost_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from nationalcost")
            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/nationalcost",methods=["GET"])
def nationalcost():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from nationalcost where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from nationalcost where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/cityhall_all", methods=["GET"])
def cityhall_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from cityhall")
            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/cityhall",methods=["GET"])
def cityhall():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from cityhall where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from cityhall where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB데이터 모두 출력
@app.route("/public_all", methods=["GET"])
def public_all():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()
            curs.execute("select * from public")
            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DB에서 ID와 타이틀 값에 맞는 데이터 출력
@app.route("/public",methods=["GET"])
def public():
    i=0
    while i != 10:
        try:
            ID = request.args.get('ID')
            TITLE = request.args.get('TITLE')
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()

            if ID is not None :
                curs.execute("select * from public where ID = " + ID)
            elif TITLE is not None :
                curs.execute("select * from public where TITLE = " + TITLE)

            result = []
            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#DialogFlow와 연동하기위한 route
@app.route('/webhook', methods=['POST',])
def create_book():
    output = ""
    try:
        conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
        cur = conn.cursor()
        req = request.data
        inputData = json.loads(req)['result']
        print(inputData)

        param = inputData['parameters']
        contexts = inputData['contexts']
        # actionName = inputData['action']

        serviceName = contexts[0]['parameters']['any.original']
        print("serviceName : ", serviceName)

        #table 합치기
        query = "select * from health where TITLE like '%" + str(serviceName) + "%' UNION \
                 select * from bokjiro where TITLE like '%" + str(serviceName) + "%' UNION \
                 select * from toyouth where TITLE like '%" + str(serviceName) + "%' UNION \
                 select * from cityhall where TITLE like '%" + str(serviceName) + "%' UNION \
                 select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                 select * from nationalcost where TITLE like '%" + str(serviceName) + "%'"

        curcnt = cur.execute(query)
        print(cur)
        if curcnt == 0:
            output = "해당 정보를 찾을 수 없습니다..."
        else:
            if param['When']:
                for x in cur:
                    txt = str(x[1]) + "의 신청기간은 " + str(x[3]) + "입니다."
                    output += txt
                    break
            elif param['Contact']:
                for x in cur:
                    txt = str(x[1]) + "관련 연락처는 " + str(x[8]) + "입니다."
                    output += txt
                    break
            elif param['How']:
                for x in cur:
                    txt = str(x[1]) + "관련 신청 방법은 " + str(x[5]) + "에서 확인 바랍니다."
                    output += txt
                    break
            elif param['Where']:
                for x in cur:
                    txt = str(x[1]) + "의 위치(주소) " + str(x[6]) + "입니다."
                    output += txt
                    break
            elif param['Who']:
                for x in cur:
                    txt = str(x[1]) + "의 적용 대상은 " + str(x[4]) + "입니다"
                    output += txt
                    break
            else :
                output = "해당 정보를 찾을 수 없습니다..."

        # print("param : {}".format(param))
        # print("context : {}".format(context))
        # res_msg = "{'fulfillmentMessages': [{'card': {'title': 'card title', 'subtitle': 'card text'}}]}"

    except Exception as e:
        print("database conn error")
        print(e)

        if conn:
            conn.rollback()
    else:
        print("output : ", output)

    finally:
        if conn:
            conn.close()

    res_msg = "{'speech': '%s', 'displayText': '%s'}" % (output, output)

    return res_msg


#고용
@app.route("/hire", methods=["GET"])
def hire():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "고용"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#문화
@app.route("/culture", methods=["GET"])
def culture():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "문화"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#의료
@app.route("/cure", methods=["GET"])
def cure():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "의료"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#보호안전
@app.route("/secure", methods=["GET"])
def secure():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "보호안전"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#생활
@app.route("/life", methods=["GET"])
def life():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "생활"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#금융
@app.route("/cash", methods=["GET"])
def cash():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "금융"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#주거
@app.route("/house", methods=["GET"])
def house():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "주거"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"

#교육
@app.route("/edu", methods=["GET"])
def edu():
    i=0
    while i != 10:
        try:
            conn = pymysql.connect( host=mysql_cred['hostname'], port=int(mysql_cred['port']), user=mysql_cred['username'], passwd=mysql_cred['password'], db=mysql_cred['name'], charset='utf8')
            curs = conn.cursor()


            req = request.data
            serviceName = "교육"
            query = "select * from health where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from bokjiro where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from toyouth where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from cityhall where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from public where CATEGORY like '%" + str(serviceName) + "%' UNION \
                     select * from nationalcost where CATEGORY like '%" + str(serviceName) + "%'"

            curs.execute(query)

            result = []

            for row in curs:
                temp_dic = {
                    'ID' : row[0],
                    'TITLE' : row[1],
                    'CONTENTS' : row[2],
                    'DATE' : row[3],
                    'TARGET' : row[4],
                    'LINK' : row[5],
                    'REGION' : row[6],
                    'ASK' : row[7],
                    'CONTACT' : row[8],
                    'ORIGIN' : row[9],
                    'CATEGORY' : row[10]
                }
                result.append(temp_dic)

            temp = json.dumps(result, ensure_ascii=False, separators=(',',':'))
            curs.close()
            conn.close()
            return temp
        except Exception as e :
            i+=1
            print("error is ==> ", e)
    return "<h1>ERROR</h1>"



if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=False)
