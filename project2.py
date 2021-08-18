'''
AISC1000Python 01COURSE GROUPSS21
Ajay prudhvi Kalidasu - 500187692
Harpreet kaur Dounshi  -  500187865
Sai sourabh Cherukupally - 500194560
Vimala Ponnambalam  - 500188738
Yashaswini Tangirala  - 500192762

'''

import pyinputplus as pyip           # needed for validation
import datetime                     #Needed for date time calculations
import numpy as np                  # needed for calculation
from scipy.stats import pearsonr    #Needed for calculation correlation


#below function get energy bill values for 2020 and 2019 as lists
def get_det(year):
    e_bill=[]
    #months =['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    for i in range(12):
        print("Enter Enerygy bill for the year",year,"month-",months[i],':')
        x= pyip.inputNum(min=0,max=9999)
        e_bill.append(x)
    return(e_bill)



#Below function for getting X value, removing non digits, replacing with mean value
def get_eng():
    energy=[]

    for i in range(12):
        print("Natural Gas Spent for the Month",months[i],':')
        x=input()
        energy.append(x)
        #print(x)
    #return([int(item) if item.isdigit() else 0 for item in energy ])
    energy=[int(item) if item.isdigit() else 0 for item in energy]   #removing non numeric values
    return([x if x!=0 else sum(energy)/len(energy) for x in energy ])  # replacing with mean


#Below function for calculating savings details and printing avg,min, max savings
def cal(bill1,bill2):
    bill1=np.array(bill1)
    bill2=np.array(bill2)
    savings=np.subtract(bill1,bill2)
    print('\n')
    for i in range(len(savings)):
        print('savings in',months[i],year,'=',savings[i]) # creating savings list
    print('\nMax savings occured in ',months[np.where(savings==savings.max())[0][0]],year,':',max(savings)) # cal max
    print('Min savings occured in ',months[np.where(savings==savings.min())[0][0]],year,':',min(savings))   #cal min
    print('Avg savings 2019-2020:',sum(savings)/len(savings)) # cal avg
    #print(x)


#below function to get corr value between X and savings column
def rel(l1,l2):
    corr, _ = pearsonr(l1, l2) # calculate corr
    print('\nCorelation value between Savings and Natual Gas consumption(X):',round(corr,2))

#To write comments on corr
    if corr>0:
        if (corr<.15):
            return('There is no relationship between X and savings')
        elif (corr<=0.4 and corr >=0.15):
            return('X is in positive linear relationship with savings but weak')
        elif(corr<=0.6 and corr > .4):
            return('X is in positive linear relationship with savings but moderate')
        elif(corr >.6):
            print('X is in positive linear relationship with savings and strong')

    elif corr<0:
        if (corr>-.15):
            return('There is no relationship between X and savings')
        elif (corr>=-0.4 and corr <=-0.15):
            return('X is in negative linear relationship with savings but weak')
        elif(corr>=-0.6 and corr < -.4):
            return('X is in negative linear relationship with savings but moderate')
        elif(corr <-.6):
            return('X is in negative linear relationship with savings and strong')
    else:
        return('There is no relationship between X and savings')

#Main program below

months =['January','February','March','April','May','June','July','August','September','October','November','December']
#year= pyip.inputNum("Enter the year the rooftop gardens was implemented:",max=datetime.date.today().year)
year=2020
bill1=get_det(year) # get energy bill for 2020
bill2=get_det(year-1) # get energy bill for 2019
savings=list(np.subtract(bill1,bill2)) # creating savings list
x=get_eng() # get X column values
cal(bill1,bill2) # calculate max, min, avg savings
print(rel(savings,x)) # printing corr and notes


#formatted output and printing
min_sav=[str(min(savings)) if x==0 else ' ' for x in range(12)]
max_sav=[str(max(savings)) if x==0 else ' ' for x in range(12)]
avg_sav=[str(round(sum(savings)/len(savings),2)) if x==0 else ' ' for x in range(12)]
#print(min_sav,max_sav,avg_sav)
#print(months,bill1,bill2,savings,x)
print('\n\n')
print('Months   ','2019\t','2020\t','X   ','Saving ','Max.Saving  ','Min.Saving  ','Avg.Saving')
print('*'*7+' '+'*'*6+' '*3+'*'*4+' '*3+'*'*4+' '*3+'*'*4+' '*3+'*'*11+' '*3+'*'*11+' '+'*'*11)
counter =0
while counter < 12:
    print
    print ('%7s  %4d\t%2d\t%d\t%d\t%s\t\t%s\t  %s' %(months[counter],bill1[counter], bill2[counter], x[counter],savings[counter],max_sav[counter],min_sav[counter],avg_sav[counter])) 
    counter = counter + 1

    print 

