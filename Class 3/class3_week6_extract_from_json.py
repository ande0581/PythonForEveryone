import json
import urllib
from pprint import pprint as pp


def main():
    url = raw_input('Enter url for JSON Data:')
    if len(url) < 1:
        #url = "http://python-data.dr-chuck.net/comments_42.json"
        url = "http://python-data.dr-chuck.net/comments_322511.json"
    print "Retrieving URL: {}".format(url)

    try:
        uh = urllib.urlopen(url)
    except IOError as e:
        print e
        main()

    data = uh.read()
    print "Retrieved: {} characters".format(len(data))
    js = json.loads(data)
    #print pp(js)

    my_sum = []
    for k in js['comments']:
        my_sum.append(int(k['count']))

    print "Sum: {}".format(sum(my_sum))

if __name__ == '__main__':
    main()
