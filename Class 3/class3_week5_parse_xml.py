import urllib
import xml.etree.ElementTree as ET


def enter_url():
    url = raw_input('Enter a URL: ')
    if len(url) < 1:
        #url = 'http://python-data.dr-chuck.net/comments_42.xml'
        url = 'http://python-data.dr-chuck.net/comments_322507.xml'
    return url


def main():
    url = enter_url()
    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved', len(data), 'characters'
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    my_sum = []

    for count in counts:
        my_sum.append(int(count.text))

    print "Count:", len(my_sum)
    print "Sum:", sum(my_sum)


if __name__ == '__main__':
    main()
