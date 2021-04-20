#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:36:54 2021

@author: teresawithoutah
"""

def calculation(total_bill,guests):  
    tip = float(0.15/100)*float(total_bill)
    #calculates final amount of bill with the tip included
    bill_with_tip = tip+total_bill
    
    return bill_with_tip 


def split_bill(total_bill,guests):
 
  
    final_bill = calculation(total_bill,guests)
    split_tip= final_bill/guests
    
   # print("\nSplit bill ", split_tip)
    
    i = 1

    #prints how much each guest will need to pay
    while ( i <= guests):
        print ('\nGuest',i,'will have to pay:', split_tip)
        i = i + 1


    
def process_input(total_bill,guests):      
    try:
        total_bill = float(total_bill)
    except ValueError:
        print ("Wrong entry for total bill")
        return
    
    try:
        guests = int(guests)
    except ValueError:
        print ("Wrong entry for guests")
        return

    split1 = split_bill(total_bill,guests)
    print(split1)
    
        
 # if can divide without remainder
    if total_bill % guests ==0: 
        print("dividable")
        return True
       
    else:
        print("not dividable")
        return False   
    
def main(): 
    
    total_bill = input("Enter total bill: ")
    guests = input("Enter number of guests: ")
    
    process_input(total_bill,guests)
    



  
        
if __name__ == '__main__':
    main()
 