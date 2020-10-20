
class arithmatic:

	def __init__(self,value1,value2):
		self.v1=value1
		self.v2=value2
		self.res1=0

	def Addition(self,value1,value2):
		self.res1=value1+value2
		print(self.res1)
		
	def Subtraction(self,value1,value2):
		self.res1= value1-value2
		print(self.res1)
		
	def  Multiplication(self,value1,value2):
		self.res1= value1*value2
		print(self.res1)
	
 	def Division(self,value1,value2):
		self.res1=value1/value2
		print(self.res1)

def main():
	obj1=arithmatic(int(input("ennter no")),int(input("ennter no")));
	obj1.Addition(int(input("ennter no")),int(input("ennter no")));
	obj1.Subtraction(int(input("ennter no")),int(input("ennter no")));
	obj1.Multiplication(int(input("ennter no")),int(input("ennter no")));
	obj1.Division(int(input("ennter no")),int(input("ennter no")));

if __name__=="__main__":
	main();
