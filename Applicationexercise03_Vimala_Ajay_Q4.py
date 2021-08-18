
players= {'Elizabeth':{'wins':41,'Losses':3,'Ties':22},'Joel':{'wins':32,'Losses':10,'Ties':12},'Abby':{'wins':2,'Losses':8,'Ties':10}}

def display():
    test=[]
    print('Game Stats Program\nALL PLAYERS:')
    for n in players:
        test.append(n)
    test=sorted(test)
    print(*test,sep='\n')


def get_details():
    name=input('Enter a player name: ')
    for n,k in players.items():
        #print(len(k))
        if name in players:
            #print(type(k))
            if n==name:
                for sts,v in k.items():
                    print(sts,'\t:',v)
        else:
            print('There is no player named',name)
            break




temp='y'
display()
while temp!='n':
    
    get_details()
    temp=input('Continue? (y/n): ')