#!/usr/bin/python

import os
import sys
import subprocess as sub

users = []

def configSkel():

    contents = "set showmode\n",
    "start\n",
    "map #2 :set number\n"
    "map #3 :set nonumber\n"
    filepath = os.path.join('/etc/skel', '.exrc')
    if not os.path.exists('/etc/skel'):
        os.makedirs('/etc/skel')
    print("[Writing .exrc to /etc/skel]")
    f = open(filepath, "w")
    f.write(contents)
    f.close()

def readIn():
    filename = str(sys.argv[1])
    filein = open(filename)
    print('[Reading file..' , filename, ']')
    global users

    for line in filein:

        a = line.split(",")
        for i in range(5):
            a[i] = a[i].replace('"', '').strip("\n")
        users.append(a)
        name = a[0], a[1]
        building = a[2]
        phone = a[3]
        department = a[4]

        print(name[0] + ' ' + building + ' ' + phone + ' ' + department)

def enterUsers():
    count = 0
    '''
    for entry in users:
        fname = entry[1].split(" ")
        print('useradd', '–s', '/bin/csh', '–m', '–d', '/home/'+entry[4], '–g', entry[4],'-c','"'+ entry[2] + " "
              + entry[3]+'"', fname[1][0] + entry[0])
'''
    for entry in users:
        fname = entry[1].split(" ")
        if entry[4] == "Engineering":
            print("Engineer")
            p = sub.Popen(['useradd', '–s', '/bin/csh', '–m', '–d', '/home/'+entry[4], '–g', entry[4],'-c','"'+ entry[2] + " "
              + entry[3]+'"', fname[1][0] + entry[0]],stdout=sub.PIPE,stderr=sub.PIPE)
        else:
            p = sub.Popen(['useradd', '–s', '/bin/bash', '–m', '–d', '/home/'+entry[4], '–g', entry[4],'-c','"'+ entry[2] + " "
              + entry[3]+'"', fname[1][0] + entry[0]],stdout=sub.PIPE,stderr=sub.PIPE)
        output,errors = p.communicate()
        print(output)

configSkel()
readIn()
enterUsers()
