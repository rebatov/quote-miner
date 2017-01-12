# -*- coding: utf-8 -*-
# @Author: bishal
# @Date:   2017-01-12 12:30:46
# @Last Modified by:   bishal
# @Last Modified time: 2017-01-12 14:26:40
from lxml import html
import requests
import json
url = 'https://www.brainyquote.com/quotes/topics/topic_relationship'
quotexpathleft='//*[@id="quotesList"]/div['
quotexpathright=']/div[1]/span/a/text()'
authorxpathleft = '//*[@id="quotesList"]/div['
authorxpathright = ']/div[1]/div/a/text()'
content = []
for i in xrange(2,39):
	urlnew = url+str(i)+'.html'
	page = requests.get(urlnew)
	tree = html.fromstring(page.content)
	for j in xrange(1,16):
		quote=tree.xpath(quotexpathleft+str(j)+quotexpathright)
		author=tree.xpath(authorxpathleft+str(j)+authorxpathright)
		# print quote,author
		q={"quote":quote[0],"author":author[0]}
		content.append(q)

# print content
string = json.dumps(content)
JSON = json.loads(string)
print(JSON)
with open('relationship.json','w') as outfile:
	json.dump(JSON,outfile)

# page = requests.get('https://www.brainyquote.com/quotes/topics/topic_technology.html')
# tree = html.fromstring(page.content)
# print tree
# quote=tree.xpath('//*[@id="quotesList"]/div[1]/div[1]/span/a/text()')
# print quote
# //*[@id="quotesList"]/div[2]/div[1]/span/a
# //*[@id="quotesList"]/div[1]/div[1]/div/a
# //*[@id="quotesList"]/div[2]/div[1]/div/a