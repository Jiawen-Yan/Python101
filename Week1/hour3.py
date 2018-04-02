##################
# Topic: File Operations
# Author: Charles Yan
# Date: 03/30/2018
# Verison: 1.0
##################

# 1. if you want to write to a file
file_input = open("test.txt", "w")
file_input.write("Today is good and Python is great!")
file_input.flush()
file_input.close()

# 2. if you want to append writing to a file
file_input = open("test.txt", "a")
file_input.write("Today is good and Python is great!")
file_input.flush()
file_input.close()

# 3. if you want to read a file 

file_input = open("test.txt","r").read()
file_input = open("test.txt","r").readlines()
file_input = open("test.txt","r").readline()

# 4. THE standard way of loading a file
'''
Why it is the standard: 
	(1) "fin" exists within the "with" scope, and will be automatically closed;
	(2) for file loop read a line each time, do not need to load whole file into memory; 
	(3) which avoids potential memory overflow problem; 
'''
with open("test.txt","r") as fin: 
	for l in fin: 
		print(l)



