def get_ord():
    end ='n'
    print('1.Yum Yum Burger \t= .99\n2.Grease Yum Fries \t= .79\n3.Soda Yum \t\t= 1.09')
    print('Enter 1 for Burger\nEnter 2 for fries\nEnter 3 for Soda')
    total_burger=0
    total_fries=0
    total_soda=0
    cost=0
    
    while end=='n':
        
        option = int(input('Enter now---:'))
        if option ==1:
            total_burger+=int(input('Enter number of Burgers:'))
        elif option==2:
            total_fries+=int(input('Enter number of Fries:'))
        elif option==3:
            total_soda+=int(input('Enter number of Sodas:'))
        else:
            print('Invalid Entry! Try again')
        end=input('Do you want to end order? Enter y or n:')
    cost= round((total_burger*.99)+(total_fries*.79)+(total_soda*1.09),2)
    #tax=.06*cost
    total=round(cost*1.06,2)
    print('The total Price is $',total)
    #print (cost,total_burger,total_fries,total_soda)
    #return(cost,total_burger,total_fries,total_soda)
get_ord()