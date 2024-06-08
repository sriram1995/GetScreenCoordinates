def duration(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print("%dh %dm %ds" % (hour , minutes, seconds))

import re
def convert_time_seconds(time):
    outtime_inseconds = []
    print("length" , len(time))
    for i in range(len(time)):
        timelist = [int(s) for s in re.findall(r'\d+', time[i])]
        if len(timelist) == 2:
            minutes ,seconds = timelist[0] * 60 , timelist[1]
            totaltime_seconds = minutes + seconds
            print(totaltime_seconds)
            outtime_inseconds.append(totaltime_seconds)
            #duration_seconds = sum(outtime_inseconds)
        elif len(timelist) == 3:
            hours , minutes , seconds = timelist[0] *3600 , timelist[1] * 60 , timelist[2]
            totaltime_seconds = hours + minutes + seconds
            print(totaltime_seconds)
            outtime_inseconds.append(totaltime_seconds)
            #duration_seconds = sum(outtime_inseconds)
        else:
            raise Exception
    #print(outtime_inseconds)



a = ['2m 59s' ,'1m 0s','1m 29s','0m 4s','0m 48s','1m 0s','1m 29s','1m 0s','0m 9s','0m 9s','0m 9s','2m 59s','5m 1s','2m 59s' , '1hr 00m 00s']
b = ['00m 18s' ,
'00m 11s',
'00m 5s',
'00m 36s',
'00m 59s',
'01m 0s',
'01m 10s',
'02m 49s',
'00m 44s',
'01m 21s',
'10m 55s',
'02m 31s',
'03m 01s',
'01m 58s',
'00m 30s',
'02m 07s',
'00m 43s',
'01m 01s',
'02m 29s',
'00m 59s',
'03m 15s',
'00m 42s',
'01m 11s',
'01m 37s',
'0m 9s',
'1m 0s',
'0m 48s',
'0m 4s',
'1m 29s',
'15m 30s',
'2m 59s',
'5m 1s',
'03m 51s',
'02m 30s',
'04m 21s',
'01m 58s',
'03m 23s',
'04m 33s',
'02m 02s',
'01m 50s',
'05m 12s',
'3m 26s',
'1m 0s',
'8m 22s',
'59m 58s',
'04m 02s',
'05m 30s',
'06m 33s',
'03m 11s',
'03m 26s',
'02m 19s',
'04m 04s',
'03m 17s',
'05m 03s',
'02m 44s']

#a = ['1hr 00m 00s',	'1hr 10m 22s']
convert_time_seconds(b)


