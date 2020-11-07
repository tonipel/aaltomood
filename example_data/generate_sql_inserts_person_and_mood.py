# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:01:09 2020

@author: Anston


INSERT INTO mood_person
VALUES(1 {id}, 4 {wellbeing});

INSERT INTO mood_mood
VALUES(1 {mood id}, '2007-01-01' {date}, 0 {time} ,4 {moodval}, 1 {user_id});
"""
import numpy as np


f = open("sql_inserts.txt", "w")

# generate persons
n_persons = 10
n_moods = 30

wellness = np.random.binomial(5, 0.6, n_persons)

for id in range(1, n_persons + 1):
    f.write("\n\n--Generate person with id " + str(id) + "\n")
    f.write("INSERT INTO mood_person\nVALUES(" + str(id) + ", " 
                                             + str(wellness[id-1]) + ");\n")
    
    f.write("--Inserting moods for person " + str(id) + "\n")
    
    moods = np.random.binomial(5, wellness[id-1]*(9/50), n_moods)
    
    for day in range(1,n_moods+1):
        f.write("INSERT INTO mood_mood\nVALUES(" +
                str(id*1000+day) + ", \'2020-11-" +
                str(day).zfill(2) + "\', " + "0, " + str(moods[day-1]) +
                ", " + str(id) + ");\n")


f.close()

