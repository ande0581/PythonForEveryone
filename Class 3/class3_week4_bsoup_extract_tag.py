# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = "http://python-data.dr-chuck.net/comments_42.html"
url = "http://python-data.dr-chuck.net/comments_322510.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

my_sum = []

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    my_sum.append(int(tag.contents[0]))

print "Count:", len(my_sum)
print "Sum:", sum(my_sum)

