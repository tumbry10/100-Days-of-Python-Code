# A dictionary is a collection wc is unordered, changeable, indexed and contain no duplicate members
# Dictionaries store data values like a map i.e key:value pair

# Creating a dictionary
person = {
    'first_name' : 'Nyasha',
    'last_name' : 'Tumba',
    'age' : 30
}
# first_name is the key, and Nyasha is the value
# Key-value pairs are separated by a comms (,), where as key-to-value is separated by a colon (:)

# Creating a dictionary using a constructor
person2 = dict(
    first_name = 'Nallen',
    last_name = 'Junior',
    age = 6
)

# Accessing elements of a dict
# You pass in the key, and it returns its value
print(person['first_name'])

# OR : Use the get method
print(person.get('last_name'))

# Adding key/value pair to the dict
person['phone'] = '0783270887'
print(person)

# Get dict keys
print(person.keys())

# To get dict items
print(person.items())

# To copy a dict
person3 = person2.copy()
person3['city'] = 'Masvingo'
print(person3, type(person3))

# Remove item from dict
del (person3['age'])
print(person3)

# OR Deleting using POP method
person3.pop('city')
print(person3)

# LIST OF DICTIONARIES

people = [
    {
        'first_name':'Nyasha', 
        'last_name':'Tumba',
        'age':30
    },
    {
        'first_name':'Nallen',
        'last_name':'Kunashe',
        'age':6
    },
    {
        'first_name':'Ryan',
        'last_name':'Zvikol',
        'age':7
    }
]

# To get the first_name of the person in the second dict
print(people[1]['first_name'])