import pandas as pd 
import numpy as np





class Data:
	
	
	def __init__(self,pruid,prname,prnameFR,date,numconf,numprob,numdeaths,numtotal):
		
		self.pruid = pruid  
		self.prname = prname
		self.prnameFR = prnameFR
		self.date = date
		self.numconf = numconf
		self.numprob = numprob
		self.numdeaths = numdeaths
		self.numtotal = numtotal

	def get_pruid(self):
		return self.pruid
	def set_pruid(self,pruid):
		self.pruid = pruid

	def get_prname(self):
		return self.prname
	def set_prname(self,prname):
		self.prname = prname

	def get_prnameFR(self):
		return self.prnameFR
	def set_prnameFR(self,prnameFR):
		self.prnameFR = prnameFR

	def get_date(self):
		return self.date
	def set_date(self,date):
		self.date = date

	def get_numconf(self):
		return self.numconf
	def set_numconf(self,numconf):
		self.numconf = numconf

	def get_numprob(self):
		return self.numprob
	def set_numprob(self,numprob):
		self.numprob = numprob

	def get_numdeaths(self):
		return self.numdeaths
	def set_numdeaths(self,numdeaths):
		self.numdeaths = numdeaths

	def get_numtotal(self):
		return self.numtotal
	def set_numtotal(self,numtotal):
		self.numtotal = numtotal

	def __repr__(self):
		return repr(str(self.pruid) + "|*|*|" + self.prname + "|*|*|" + self.prnameFR + "|*|*|" + self.date + "|*|*|" + str(self.numconf) + "|*|*|" + str(self.numprob) + "|*|*|" + str(self.numdeaths) + "|*|*|" + str(self.numtotal))



def main():
	df = pd.read_csv('covid19-download.csv')
	data_set = set()
	FULLNAME = "**********************************************\nMahamudul Islam\n**********************************************\n"
	for index,each_row in df.iterrows():
		
		data_set.add(Data(each_row['pruid'],each_row['prname'],each_row['prnameFR'],each_row['date'],each_row['numconf'],each_row['numprob'],each_row['numdeaths'],each_row['numtotal']))

	for i in data_set:
			print(FULLNAME)
			print(i)


if __name__ == "__main__":
	main()

