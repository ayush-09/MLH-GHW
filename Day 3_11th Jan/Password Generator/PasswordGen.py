# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:33:57 2023

@author: ayush
"""
# Build Password Generator

import random

uppercase="QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase=uppercase.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_+{}|:[]-=;,.<>/?\\"

uper,lower,nums,sym = True,True,True,True

res=""

if uper:
    res+=uppercase
if lower:
    res+=lowercase
if nums:
    res+=digits
if sym:
    res+=symbols
    
length=10 # how long you want your password
amount=1  # how many passwords you want

for x in range(amount):
    password="".join(random.sample(res, length))
    print(password)
    
