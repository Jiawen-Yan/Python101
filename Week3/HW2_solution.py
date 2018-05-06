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
	fin = open(path, "r").read()
	step = 0 
	for l in fin.split("\n"):
		step = step + 1
		if step > 1: 
			if len(l.split(",")) ==7:
				# _date, _open, _high, _low, _close, _adj_close, vol = l.split(",")
				_date = l.split(",")[0]
				_adj_close = l.split(",")[5]
				Date.append(_date)
				AdjClose.append(float(_adj_close))

	return Date, Open, High, Low, Close, AdjClose, Vol


def plot_data(Date, y):
	import matplotlib.dates as mdates
	Date = mdates.num2date(mdates.datestr2num(Date))

	plt.plot(Date, y, label="AAPL")
	plt.xlabel("Date")
	plt.ylabel("Adjusted Price")
	plt.legend()
	plt.title("Apple Stock Price Chart")
	# plt.show()
	plt.savefig("AAPL.png", dpi=600)




if __name__=='__main__':
	path = "AAPL.csv"
	Date, Open, High, Low, Close, AdjClose, Vol = read_data(path)
	plot_data(Date, AdjClose)












