import requests
import json
import csv
import time
import random
i=0
with open('tweets.csv',encoding = 'unicode_escape') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    f = open("demofile.txt", "a")
    for row in reader:
        # time.sleep(random.randint(5,10))
        # url="https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ta&dt=t&q="+row[1]
        # response = json.loads(requests.get(url).content.decode('utf-8'))[0][0][0]
        # print(response)
        # f.write(response)
        print(row[1])
        i+=1
        if i>=1000:
            break


# url="https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ta&dt=t&q="+query
# f = open("demofile.txt", "w")
# response = json.loads(requests.get(url).content.decode('utf-8'))[0][0][0]
# print(response)
# f.write(response)
