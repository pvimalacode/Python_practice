def prime(n):
    j=0
    for i in range(2,n):
        if (n%i==0):
            j+=1
            #print(n,'is not a prime number')
            #break
        else:
            continue
    if j==0:
        print(n,'is a prime number')
    else:
        print(n,'is not a prime number\n it has',j+2,'factors')




option ='y'
print('Prime Number Checker')
while option=='y':
    n=int(input("Please enter an integer between 1 and 5000:"))
    if n<=5000 and n!=1:
        prime(n)
    else:
        print('Invalid Interger.Please try again')
        #n=int(input("Please enter an integer between 1 and 5000:")) 
    option = input('Try again? (y/n):')
print('Bye!')