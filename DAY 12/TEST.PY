# Modify the line below (String remains as is)
name = input('What is your name? ')

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below (Convert to integer)
age = int(input('What is your age? '))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below (Convert to float)
height = float(input('What is your height in meters? '))

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below (Convert to boolean: Assume 'yes' means True, anything else is False)
loyalty = input('Are you part of our loyalty program? (yes/no) ').strip().lower() == 'yes'

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
n