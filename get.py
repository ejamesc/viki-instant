import pycurl
import os
import simplejson as json
""" Grabs all channel ids and serializes to file.
    (ids alone may come in useful later)
"""

file = open('shows.json')
a = file.read()
file.close()

b = json.loads(a)

print b
show_ids, movie_ids = [], []

shows, movies = b['tv_shows'], b['films']

for i in shows:
    show_ids.append(i["id"])

for i in movies:
    movie_ids.append(i["id"])

with open('showids.txt', 'w') as f:
    for i in show_ids:
        f.write(str(i))
        f.write('\n')

with open('movieids.txt','w') as f:
    for i in movie_ids:
        f.write(str(i))
        f.write('\n')

