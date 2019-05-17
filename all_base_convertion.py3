
######################################
#  - From Decimal to Binary, Octal   #
#	& Hexadecimal 					#
#  - From Octal & Binary to Decimal  #
######################################

print("*" * 34)
print("\n  1 => Decimal To Other Base")
print("  2 => Octal & Binary To Decimal\n")
print("*" * 34)

a = int(input("Enter 1 or 2 To Start Convertion :\n"))

if(a == 1):
	def convert(n, b):
		k = []
		i = 0
		while(n>0):
			k.insert(0, n%b)
			n = n//b
		for i in k:
			if(i == 10):
				i = "A"
			elif(i == 11):
				i = "B"
			elif(i == 12):
				i = "C"
			elif(i == 13):
				i = "D"
			elif(i == 14):
				i = "E"
			elif(i == 15):
				i = "F"
			print(i, end="")
		print(" ")
		

	T = int(input("Enter How May Bases You Want To Convert: "))
	for i in range(T):
		n = int(input("Enter Your Decimal Value: "))
		b = int(input("Enter Your Base Value You Want To Convert Into: "))
		convert(n, b)
		
elif(a == 2):
	def con(n, b):
		k = []
		i = 0
		c = n
		h = []
		while(n>0):
			k.insert(0, n%10)
			n = n//10
			d = len(k)-1
			j = 0		
		for i in k:
			if(i > b):
				print("error")
				break
			else:
				j += i*(b**d)
				d = d - 1
		print(j)
	
	T = int(input("Enter How May Bases You Want To Convert: "))
	for i in range (T):
		n = int(input("Enter Your Value To Convert: "))
		b = int(input("Enter The Base Number Of The Above Value: \n"))
		con(n,b)
else:
	print("Enter number correctly")
