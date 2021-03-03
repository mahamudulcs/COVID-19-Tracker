import csv

class RecordClass:
	
	def __init__(self,id,pruid,prname,prnameFR,date,numconf,numprob,numdeaths,numtotal,numtoday,ratetotal):
		self.__id = id
		self.__pruid = pruid  
		self.__prname = prname
		self.__prnameFR = prnameFR
		self.__date = date
		self.__numconf = numconf
		self.__numprob = numprob
		self.__numdeaths = numdeaths
		self.__numtotal = numtotal
		self.__numtoday = numtoday
		self.__ratetotal = ratetotal
	
	def get_id(self):
		return self.__id
	def set_id(self,id):
		self.__id = id
	def get_pruid(self):
		return self.__pruid
	def set_pruid(self,pruid):
		self.__pruid = pruid

	def get_prname(self):
		return self.__prname
	def set_prname(self,prname):
		self.__prname = prname

	def get_prnameFR(self):
		return self.__prnameFR
	def set_prnameFR(self,prnameFR):
		self.__prnameFR = prnameFR

	def get_date(self):
		return self.__date
	def set_date(self,date):
		self.__date = date

	def get_numconf(self):
		return self.__numconf
	def set_numconf(self,numconf):
		self.__numconf = numconf

	def get_numprob(self):
		return self.__numprob
	def set_numprob(self,numprob):
		self.__numprob = numprob

	def get_numdeaths(self):
		return self.__numdeaths
	def set_numdeaths(self,numdeaths):
		self.__numdeaths = numdeaths

	def get_numtotal(self):
		return self.__numtotal
	def set_numtotal(self,numtotal):
		self.__numtotal = numtotal

	def get_numtoday(self):
		return self.__numtoday
	def set_numtoday(self,numtoday):
		self.__numtoday = numtoday

	def get_ratetotal(self):
		return self.__ratetotal
	def set_ratetotal(self,ratetotal):
		self.__ratetotal = ratetotal

	@property
	def message(self):
	


		return str(self.__id) + '|' +self.__pruid + "|" + self.__prname + "|" + self.__prnameFR + "|" + self.__date + "|" + self.__numconf + "|" + self.__numprob


	def __str__(self):
	


		return str(self.__id) + '|' +self.__pruid + "|" + self.__prname + "|" + self.__prnameFR + "|" + self.__date + "|" + self.__numconf + "|" + self.__numprob


