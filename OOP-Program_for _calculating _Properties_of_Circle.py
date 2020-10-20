
class circle:
	pi=3.14;

	def __init__(self,r,a,c):
		global pi
		pi=3.14+0
		self.value=r
		self.area=a
		self.circumference=c

	def CalculateArea(self,r):
		global pi
		pi=3.14+0
		self.area=self.area+pi*r*r;
		print(self.area)
		
	def CalculateCircumference(self,r):
		global pi
		self.circumference=self.circumference+pi*(2*r);
		print(self.circumference)
		
	def  Display(self):
		print("radious is",self.value);
		print ("aera is",self.area);
		print("circumference is",self.circumference);
	
def main():
	obj1=circle(5,0,0);
	obj1.CalculateArea(5);
	obj1.CalculateCircumference(5);
	obj1.Display();

if __name__=="__main__":
	main();
