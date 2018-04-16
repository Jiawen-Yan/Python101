# Class, group of functions 
class MyClass:

	def myadd(self, a,b):
		self.a = a
		self.b = b
		return a+b

	def mysub(self, a,b):

		return a-b

	def find_max(self, a,b):
		if a>b:
			return "a is bigger"
		elif a == b:
			return "a is equal to b"
		else:
			return "b is bigger"

myclass = MyClass()
print("Please input a number")
a = input()
print("Please input another number")
b = input()
a = int(a) 
b = int(b)
c = myclass.mysub(a,b)
print("a-b=", c)

# Import Syntax 
a = [1,1,2,3,4,9]
# import statistics 
# import statistics as st 
from statistics import mean, median
try:
	# print(mean(a))
	# print(median(a))
	# print(mode(a))
	print(a[6])
except Exception as name:
	print(name)
finally:
	print("Finished")
'''


a = """
def myadd(self, a,b): 
	return a+b
myadd(3,4)
"""

print(type(a))
a = eval(a)
print(type(a))




ctrl + n  new file


































