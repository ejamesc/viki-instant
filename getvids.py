import pycurl
import simplejson as json
import os
import StringIO
""" I need a json string with show titles and corresponding video ids
    This file is used to construct and serialize such a string
    Uses pycurl to grab data from the Viki API
"""

with open('showids.txt') as f:
    showids = [i for i in f]

res = []
for id in showids:
    url = "http://www.viki.com/api/v2/shows/%s.json" % id
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, ["User-Agent: vikimobile/4.0"])

    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    tmpstr = b.getvalue()
    b.close()
    print tmpstr
    try:
        j = json.loads(tmpstr)
        epilist = j["media"]
        for e in epilist:
            #print e
            curr = {}
            curr["title"] = j["title"] + " " + e["title"]
            curr["id"] = e["id"]
            res.append(curr)
    except (json.decoder.JSONDecodeError, ValueError):
        print "ERROR:", tmpstr
        pass
   
with open('movieids.txt') as f:
    movieids = [i for i in f]

for id in movieids:
    url = "http://www.viki.com/api/v2/shows/%s.json" % id
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, ["User-Agent: vikimobile/4.0"])

    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    tmpstr = b.getvalue()
    b.close()
    print tmpstr

    try:
        j = json.loads(tmpstr)
        mov = j["media"]
        for m in mov:
            curr = {}
            curr["title"] = j["title"]
            curr["id"] = m["id"]
            res.append(curr)
    except (json.decoder.JSONDecodeError, ValueError):
        print "ERROR:", tmpstr
        pass

with open('showids_final.json', 'w') as f:
    f.write(json.dumps(res, sort_keys = True, indent = 4))


