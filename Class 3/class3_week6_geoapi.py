import json
import urllib
from pprint import pprint as pp


def main():
    location = raw_input('Enter location: ')
    if len(location) < 1:
        #location = 'South Federal University'
        location = 'Saint Petersburg State University of Aerospace Instrumentation'

    url = "http://python-data.dr-chuck.net/geojson?{}".format(urllib.urlencode({'sensor': 'false', 'address': location}))
    result = urllib.urlopen(url).read()
    js = json.loads(result)

    #print pp(js)

    print "Place id {}".format(js['results'][0]['place_id'])

if __name__ == '__main__':
    main()
