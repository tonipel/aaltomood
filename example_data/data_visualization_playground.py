# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:38:28 2020



"""

# library
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


### Monthly variation construction ###

### dates data gathered from SQL ###
dates = list()
for day in range(1, 31):
    #dates.append(date(2020, 11, day).isoformat())
    dates.append(str(day) + "-11")
    


averages = np.random.normal(2.9, 0.3, len(dates))
#myanswers = [random.randrange(1,6) for i in range(len(dates))]
myanswers = np.random.binomial(5, 0.6, len(dates))

#print(dates)

plt.plot(dates, averages)
plt.plot(dates, myanswers)

plt.xticks(dates,dates,rotation= 'vertical' )
plt.yticks(ticks = range(1,6))

### BarPlot construction ###

# Create bars
barWidth = 0.9
bars = (':D', ':)', ':|', ':(', ':C')
 
# The X position of bars
r1 = [1,2,3,4,5]

height = [3, 12, 5, 18, 4]

label = list()

for i in height:
    label.append(str(i))
    
print(label)

for i in range(len(r1)):
    plt.text(x = r1[i]-len(label[i])*0.1 , y = height[i]+0.1, s = label[i], size = 20)




# Create barplot
#p1 = a.bar(r1, height, color = ['green', 'greenyellow', 'yellow', 'orange', 'red'])
plt.bar(r1, height, color = ['#2db585', '#0f5251', '#bde8f1', '#fbdb44', '#fe6c3b'])


plt.xticks(r1, bars)

# Create legend
#plt.legend()
 
plt.show()
