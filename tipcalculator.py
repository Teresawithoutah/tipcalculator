# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

total_bill = float(input("Enter total bill: "))

guests = float(input("Enter number of guests: "))

tip = (15/100)*total_bill

#calculates final amount of bill with the tip included
final_bill = tip+total_bill


print ("\nFinal bill with tip: ", final_bill)

#splits the final bill amounts all the guests
split_tip= final_bill/guests


print ("\nSplit bill ", split_tip)

i = 1

#prints how much each guest will need to pay
while ( i <= guests):
    print ('Guest',i,'will have to pay:', split_tip)
    i = i + 1

