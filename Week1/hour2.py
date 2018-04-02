
def my_add(x, y):
	return x+y

def my_product(x, y):
	return x*y

def my_default(x = 4, y = 5):
	return x+y 

ret = my_add(4, 5)
print(ret)

ret = my_add("My name is ", "Charles")
print(ret)

ret = my_product(4, "Charles")
print(ret)

print(my_default())
print(my_default(y=2))
print(my_default(2, 3))
print(my_default(x = 2, y = 3))



