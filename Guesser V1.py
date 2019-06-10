import random
actualnumber=random.randint(1, 100)
guesses=6
while guesses!=0:
    number=input('Choose a Number between 1 and 100')
    if int(number)==actualnumber:
        break
    else:
        print('That is the wrong number!')
    guesses=guesses-1
    print('You have '+str(guesses)+' guesses left.')
if int(number)==actualnumber:
    print('You got it right!')
elif int(number)!=actualnumber:
    print('Sorry, but my number was '+str(actualnumber)+'.')
    

