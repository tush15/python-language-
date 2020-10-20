class Demo:
	value=0

	def __init__(self,no1,no2):
		self.no1=int(input("no1 is"))
		self.no2=int(input("no2 is"))

	def fun(self):
		print(self.no1)

	def gun(self):
		print(self.no2)
	
	

def main():
	obj1=Demo(11,21)
	print(obj1.no1)
	print(obj1.no2)

	obj2=Demo(51,101)
	print(obj2.no1)
	print(obj2.no2)
	
	obj1.fun();
	obj2.fun();
	obj1.gun();
	obj2.gun();


if __name__=="__main__":
	main();

