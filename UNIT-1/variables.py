def main():
    first_name = 'Shad'
    last_name = 'Uadiale'

    full_name = first_name + ' ' + last_name

    print(full_name)

    #boolean variable (True or False values only)
    has_child = True

    #null/none variable
    cars = None 

if __name__ == '__main__':
    main()

def conditionals():
    #given a range of grades 0-100
    #if grade is between 80 and 100 - print 'A'
    #if  grade is between 60 - 79 - print 'B'
    #if grade is between 50 - 59 - print 'C'
    #0 - 40 - print 'F'

    val =79
    if val >= 80 
        print('A')
    elif val >=60 
        print('B')
    else print('C')


    val = 50
    if val > 35
        print('HIGH')
    elif val > 15:
        print('MEDIUM')
    else:
        print('LOW')


def.fizzbuzz():

    '''
     for the number 1 to 50
    print 'fizz' if the number is a mutiple of 3
    print 'buzz' if the number is a multiple of 5
    print 'fizzbuzz' if the umber is a multiple of 15
    otherwise print the number
    '''

    for num in range(1, 51):
        if num % 3 == 0
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0:
                print('fizz')
        else:
            print (num)
if __name__ == '__main__':
    fizzbuzz()

