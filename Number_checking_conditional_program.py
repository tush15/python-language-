def ChkNum(no):
	if (no > 0):
		print ("Positive  Number")

	if (no < 0):
		print ("Negative  Number")

	if (no == 0):
		print ("zero ")

def main():
	ChkNum(11);
	ChkNum(-8);
	ChkNum(0);

if __name__ == "__main__":
	main();
