# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


def read_html(input_url):
    html = urllib.urlopen(input_url).read()
    return BeautifulSoup(html)


def extract_url(input_html, position):
    tags = input_html('a')
    next_url = tags[position].get('href', None)
    return next_url


def main(**kwargs):
    all_urls = []
    url = kwargs['url']
    position = kwargs['position'] - 1
    limit = kwargs['repeat']

    for j in range(limit):
        output = read_html(url)
        url = extract_url(output, position)
        all_urls.append(url)

    # print names
    for url in all_urls:
        extracted_name = re.findall('known_by_(\S+).html', url)
        print extracted_name[0]


if __name__ == '__main__':
    #my_vars = {'url': 'http://python-data.dr-chuck.net/known_by_Fikret.html', 'position': 3, 'repeat': 4}
    my_vars = {'url': 'http://python-data.dr-chuck.net/known_by_Lyall.html', 'position': 18, 'repeat': 7}
    main(**my_vars)
