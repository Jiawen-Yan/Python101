# 昨天Demo时的两个问题

# 1. 在一个list 后面增加
a = [1,2,3,4,5]
a.append(100) # 注意，这里不是 a = a.append(100), list append 函数返回值为None,  
print(a) # 输出结果是 [1,2,3,4,5,100]
b = a.append(1) # b 为 None
print(b)

# 2. Eval 貌似只能对 Variable 进行 Evaluate, Exec 可以对函数进行分析和执行

print(eval("[1,2,3,]"))

exec("""
def my_add(a,b):
    return a+b
print(my_add(5,10))
""") # 输出结果15 
