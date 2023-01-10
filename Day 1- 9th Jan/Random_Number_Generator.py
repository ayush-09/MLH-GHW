# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:55:49 2023

@author: ayush
"""

# Random Number Generator

import random

number=random.random()
print(number)

num=random.randint(10, 50)   #Generate a random integer no. between the range (10,50)
print(num)

numb= random.randrange(10,30,2) #Genrate a random no. between the give range with gap of even interval i.e 2
print(numb)