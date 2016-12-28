#! /usr/bin/python3
"""[EASY] #295 Letter by Letter."""
# coding: utf-8

input1 = 'a fall to the floor'
input2 = 'braking the door in'

for i in range(len(input1) + 1):
    print(input2[0:i] + input1[i:])
