import re


def timeconvertlist(inputlist):
    ts=[]
    for time in range(len(inputlist)):
        t =[int(s) for s in re.findall(r'\d+', inputlist[time])]
    #print(t)
        minutes=60*60
        seconds=60
        totalseconds = (t[0]*minutes) + (t[1]*seconds) + t[2]
        ts.append(totalseconds)
    print(ts)


#a = ['00h 00m 5s', '00h 00m 59s', '00h 02m 31s', '00h 05m 20s', '00h 10m 52s','00h 00m 48s','00h 00m 09s','00h 05m 01s','00h 04m 27s','00h 21m 15s','00h 05m 30s','00h 08m 22s','00h 03m 26s','00h 10m 04s','01h 28m 44s']

c = ['00h 00m 18s',
'00h 00m 11s',
'00h 02m 53s',
'00h 04m 20s',
'00h 10m 52s',
'00h 01m 29s',
'00h 00m 09s',
'00h 02m 24s',
'00h 05m 58s',
'00h 45m 36s',
'00h 03m 26s',
'00h 05m 30s',
'00h 06m 02s',
'00h 06m 02s',
'01h 34m 48s'
]
timeconvertlist(c)


