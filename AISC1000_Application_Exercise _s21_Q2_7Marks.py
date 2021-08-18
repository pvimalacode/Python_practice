'''

******Q.2  [7 marks]*****
Write program that will take in the number of call minutes used. Your program will calculate the amount of charge for the first 250 minutes with a rate of $0.35;
 the remaining minutes with a rate of $0.55. The tax amount is calculated as 11% on top of the total. The customer could have a credit that also has to be considered 
 in the calculation process. Finally, the program displays all these information. Below is a sample run:


Customer account number:			12345
Minutes used:					(you provide)
Charge for the first 250 minutes@ 0.35:		(you provide)
Charge for the remaining minutes@ 0.55:	(you provide)	
Taxes:						(you provide)
Credits:						(you provide)
Total bill:					(you provide)
*************************************
'''

#*****Code starts here*********

import pyinputplus as pyip

#Enter Details
mins=pyip.inputNum('Enter Minutes used \t\t\t:',min=0)
cardnum= pyip.inputNum('Enter Card Number\t\t\t:',max=9999999999999999,min=100000000000)
acc_credit= pyip.inputNum('Enter Credit available\t\t\t:')


#calculation
if mins==0:
    free=0
    #print(free)
else:
    free=250*0.35


if mins >250:
    rem=(mins-250)*0.55
else:
    rem=0

tax=(free+rem)*0.11
total=free+rem+tax
bill=round(abs(acc_credit-total),3)


#printing deatils
print('\n\nCustomer account number\t\t\t:',cardnum)
print('Minutes used\t\t\t\t:',mins)
print('Charge for the first 250 minutes@ 0.35\t:',free)
print('Charge for the remaining minutes@ 0.55\t:',rem)
print('Tax\t\t\t\t\t:',tax)
if acc_credit>total:
    print("\nPaid using credits\n\navailable credit\t\t\t:",bill)
    print("Total\t\t\t\t\t:0")
else:
    print("Total\t\t\t\t\t:",bill)










