import csv
from model import RecordClass

from datetime import datetime



class Controller():
	def __init__(self):
		self.covid_list = []
		with open('covid19-download.csv', newline='') as csvfile:
			covid_data_lines = csv.DictReader(csvfile)
			
			for index, row in enumerate(covid_data_lines):
				each_object = RecordClass(index,row['pruid'],row['prname'],row['prnameFR'],row['date'],row['numconf'],row['numprob'],
			row['numdeaths'],row['numtotal'],row['numtoday'],row['ratetotal'])
				self.covid_list.append(each_object)
				if index == 101:
					break
	
	def print_rows(self):
		for item in self.covid_list:
			print(item)

	def persist_data_to_comma_separated_file(self):
		with open('assignment2.csv','w',newline='') as covid_file:
			covid_file.truncate()
			covid_writter = csv.writer(covid_file,delimiter=',')
			covid_writter.writerow(["pruid","prname","prnameFR","date","numconf","numprob","numdeaths","numtotal","numtoday","ratetotal"])


			for each_row in self.covid_list:
				covid_writter.writerow([each_row.get_pruid(), each_row.get_prname(),each_row.get_prnameFR(),each_row.get_date(),
					each_row.get_numconf(),each_row.get_numprob(),each_row.get_numdeaths(),each_row.get_numtotal(),each_row.get_numtoday(),
					each_row.get_ratetotal()])
			covid_file.close()



	def create_data(self,data_dict):
		length_of_list = len(self.covid_list) + 1 

		self.covid_list.append(RecordClass(length_of_list,data_dict['pruid'],data_dict['prname'],data_dict['prnameFR'],
			data_dict['date'],data_dict['numconf'],data_dict['numprob'],data_dict['numdeaths'],data_dict['numtotal'],
			data_dict['numtoday'],data_dict['ratetotal']))
	
	def set_data(self,index,column_name,column_attribute):
		for item in self.covid_list:
			if index == item.get_id():
				if column_name == 'pruid':
					item.set_pruid(column_attribute)
				elif column_name == 'prname':
					item.set_prname(column_attribute)
				elif column_name == 'prnameFR':
					item.set_prnameFR(column_attribute)
				elif column_name == 'date':
					item.set_date(column_attribute)
				elif column_name == 'numconf':
					item.set_numconf(column_attribute)
				elif column_name == 'numprob':
					item.set_numprob(column_attribute)
				elif column_name == 'numdeaths':
					item.set_numdeaths(column_attribute)
				elif column_name == 'numtotal':
					item.set_numtotal(column_attribute)
				elif column_name == 'numtoday':
					item.set_numtoday(column_attribute)
				elif column_name == 'ratetotal':
					item.set_ratetotal(column_attribute)
				print(item)


	def select_and_display_data(self,search_list):
		result_list = []
		print("the search_list is " + str(search_list))
		for item in self.covid_list:

			for index_item in search_list:
				if item.get_id() == index_item:
					result_list.append(item)
		return result_list

	def select_and_delete_data(self,row_number):
		for item in self.covid_list:
			if item.get_id == row_number:
				self.covid_list.remove(item)
