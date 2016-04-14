#-*-coding:utf8-*-
import re
import requests
import MySQLdb
try:
    connect = MySQLdb.connect(host='localhost',user='root',passwd='lsb',port=3306)
    cur = connect.cursor()
    db_name = 'py_db'
    cur.execute('create database if not exists '+db_name)
    connect.select_db(db_name)
    cur.execute('create table test(id int,info varchar(200))')
    value = [1,'hi python db']
    cur.execute('insert into test values(%s,%s)',value)
    connect.commit()
    # cur.close()
    # connect.close()
except MySQLdb.Error,e:
    print('-----db error :' + e)
finally:
    print('-------please try again')

html = requests.get('http://lab.grapeot.me/zhihu/autoface').text

pic_url = re.findall('img src="(.*?)"',html,re.S)

user_webview = re.findall('a href="(.*?)"',html,re.S)
assert isinstance(html, object)
print('html:' + html+'/n')
# print(pic_url)
i = 0
for i in range(0,len(pic_url)):
#     if "/zhihu/imgs/" in each:
#         continue
#         # each = each.replace('/zhihu/imgs/','')
#         print('-------------yes----old image name = ' + each)
#         # print('-------------yes----new image name = ' + newimage)
    print(user_webview)
    user_url= user_webview[i]
    print('------------------')
    print(user_url)
    value = [i,user_url]
    cur.execute('insert into test values(%s,%s)',value)
    connect.commit()
    print('insert result: ----')
    # i += 1
    # each = pic_url[i]
    # url = "http://lab.grapeot.me" + each
    # print('current = now downloading:' + url)
    # pic = requests.get(url)
    # fp = open('pic//' + str(i) + '.jpg','wb')
    # fp.write(pic.content)
    # fp.close()
    # i += 1
