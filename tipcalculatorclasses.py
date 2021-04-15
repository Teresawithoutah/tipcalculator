def calculation(total_bill,guests):  
    tip = (15/100)*total_bill
    #calculates final amount of bill with the tip included
    bill_with_tip = tip+total_bill
    
    return bill_with_tip


def split_bill(total_bill,guests):
 
  
    final_bill = calculation(total_bill,guests)
    split_tip= final_bill/guests
    
    print("\nSplit bill ", split_tip)
    
    i = 1

    #prints how much each guest will need to pay
    while ( i <= guests):
        print ('Guest',i,'will have to pay:', split_tip)
        i = i + 1


def main(): 
    
    total_bill = float(input("Enter total bill: "))
    guests = float(input("Enter number of guests: "))

    split_bill(total_bill,guests)
        
    
if __name__ == '__main__':
    main()
 