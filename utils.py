import urllib2
key = " 8ee67db7de50f8ae9437606376ac7a90:1:63152520"
defaulturl = "http://api.nytimes.com/svc/politics/v3/us/legislative/congress/113/senate/members/current.json?api-key=%s"

def getcongress ():
    actualurl = defaulturl%(key)
    request = urllib2.urlopen(actualurl)
    data = request.read()
    print data
