# A list is a collection wc is ordered, changeable & allows duplicate numbers.

#To create a list: 
numbers = [1, 2, 3, 4, 5]

#We can alos create a list using a constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers, numbers2)

# A List of strings
names = ['Nyasha', 'Nallen', 'Jnr', 'Kunashe', 'Tumbry', 'Ten']

# To get a value from the list we pass its index position. Python also allows for negative indexing
print(names[0])  #will return the first element in the list, i.e 'Nyasha'
print(names[-2]) # will return the second from last element i.e 'Tumbry'

# To select and return a range of values in a list
'''
    We pass in 2 indexies, the start and the end index
    NB: The end index is the index of the last element is the range u want + 1,
    eg Lets say we want a range from 'Nallen' to 'Tumbry' from the names list above.
    The start index will be 1 & the end index will be 4+1=5
'''
print(names[1:5])

# To Append to the end of the list
names.append('Ryan')

# To remove an item from the list
names.remove('Nallen')  #Will remove Nallen from the list

# To insert an item into a specific position in a list
names.insert(2, 'Zviko') # We pass in the index position (2) wc we are inserting the item to and the item name

# Remove py pop
names.pop(2) #We pass in the index position of the item being removed 

#Reverse the List
names.reverse()

# To sort the list alphabetically
names.sort()

# Reverse Sort
names.sort(reverse=True)

# To change the item in a list
names[1] = 'Nick' #We pass in the index position of the item to be changed and the new value to be saved
print(names)