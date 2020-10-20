no1 = 1

def fun(no):
	
	for i in range(1,no+1):
		global no1
		no1 = no1 * i
		
		

def main():
	no = int(input("Enter the number"))	
	no2 = fun(no);
	print (no2)

if __name__ == "__main__":
	main();
