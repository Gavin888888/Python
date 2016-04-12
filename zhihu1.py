#-*-coding:utf8-*-
import re
import requests

html = requests.get('http://lab.grapeot.me/zhihu/touxiang/bai-yuan-yuan-73').text


pic_url = re.findall('src="../(.*?)"',html,re.S)
assert isinstance(html, object)
print('html:' + html)
i = 0
for each in pic_url:
    url = 'http://lab.grapeot.me/zhihu/' + each
    print('now downloading:' + url)
    pic = requests.get(url)
    fp = open('pic//' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1