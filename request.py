#Sample program which works as a monitoring tool for webssites
#Author - Amit Joshi
import json
#import request
import requests
import time
import urllib
from datetime import datetime

#Check if the website response is fine
def check_website_response(sa, ft):
    try:
        start_time = time.time()
        source = requests.get(sa)
        work_latency = time.time() - start_time
        source.raise_for_status()
    except requests.exceptions.RequestException as err:
        print("Some other error", err)
        fw.write(sa.rstrip() + "|" + ft.rstrip() + "|" + str(err).rstrip() + "\n" )
        return None

    return_code = str(source.status_code)

    if ft.rstrip() in source.text:
        string_matched = "string present in the output"
    else:
        string_matched = "string is not present in the output"
    fw.write(sa.rstrip() + "|" + ft.rstrip() + "|" + return_code.rstrip() + "|" + string_matched.rstrip() + "|" + "time elapsed in seconds:" + str(work_latency).rstrip() + "\n" )


if __name__ == '__main__':
    #The loop runs forever
    while(True):
        #the opt directory is mapped with local working directory
        fw = open("/opt/logfile.txt", "a+")
        f = open("/opt/website_list.txt" , "r")
        fw.write("\n" + "Check started at:" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "\n\n")

        line_read = f.readlines()

        time_interval = 0
        for match_string in line_read:
            if "time interval" in match_string:
                key, time_interval = match_string.split(':')
                if int(time_interval) == 0:
                    fw.write("\n time interval not set to non zero value. set time interval in seconds \n")
                    break
                continue

                 # raise Exception("time interval not set to non zero value. set time interval in seconds")
            comma_seperated = match_string.split(',')
            site_add, find_text = comma_seperated
            check_website_response(site_add, find_text)


        f.close()
        fw.close()
        time.sleep(int(time_interval))
