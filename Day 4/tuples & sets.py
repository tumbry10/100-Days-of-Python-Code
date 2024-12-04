# A tuple is a ordered collection wc is immutable i.e Tuples are unchangeable after creation
# Just like lists, tuples allow duplicate members

# Creating A Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#Tuples can alos be created using a constructor
#Note: tuples use () while lists uses {}, 
# NB: If a tuple has only one element, u need to leave a trailing comma so that python wont treat it as a string

fruit = ('Mango')     # This is a str
fruit2 = ('Mango',)   # This is a tuple

# Delete a tuple
del fruit2

'''         SETS        '''
#A set is a collection wc is unordered, unindexed and has no duplicate members
# A set is iterable and mutable
# Sets uses {} just like lists

# Create A Set
fruit_set = {'Apples', 'Mango', 'Oranges'}

# Accesing elements in a set. 
'''
    Since elements in a set are unindexed, they cannot be accessed using Index numbers
    You can either check if an element is in the set or iterate/loop thru the items in the set
'''
# To check if an element is in the set
print('Apples' in fruit_set)        # It returns a boolean True/False

# To loop thru the elements of a set
for i in fruit_set:
    print(i, end=" ")

# Add items into a set
fruit_set.add('Grapes')

#Remove Items from a set
fruit_set.remove('Mango')


# To clear/Empty set
fruit_set.clear()

# To delete the entire set
del fruit_set

#NB : In sets, if you try to add a duplicate element, u wont get error message, but it wont add a duplicate.
names = {'Nyasha', 'Nallen', 'Kunashe', 'Tumbry'}
names.add('Nallen')
print(names)