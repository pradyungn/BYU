from database import Simpledb
book=open('phonebook.txt','a')
book.close()

print('Welcome to your Phone Book!')
file = Simpledb('phonebook.txt')
while True:
    status = 'whoa'
    while status!='a' and status!='f' and status!='d' and status!='u' and status!='q':
        status=input('Select one of the following actions:\n\'a\' for Adding a new contact\n\'f\' for searching for an existing contact\n\'d\' for Deleting an existing contact\n\'u\' for updating an existing contact\n\'q\' for Exiting the program')
    if status=='a':
        file.key=input('What is the person\'s name?')
        file.value=input('And their phone number?')
        file.insert()
        print('All done!')
        input('Press enter to continue:')
    elif status=='f':
        file.key=input('What is the person\'s name?')
        print('Here is their phone number:')
        print(file.select_one())
        input('Press enter to continue:')
    elif status=='d':
        file.key = input('What is this person\'s name?')
        file.delete()
        print('Consider it done!')
        input('Press enter to continue:')
    elif status=='u':
        file.key = input('What is this person\'s name?')
        file.value=input('What is this person\s new phone nubmer')
        file.update()
        print('Yippee-Ki-Yay, it\'s done!')
        input('Press enter to continue:')
    elif status=='q':
        break
print('Thank you for using this program')
print('Have a nice day!')
