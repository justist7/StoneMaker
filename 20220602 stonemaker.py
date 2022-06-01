# -*- coding: utf-8 -*-
import sys
import random
import numpy as np

sys.setrecursionlimit(1000000000) 

def bp(p) :
  if p >= 75 :
    return 75
  elif p <= 25 :
    return 25
  else :
    return p
def bas(a) :
  if a <= -0.5 :
    return 0
  else :
    return a

def ok(s) :
  if s == 0 :
    return 0
  else :
    return 1

p = 75
s1 = int(input("1번칸수"))
s2 = int(input("2번칸수"))
s3 = int(input("3번칸수"))
a1 = int(input("1번목표"))
a2 = int(input("2번목표"))


print("잠시기다려주세요")

global problist
problist = np.ones([15, 15, 15, 15, 15, 100])
problist = -1 * problist
global count
count = 0
global count2
count2 = 0



global p1list
p1list = np.ones([15,15,15,15,15,100])
p1list = -1 * p1list
global p2list
p2list = np.ones([15,15,15,15,15,100])
p2list = -1 * p2list
global p3list
p3list = np.ones([15,15,15,15,15,100])
p3list = -1 * p3list

def p1(s1, s2, s3, a1, a2, p):
  global p1list
  temp_prob = 0
  if p1list[s1, s2, s3, a1, a2, p] >= -0.5 :
    temp_prob = p1list[s1, s2, s3, a1, a2, p]
  elif a1 == 0 and a2 == 0 :
    temp_prob = 1
  elif (s1 == 0 and a1 != 0) or (s2 == 0 and a2 != 0) :
    temp_prob = 0
  if s1 == 0 :
    temp_prob = 0
  else :
    temp_prob = p/100 * ok(s1)*prob(bas(s1 - 1), s2, s3, bas(a1 -1), a2, bp(p-10)) + (100-p)/100 * prob(bas(s1 - 1), s2, s3, a1, a2, bp(p+10))
  p1list[s1, s2, s3, a1, a2, p] = temp_prob
  return p1list[s1, s2, s3, a1, a2, p]

def p2(s1, s2, s3, a1, a2, p):
  global p2list
  temp_prob = 0
  if p2list[s1, s2, s3, a1, a2, p] >= -0.5 :
    temp_prob = p2list[s1, s2, s3, a1, a2, p]
  elif a1 == 0 and a2 == 0 :
    temp_prob = 1
  elif (s1 == 0 and a1 != 0) or (s2 == 0 and a2 != 0) :
    temp_prob = 0
  if s2 == 0 :
    temp_prob = 0
  else :
    temp_prob = p/100 * ok(s2)*prob(s1, bas(s2 - 1), s3, a1, bas(a2 -1), bp(p-10)) + (100-p)/100 * ok(s2)*prob(s1, bas(s2 - 1), s3, a1, a2, bp(p+10))
  p2list[s1, s2, s3, a1, a2, p] = temp_prob
  return p2list[s1, s2, s3, a1, a2, p]

def p3(s1, s2, s3, a1, a2, p):
  global p3list
  temp_prob = 0
  if p3list[s1, s2, s3, a1, a2, p] >= -0.5 :
    temp_prob = p3list[s1, s2, s3, a1, a2, p]
  elif a1 == 0 and a2 == 0 :
    temp_prob = 1
  elif (s1 == 0 and a1 != 0) or (s2 == 0 and a2 != 0) :
    temp_prob = 0
  if s3 == 0 :
    temp_prob = 0
  else :
    temp_prob = p/100 * ok(s3)*prob(s1, s2, bas(s3 -1), a1, a2, bp(p-10)) + (100-p)/100 * ok(s3)*prob(s1, s2, bas(s3 -1), a1, a2, bp(p+10))
  p3list[s1, s2, s3, a1, a2, p] = temp_prob
  return p3list[s1, s2, s3, a1, a2, p]
      

def prob(s1, s2, s3, a1, a2, p) :
  global count
  count += 1
  global problist
  global p1list
  global p2list
  global p3list
  temp_prob = 0
  if problist[s1, s2, s3, a1, a2, p] >= -0.5 :
    temp_prob = problist[s1, s2, s3, a1, a2, p]
  elif (a1 == 0 and a2 == 0) :
    temp_prob = 1
  elif (s1 == 0 and a1 != 0) or (s2 == 0 and a2 != 0) :
    temp_prob = 0
  else :
    temp_prob = max(p1(s1, s2, s3, a1, a2, p), p2(s1, s2, s3, a1, a2, p), p3(s1, s2, s3, a1, a2, p))
  problist[s1, s2, s3, a1, a2, p] = temp_prob
  return temp_prob
  
def choice(s1, s2, s3, a1, a2, p) :
  global p1list
  global p2list
  global p3list
  first = p1(s1, s2, s3, a1, a2, p)
  second = p2(s1, s2, s3, a1, a2, p)
  third = p3(s1, s2, s3, a1, a2, p)
  print("현재 s1: " + str(s1) + ", s2: " + str(s2) + ", s3: " + str(s3) + ", a1: " + str(a1) + ", a2: " + str(a2) + ", p: " + str(p))
  print("p1: " + str(first))
  print("p2: " + str(second))
  print("p3: " + str(third))
  if s3 != 0 and third >= second and third >= first :
    print("3번")
    return 3
  elif s1 != 0 and first >= second :
    print("1번")
    return 1
  elif s2 != 0 :
    print("2번")
    return 2
  else :
    print("끝")
  return 0

c = 4

while c != 0 :
  c = choice(s1, s2, s3, a1, a2, p)
  k = 1
  while k != 0 :
    result = input()
    if result == "ㅇ" :
      p = bp(p -10)
      if c == 1:
        s1 = bas(s1 -1)
        a1 = bas(a1 -1)
      elif c == 2 : 
        s2 = bas(s2 -1)
        a2 = bas(a2 -1)
      elif c == 3 :
        s3 = bas(s3 -1)
      else :
        print(c)
      k = 0
    if result == "ㄴ" :
      p = bp(p + 10)
      if c == 1:
        s1 = bas(s1 -1)
      elif c == 2:
        s2 = bas(s2 -1)
      elif c == 3:
        s3 = bas(s3 -1)
      else :
        print(c)
      k=0
  if c == 0 :
    print("gogogo?")
    gogogo = input()
    if gogogo == "gogogo":
      c = 4      

      