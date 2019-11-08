

a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]
b = a[:]  # even better way to copy a list
print (a)
print(b)

