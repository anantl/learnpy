'''
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
'''

from __future__ import division

count = int(raw_input())

a = {}
for i in range(count):
    marks = raw_input().split(" ");
    average = 0.00
    for j in range(1,4):
        average = average + float(marks[j])
    average = average / 3.00;
    a[marks[0]] = average

print("%.2f"%round(a[raw_input()],2));
