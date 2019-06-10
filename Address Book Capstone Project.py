#This program is designed to allow the user to enter and read addresses associated with
#people. The program will utilize a specific method o name storage to allow the user to input
#the address of a user and then read it back without issues.
#The list of addresses will be stored in a txt file so that the addresses are not lost when the program terminates.
#This program will be a prototype of what functions will be used within the program, but the actual read and write is not ready yet

'-------------------------------------------------------------------------------------------------------------------------------------'
print('A D D R E S S')
print('  B O O K   ')
addresses = {}
with open('Addresses.txt','w+') as txt:#This is where the txt file is opened and assigned to a variable
    for line in txt:
        (person, address, phone)=line.split('//+///+//')
        addresses[person]=[address,phone]
        
def read(): #This function allows the user to see what address belongs to a certain person that is already in the dictionary.
    global addresses
    name=''
    name = input('Whose address and phone number would you like? Input their name as the following: [Last Name],[First Name])')
    while name not in list(addresses.keys()):
        name = input('Sorry, That is not a valid name. Please try again.')
    print("The following person's address is "+addresses[name][1]+'.')
    print('Their phone number is '+addresses[name][0]+'.')
def enter():#This function allows the user to input new names and addresses
    global addresses
    name=input('What is this person\'s name? Please state their name in a [Last Name],[First Name] format to make future access easier.')
    number=input('What is their phone number?')
    address=input('What is their address?')
    addresses[name] = [address,number]
while True:#This is the actual program loop, to allow the user to read or input and infinite amount of addresses
    userstate=''
    userstate=input('Type 1 to enter an address and phone number, 2 to read an address and phone number, and 3 to end the program and save your current session.')
    while int(userstate)!=1 and int(userstate)!=2 and int(userstate)!=3:
        userstate=input('Please try again, that option is invalid')
    userstate=int(userstate)
    if userstate==1:
        enter()
    if userstate==2:
        read()
    if userstate==3:
        break
print('Thank you for using this program!')
print('DO NOT DELETE THE TXT FILE ASSOCIATED WITH THIS PROGRAM')
with open('Addresses.txt','w') as txt:#This code saves the dictionary to the txt file again
    for person in addresses:
        txt.write(person+'//+///+//'+addresses[person][0]+'//+///+//'+addresses[person][1])
