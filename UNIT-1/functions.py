'''
#defining a function
def square(value):
    result = value * value
    return result

answer = square(10)
print(answer)

print(square(50))

#function with multiple arguements
def greetings(name, job, hobby):
    print('Hello {} your job is {} and you like {} hobby'. format(name, job, hobby))
    greetings('shad', 'student', 'biking')
'''
'''
my_list = ["tom", "john", "bianca", "draymond", "victor", "shad"]
print(len(my_list))

list_emp =[]

for names in my_list:
    print len(my_list[-1, 0]) 
'''
def reverse_list(my_list):
    new_list = []
    #iterate over a list in reverse order
    for index in range(len(my_list)-1, -1, -1):
        #add each element to a new list
            new_list.append(my_list[index])
    #return the reverse list
    return new_list

numbers = [1,2,3,4,5,6,7,8,9,10]

fruits = ["apple", "orange", "banana", "kiwi"]
result = reverse_list(numbers)

print(result)

print(reverse_list(fruits))

#print reverse _list
def reverse_string(my_string):
    reverse_string = ' '
    for i in range(len(my_string) - 1, - 1, -1):
        reverse_string += my_string[i]
    return reverse_string

def  is_parlindrome(word):
    #check if word is same forward and backwards
    word_reversed = reverse_string(word)
    if word_reversed == word:
        return True
    return False

print(is_parlindrome("bob"))


#checking if a word is a parlindrome

# print true is word is a parlindrome

# print false is word is a parlindrome

