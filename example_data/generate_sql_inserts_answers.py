# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:07:13 2020

INSERT INTO mood_answers
VALUES(1 {a_id}, 0 {a: 0/1}, 1 {user_id}, 1 {q_id});

@author: Anston
"""


import numpy as np
import random


f = open("sql_inserts_answers.sql", "w")

# generate persons
n_persons = 10
n_days = 30

pos_q_of_day = [random.randrange(16,25) for i in range(30)]
neq_q_of_day = [random.randrange(1,16) for i in range(30)]

wellness = [5,2,4,2,1,3,2,5,4,3]


for id in range(1, n_persons + 1):
    
    f.write("--Inserting answers for person, one positive, one negative question answered per day " 
            + str(id) + "\n")
    
    pos_q = np.random.binomial(1, wellness[id-1]*(9/50), n_days)
    neq_q = np.random.binomial(1, 1 - wellness[id-1]*(9/50), n_days)
    
    for day in range(1,n_days+1):
        f.write("INSERT INTO mood_answers\nVALUES(" +
                str(id*1000+2*day-1) + ", " + str(pos_q[day-1]) + ", " +
                str(id) + ", " + str(pos_q_of_day[day-1]) + ");\n")
        
        f.write("INSERT INTO mood_answers\nVALUES(" +
                str(id*1000+2*day) + ", " + str(neq_q[day-1]) + ", " +
                str(id) + ", " + str(neq_q_of_day[day-1]) + ");\n")
        


f.close()