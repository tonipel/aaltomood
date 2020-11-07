# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:42:04 2020

INSERT INTO mood_questions
VALUES(1, -1, 0, 'Are you feeling overwhelmed by the amount of work you have to do?');

@author: Anston
"""

import csv


wfile = open("sql_inserts_questions.sql", "w")
id = 1
with open('example_questions.csv', 'r') as rfile:
    reader = csv.reader(rfile)
    for row in reader:
        wfile.write("INSERT INTO mood_questions\nVALUES("
                    + str(id) + ", " + row[1] + ", "
                    + row[2] + ", " + "\'"+row[0]+"\'" + ");\n\n")
        id += 1



wfile.close()
rfile.close()