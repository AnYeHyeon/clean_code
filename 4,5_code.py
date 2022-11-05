# -*- coding: utf-8 -*-
""" 클린 코드 4, 5장 Code
"""

if character not in ".,!?"

if item_under_repair.has_key('tires'):
    is_vehicle = True

print('Good morning!')
print('How are you feeling?') 
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input() 
print('I am happy to hear that you are feeling'+ feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling'+ feeling + '.')

def askFeeling():
    print('How are you feeling?')
    feeling = input() 
    print('I am happy to hear that you are feeling' + feeling + '.')
    
print('Good morning!')
askFeeling() 
print('Good afternoon!')
askFeeling() 
print('Good evening!')
askFeeling()

for timeOfDay in ['morning', 'afternoon', 'evening']: 
    print('Good' + timeOfDay+'!')
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling' + feeling + '.')

#여러 시간 값에 대한 상수 설정
from time import time

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
SECONDS_PER_WEEK = 7 * SECONDS_PER_DAY

expiration = time() + SECONDS_PER_WEEK #1주 뒤에 만료
expiration

expiration = time() + 604800  #1주 뒤에 만료
expiration

while True:
    print('set solar panel direction:')
    direction = input().lower() 
    if direction in ('north', 'south', 'east', 'west'): 
        break

print('solar panel heading set to:', direction) 
if direction == 'nrth':
    print('Warning: Facing north is inefficient for this panel.')

#각 방향에 대한 상수 설정

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

while True:
    print('Set solar panel direction:')
    direction = input().lower()
    if direction in (NORTH, SOUTH, EAST, WEST): 
        break

print('Solar panel heading set to:', direction)
if direction == NRTH:
    print('Warning: Facing north is inefficient for this panel.')

import random

def coinFlip():
    if random.randint(0, 1): 
        return 'Heads!'
    else:
        return 'Tails!' 
    return 'The coin landed on its edge!'
print(coinFlip())

def exampleFunction():
    pass

def exampleFunction():
    raise NotImplementedError

exampleFunction()

import logging

logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s') 
logging.debug('This is a log message.')

import logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

spam = []
for number in range(100): 
    if number % 5 != 0:
        spam.append(str(number))
spam

spam = [str(number) for number in range(100) if number % 5 != 0]
spam

nestedIntList = [[0, 1, 2, 3], [4], [5,6], [7, 8, 9]] 
nestedStrList = [[str(i) for i in sublist] for sublist in nestedIntList]
nestedStrList

nestedIntList = [[0, 1, 2, 3], [4], [5,6], [7, 8, 9]]
nestedStrList = []

for sublist in nestedIntList:
    nestedStrList.append([str(i) for i in sublist])
nestedStrList

try:
    num = input('Enter a number: ') 
    num = int(num)
except ValueError:
    pass

try:
    num = input('Enter a number: ')
    num = int(num) 
except ValueError:
    print('An incorrect value was passed to int()')

# 아래 줄 코드에 대한 주석부는 여기에 넣는다
someCode()

# 이 부분은 여러 개의 단일 행 주석을
# 기호를 이용해 연속으로 배치해 여러 행에 길게 걸치게 만든 블록 주석이다
#
# 이런 형태를 블록 주석이라 부른다

if someCondition:
    # 또 다른 코드에 대한 주석부는 여기에 넣는다
    someOtherCode()  # 이 형태는 인라인 주석이다

this.