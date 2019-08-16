#coding:utf-8

import csv
import datetime
import random
import string
from tqdm import tqdm


file_number = input("最初のファイルNo.は？＞")
file_numbers = input("最後のファイルNo.は？＞")


while  int(file_number) <= int(file_numbers):
    with open("No." + str(file_number) + "text.tsv","w+", newline = "") as new_file:#test.tsvというファイルを新規作成。変数名「ｔ」
        s = csv.writer (new_file, delimiter="\t")
        fieldnames = ["log_id", "date", "latitude", "longitude"]
        writer = csv.DictWriter(new_file, fieldnames = fieldnames , delimiter="\t")
        writer.writeheader()
        file_number = int(file_number) + 1
        
        for a in tqdm(range(1, 10000+1)):
            timesone = random.uniform(datetime.datetime(2000, 1, 1), datetime.datetime(2019, 1, 1))
            
            months, days, hours, minutes, seconds = timesone.month, timesone.day, timesone.hour, timesone.minute, timesone.second 
            
            
            timestwo = str(timesone.year) + "-" + '{0:02d}'.format(months) + "-" +\
                    '{0:02d}'.format(days) + "T" + '{0:02d}'.format(hours) + ":" +\
                    '{0:02d}'.format(minutes) + ":" + '{0:02d}'.format(seconds) + "Z"
            
            idone =string.digits + string.ascii_uppercase
            def randomname(n):
                return ''.join([random.choice(idone) for i in range(1, 8+1)])
            def randomnames(n):
                return ''.join([random.choice(idone) for i in range(1, 4+1)])
            def names(n):
                return ''.join([random.choice(idone) for i in range(1, 4+1)])
            def name(n):
                return ''.join([random.choice(idone) for i in range(1, 4+1)])
            def randoms(n):
                return ''.join([random.choice(idone) for i in range(1, 12+1)])

            log = str(randomname(7)) + "-" + str(randomnames(7)) + "-" + str(names(7)) + "-" + str(name(7)) + "-" + str(randoms(7))
            lat = random.uniform(34.5, 35.5)
            long = random.uniform(134, 139)
            writer.writerow({"log_id": log, "date" : timestwo, "latitude": ('{:.6f}'.format(lat)), "longitude":  ('{:.6f}'.format(long))})
        
        print(str(file_number) + " files generated")


