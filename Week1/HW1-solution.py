'''
Hello All
这里是HW1的三个问题的解答
思路应该不唯一，大家能看懂出来就OK

可以稍微改变一下里面的数字，多尝试一些组合，看看有没有Bug
Jiawen 
2018.4.10

'''


'''
question 1

'''

def find_max(a, b, c):
	_max = None # 用一个变量记录最大值
	if a > b: 
		if a > c: # 如果 a > b 而且 a > c, 那么a为最大者，以下同理
			_max = a
		else:	
			_max = c
	else:
		if b > c:
			_max = b
		else:
			_max = c
	return _max

print(find_max(0, 1, 3))




'''
question 2 

'''
def find_divider(a, b):
	bigger = a if a < b else b # 找出两个数的最小值，从高到低，枚举能否整除。
	for i in range(bigger, 0, -1):
		if a%i == 0 and b%i==0: # % 运算是除法取余数
			return i


print(find_divider(2, 25))



'''
question 3

'''
def my_file_operation():
	with open("sentences.txt", "r") as fin:
		for line in fin.read().split("\n")[:10]: # Note 写法不唯一
			print(line)

	with open("sentences.txt", "a") as fout:
		fout.write("Hello All\n")
		fout.write("Have you figure these question out?\n")
		fout.write("Watch less TV show and learn more Python!\n")
		fout.flush()










