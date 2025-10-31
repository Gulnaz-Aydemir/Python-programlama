# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 01:33:29 2025

@author: gulna
"""

#end="\n" demektir. ama kendin tanımlamak istersen şöyle yaparsın fonksiyonu print fonk içinde olan bir parametredir. bu nedenle
print("python", end=" ") 
print("eğitimi")
#çıktı:python eğitimi

#sep= " "
print("gülnaz", "aydemir")
#çıktı:gülnaz aydemir
#ben yeni bir sep değeri tanımlarsam artık onu kullanır. örneğin:
print("gülnaz", "aydemir", sep="-")
#çıktı:gülnaz-aydemir
print("gülnaz", "aydemir", sep=" ")
#çıktı:gülnaz aydemir

print(7,5,2024, sep="/")
print("01","01",2025, sep="/")
#çıktılar:7/5/2024
#01/01/2025


print(*"TC", sep=".")
#yıldız * karakterleri tek tek ayır demektir.
#çıktı:T.C
