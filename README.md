ViKi Instant
============

An incredibly ugly hack project. Uses jQuery to parse, search and run ViKi videos.

Notes
-----
ViKi Instant doesn't use the ViKi API directly. This is mostly due to i) slow
API speeds ii) the unavailability of a search API iii) the need to spoof
user-agent strings to get comprehensive video listings.

My approach is simple: I wrote two Python scripts get.py and getvids.py, to
grab titles and video ids of all the TV shows and movies on ViKi. This is serialized as
JSON to showids_final.json. 

In test.html showids_final.json is loaded up into a var, and all subsequent
searches are done against this JSON string. I use a Javascript port of
Quicksilver's search algorithm for searching video titles, a minified version of
which may be found in qs_score.js.

After that it's a simple matter of filling the movie div with ViKi embed code.

Time spent: 1.5 days. See a demo at http://elijames.org/viki/

Dependencies:
    ```jQuery
    pycurl (for the Python scripts)
    simplejson (for the Python scripts)
    ```
