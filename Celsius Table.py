start = 1
end = 100
increment = 5

def main():   
    #create table headers
    print('The following table shows conversion of Celsius to Farenheit')
    print( 'between 1 and 100 degrees Celsius in increments of 5.')
    print('')
    print('Celsius\t   Farenheit')
    print('____________________')
    #convert celsius input to farenheit using loop
    for Celsius in range (start, end, increment):
        Farenheit = (9 / 5) * Celsius + 32
        print(Celsius, '\t', format(Farenheit, '.1f'))
main()
