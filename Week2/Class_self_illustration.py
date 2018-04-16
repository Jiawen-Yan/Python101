# illustration of self - class-wide variable

class MyClass:

	def myadd(self, a,b):
		self.a = a
		self.b = b
		return a+b

	def mysub(self):
		return self.a-self.b

myclass = MyClass()
print(myclass.myadd(4,5))
print(myclass.mysub())