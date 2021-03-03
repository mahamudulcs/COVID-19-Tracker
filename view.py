import csv
from controller import Controller


class View():
	def __init__(self):
		self.data_controller = Controller()
		print("Initalizing data ...........")
		

		while(True):
			option = self.print_prompt()
			if option == 1:
				self.reload_data()
				print("********* data reloaded ********* ") 
			elif option == 2:
				self.data_controller.persist_data_to_comma_separated_file()
				print("********* data saved into assignment2.csv ********* ") 
			elif option == 3:
				self.select_and_display()
				print("********* data displayed above ********* ")
			elif option == 4:
				print("********* data added ********* ")
			elif option == 5:
				index = int(input("please enter the row you would like to change:"))
				column_name = input("which column which you like to change: (e.g. pruid, prname, prnameFR, date, numconf, numprof, numdeath):")
				column_attribute = input("please set the value:")

				self.data_controller.set_data(index,column_name,column_attribute)
				print("********* data set ********* ")
			elif option == 6:
				row_number = int(input("please select the Nth row that you would like to delete:"))
				self.data_controller.select_and_delete_data(row_number)
				print("********* data deleted ********* ")


		

	def reload_data(self):
		self.data_controller = Controller()
		self.print_prompt()

	def save_to_csv(self):
		self.data_controller.persist_data_to_comma_separated_file()	


	def select_and_display(self):
		row_numbers = int(input("please select how many data that you would like to display:"))
		search_list = []

		for i in range(row_numbers):
			search_list.append(int(input("which row do you want to search:")))
		results = self.data_controller.select_and_display_data(search_list)
		print("the results is :" + str(results))
		for item in results: 
			print(item)


 
	def select_and_delete(self):
		row_number = int(input("please select the Nth row that you would like to delete:"))
		self.data_controller.select_and_delete_data(row_number)	

	def print_prompt(self):
		print(''' 
****************************************************************************************
Name: Mahamudul Islam
please select one of the following options(for example:1):
1 Reload the data from the dataset, replacing the in-memory data.
2 Persist the data from memory to the disk as a comma-separated file, writing to a new file.
3 Select and display either one record, or display multiple records from the in-memory data.
4 Create a new record and store it in the simple data structure in memory
5 Select and edit a record held in the simple data structure in memory
6 Select and delete a record from the simple data structure in memory
****************************************************************************************
		''')
		option = input("Please enter your option:")
		return int(option)




if __name__ == "__main__":
	view = View()
