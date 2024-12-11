# To print to the console we use the print() function
print('Hello World')

#To print multiple values - Strings with Nos separated by a comma
print('The result is:', 45) # Note it auto add a blank space between a strring and numbers

# Custom Separators (sep)
# The sep argument allows u 2 customize what separate multiple values.
print('apples', 'oranges', 'mango')
print('apples', 'orange', 'mango', sep='; ')

# Custom end xters (end)
''' By default, the print() end with a newline (\n)
    You can change this by using the end parameter'''
print('Hello', end=' ')
print('World')

# Escape Xters -  We can use the escape xters inside strings to format the output
''' Common escape xters are :
        Newline (\n)
        Tab (\t)
        Backslash(\)'''
