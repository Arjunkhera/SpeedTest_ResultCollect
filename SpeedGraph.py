# Export png image and csv results of speedtest bash script
# Made by Arjun Khera

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import datetime
import sys

daysOfWeek = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
monthsofyear = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# providing the file name through command line
filename =  sys.argv[1]

# to manually provide the filename
# filename = "log240318.txt"

fin = open(filename, "rt")

downloadSpeed = []
uploadSpeed = []
time = []
date = []
day = []
month = []
year = []


for i in fin:
    # Obtain the time and day of test
    for j in daysOfWeek:
        if (i.startswith(j)):
            strTime = ''.join(i)
            day.append(j)
            time.append(re.findall(r'\d+',strTime))
            break;

    # Obtain month of test
    for k in monthsofyear:
        if k in i:
            month.append(k)
            break;

    # Obtain download speed
    if (i.startswith("Download")):
        strdown = ''.join(i)
        downloadSpeed.append(re.findall(r'\d+',strdown))

    # Obtain upload speed
    if (i.startswith("Upload")):
        strup = ''.join(i)
        uploadSpeed.append(re.findall(r'\d+',strup))

timereadings = []
downloadreadings = []
uploadreadings = []

for i in time:
    date.append(i[0])
    year.append(i[4])
    timereadings.append(i[1]+":"+i[2])

for i in downloadSpeed:
    downloadreadings.append(i[0]+"."+i[1])

for i in uploadSpeed:
    uploadreadings.append(i[0]+"."+i[1])

xaxis = np.arange(len(timereadings))

df = pd.DataFrame(list(zip(xaxis,date,day,month,timereadings,year,downloadreadings,uploadreadings)), columns = ["Serial No","Date","Day","Month","Time","Year","Download Speed","Upload Speed"])

# export as csv
df.to_csv(filename+".csv")


# draw a graph of upload and download speeds against the timestamp pf readings
fig,ax = plt.subplots()

fig.set_figheight(5)
fig.set_figwidth(7)

ax.plot(xaxis,downloadreadings,'bo',label="Download")
ax.plot(xaxis,uploadreadings,'ro',label="Upload")

ax.set_xticklabels(timereadings)

ax.set_title("Speed Test readings")
ax.legend(loc='upper right')
ax.grid(color='k', linestyle='-', linewidth=0.5)

ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# export the graph as png
fig.savefig(filename+".png")

# close the file
fin.close()
