'''Create an empty list and call it ae1. Insert 5 integers followed by 3 strings. 
Use pop(), then remove() to delete two elements. Insert a new element using insert().
 Print the length of ae1. Extend ae1 to include two more strings. Append a list
  (called subList) to ae1. The subList contains 3 float numbers. Access subList in
   ae1 and print it out. Access the first element in the subList and print it out. 
   Randomly, select one element from ae1 and print it out. All prints must be informative 
   (e.g. include messages to explain what you print).'''

import random
ae1 = []  # create empty list
print(ae1)  #print the empty list.
ae1.append(1) #inserting 5 integers in the list.
ae1.append(2)
ae1.append(3)
ae1.append(4)
ae1.append(5)
ae1.append('a') #inserting the 3 strings in the list.
ae1.append('b')
ae1.append('c')
print(ae1)  #print the list after inserting integers and strings.
ae1.pop() # pop() is an inbuilt function.when no parameter is given it removes the the last element and returns it.
print(ae1) # prints the list after popping the value.
ae1.remove(2) #removes the given object from the list.
ae1.remove(3) #removes the given object from the list.
print(ae1) #prints the list after removing 2 from the list.
ae1.insert(4,9) #inserts the value in specified position.
print(ae1) #print the list after inserting 9 in the 4th position.
print("The length of the list is: ", len(ae1)) # print the length of the lsit
list = ('y', 'r')
ae1.extend(list)  #extending list with adding two more stings.
print(ae1)
subList = [76.7, 44.8, 23.6]
print("SubList= ", subList)
ae1.append(subList) #appending the sublist to the ae1
print("Adding sublist in ae1: ", ae1)
print("sublist in ae1: ", ae1[8])
print("First element of the sublist: ",ae1[8][0]) #Accessing the first element from the sublist.
print("Random value from the list: ",random.choice(ae1)) #printing random value from the list.


