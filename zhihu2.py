#-*-coding:utf8-*-
import re
import requests

html = requests.get('http://lab.grapeot.me/zhihu/autoface').text

pic_url = re.findall('img src="(.*?)"',html,re.S)
assert isinstance(html, object)
print('html:' + html)
i = 0
for each in pic_url:
#     if "/zhihu/imgs/" in each:
#         continue
#         # each = each.replace('/zhihu/imgs/','')
#         print('-------------yes----old image name = ' + each)
#         # print('-------------yes----new image name = ' + newimage)
    url = "http://lab.grapeot.me" + each
    print('current = now downloading:' + url)
    pic = requests.get(url)
    fp = open('pic//' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
