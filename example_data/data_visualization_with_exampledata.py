# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:38:24 2020



@author: Anston
"""


#import os.path
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
#import numpy as np


#sql_location = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/db.sqlite3"
#print(sql_location)

sql_location = "C:/Users/Anston/aaltomood/db.sqlite3"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_my_moods(conn, user_id):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT date,value FROM mood_mood WHERE user_id = " + str(user_id))

    rows = cur.fetchall()
    
    my_moods = list()#np.random.binomial(5, 0.6, len(dates))
    dates = list()

    for row in rows:
        my_moods.append(row[1])
        dates.append(row[0])
    
    return my_moods, dates


def select_average_moods(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT date, AVG(value) FROM mood_mood GROUP BY date")

    rows = cur.fetchall()
    
    avg_moods = list()#np.random.binomial(5, 0.6, len(dates))
    dates = list()

    for row in rows:
        avg_moods.append(row[1])
        dates.append(row[0])
    
    return avg_moods, dates


def select_days_moods(conn, day):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), value FROM mood_mood WHERE date = " +"\'"+day+"\'" + " GROUP BY value")

    rows = cur.fetchall()
    
    moodcounts = [0]*6#np.random.binomial(5, 0.6, len(dates))
    #dates = list()

    for row in rows:
        #print(row)
        moodcounts[row[1]] = row[0]
    
    return moodcounts
    

        

conn = create_connection(sql_location)

avg_moods, dates = select_average_moods(conn)
my_moods, my_dates = select_my_moods(conn, 7)


plt.plot(dates, avg_moods)
plt.plot(my_dates, my_moods)

plt.xticks(dates,dates,rotation= 'vertical' )
plt.yticks(ticks = range(1,6))

plt.savefig('my_moods_month.png', dpi = 600, transparent = True)
plt.show()

plt.clf()

# Generate barplots of how responders are doing today

barWidth = 0.9
bars = ('?', ':C', ':(', ':|', ':)', ':D')
 
# The X position of bars
r1 = [1,2,3,4,5,6]

height = select_days_moods(conn, "2020-11-02")



label = list()

for i in height:
    label.append(str(i))
    
print(label)

for i in range(len(r1)):
    plt.text(x = r1[i]-len(label[i])*0.1 , y = height[i]+0.1, s = label[i], size = 12)




# Create barplot
#p1 = a.bar(r1, height, color = ['green', 'greenyellow', 'yellow', 'orange', 'red'])
plt.bar(r1, height, color = ['#ffffff','#2db585', '#0f5251', '#bde8f1', '#fbdb44', '#fe6c3b'])

#plt.yticks(range(max(height)+2))
plt.yticks([])
plt.ylim((0, max(height)+1))
plt.xticks(r1, bars)

# Create legend
#plt.legend()
plt.savefig('aalto_moods_today', dpi = 400, transparent = True)
 
plt.show()


