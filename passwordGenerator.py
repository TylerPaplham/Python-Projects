import secrets
import string
import re

print('╔╦═╦═══════════════╦╦╦══╦══════════╦╦═════╗')
print('║║ ╠═╦══╦══╦╦╦╦═╦═╦╝║║╔═╬═╦═╦═╦═╦═╦╣╠╦═╦═╗║')
print('║║╔╬╝╠╗╚╬╗╚╣║║║║║╠╣║║║╚╝║╩╣║║╩╣╠╬╝╠╗╔╣║║╠╝║')
print('║╚╝╚═╩══╩══╩══╩═╩╝╚═╝╚══╩═╩╩╩═╩╝╚═╝╚═╩═╩╝.║')
print('╚═════════════════════════════════════════╝')
print('By:Tyler Paplham')

def generatePassword(length):
    #Securely generates a password with lowercase, uppercase, number, and special character
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + '!' + '#' + '$' + '%' + '&' + '?' + '"') for i in range(length))
    
    #Check to see if the password has a lowercase, uppercase, number, and special character
    valid = re.search('^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&?"]).*$', password)

    #if regex passes then provide user their password. Else generate another password.
    if valid:
        print('\nYour password is:  ' + str(password))
    else:
        generatePassword(length)

def generateAnother():
    userInput = input('\nGenerate another? [y] yes [n] no:  ')

    if userInput == 'y':
        main()
    elif userInput == 'n':
        print('\n\nThank you for using Password Generator')
    else:
        print('unexpected input')

def main(): 
    print('\nHow long would you like the password?')
    try:
        length = int(input('length = '))
        if length < 8: 
            print('\nPassword must be >= 8 characters')
            main()
        else:
            generatePassword(length)
            generateAnother()
    except:
        print('\nPlease enter a number >= 8')
        main()
    
main()