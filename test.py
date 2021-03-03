import unittest 



def postive_or_negative(number):
	""" this to assert that the number inside a list contains no negative values 
	"""
	for i in number:
		if i < 0:
			return False
	return True


class test_postive(unittest.TestCase):
	def test_positive_or_negative(self):
		""" it provides the assertTrue to evaluate a function that contains all positive values 
		will raise an exception with failed case, pass otherwise 
		"""
		self.assertTrue(postive_or_negative([1,2,3,4,5,1,1]))

	

if __name__=='__main__':
	unittest.main()