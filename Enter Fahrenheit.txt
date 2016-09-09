def main():
	
	keep_going = 'y'
	while keep_going == 'y':
		
		Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
		Celsius = (Fahrenheit - 32) * 5.0/9.0
		print ("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " Celsius")
		keep_going = input ("Do you want to enter another temperature in Fahrenheit?")

main()
