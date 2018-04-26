# coding=utf8

'''
HW2
goal:
	1. learn to read data from csv file
	2. learn to plot data using matplotlib

try to finish functions below and 
I will buy you dissert (Miaowu) if you are top 3 finishers
'''
 

import matplotlib.pyplot as plt 

def read_data(path):
	Date = []
	Open = []
	High = []
	Low = []
	Close = []
	AdjClose = []
	Vol = []
	###################################
	### you need to write your code here
	################################### 
	raise NotImplementedError

	return Date, Open, High, Low, Close, AdjClose, Vol


def plot_data(Date, y):
	import matplotlib.dates as mdates
	Date = mdates.datestr2num(Date)

	###################################
	### you need to write your code here 
	###################################
	
	raise NotImplementedError
	


if __name__=='__main__':
	path = "AAPL.csv"

	Date, Open, High, Low, Close, AdjClose, Vol = read_data(path)

	plot_data(Date, AdjClose)












