# coding: utf-8

import re
# https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
# 用浏览器打开上面的网页，复制内容到string中
string = """ """

lst = re.findall('url=.+zip', string)
urls = "".join(url.split('=') for url in lst)
# 输出urls，复制urls内容到IDM中进行下载，"任务"->"从剪贴板中下载""
