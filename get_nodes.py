#Python Script to fetch Tornodes from
#https://www.dan.me.uk/tornodes
#Python 2.7.11

import urllib
from w3lib.html import replace_entities
import requests
import schedule
import time

def get_tor_nodes():
    print "Fetching Nodes"
    url="https://www.dan.me.uk/tornodes"

    try:
        r = requests.get(url)
    except ConnectionError, e:
        print e
        return

    #Flag to Mark Beginning and Ending
    lines_capture=False


    set_alert=False
    count=0
    for x in r.text.splitlines():
        if "You can only fetch the data every 30 minutes" in x:
            set_alert=True
            break
        
        if lines_capture==False:
            if "<!-- __BEGIN_TOR_NODE_LIST__ //-->" in x:
                #Open the file if nodes are present
                f = open('tornodes.txt', 'w')
                lines_capture=True
                continue

        if "<!-- __END_TOR_NODE_LIST__ //-->" in x:
            f.close()
            lines_capture=False

    #Unicode Encode Decode:
    #convert &lt; to "<" and encode unicode characters so they can be stored into text files
        if lines_capture==True:
            count=count+1
            f.write((replace_entities(x.strip("<br />").strip("|"))).encode('utf8')+"\n")

    #If 30 Minutes Reached
    if set_alert==True:
        print "Already Accessed in 30 Minutes"

    #Display total Nodes fetched
    else:
        print "Success!"
        print "Total nodes found are "+str(count)

#Schedule function every 30 minutes
schedule.every(30).minutes.do(get_tor_nodes)

#For first time
get_tor_nodes()
print "Next will run in 30 Minutes"

#Check whether to fetch or not every second.
while True:
    schedule.run_pending()
    time.sleep(1)
