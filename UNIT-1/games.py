#ask user to guess secret number

#loop as long as users input is not equal to secret no

#print message if it is equal and end  loop

secret = 9
guess = int(input("guess my secret number: "))
while guess != secret:
    print("not correct")
    guess = int(input("guess my secret number: "))
print("yeah you got it")


# extend this game --- 
# if the guess is  +-2 - print "almost there"
#if guess is greater or less than secret by 2 -- print "too far"
