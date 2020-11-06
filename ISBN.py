def main():
    # Variables set for ISBN numbers
    LSBN13 = 0
    LSBN10 = 0
    print('This program will check and convert ISBN numbers \nPlease select one of the following options: \n'
          '1. Validate a 10 digit ISBN. \n2. Validate a 13 digit ISBN. \n3. Convert a 10 digit ISBN to a 13 digit ISBN.\n'
          '4. Convert a 13 digit ISBN to a 10 digit ISBN.')
    # 978-0131494985
    # 0131494988
    # Loads the screen function to display the menu
    screen(LSBN10, LSBN13)
    print("Would you like to choose another method?")
    restart = input("Please enter an option [Yes, No]: ")
    if restart == 'Yes':
        main()
    elif restart == "No":
        print("Goodbye!")
        exit()
    else:
        print("Incorrect entry please try again!")
        print("Goodbye!")
        exit()


# Function to display the user menu and load needed functions
def screen(LSBN10, LSBN13):
    selection = 0
    slection = userselection(selection)
    if slection == '1':
        # Strips and splits the ISBN number for parsing
        LSBN10 = userinput(LSBN10).strip().split()
        for t in LSBN10:
            # f literal used to return variables
            print(f"ISBN10 {t} validates {is_isbn10(t)}")
    elif slection == '2':
        # Strips and splits the ISBN number for parsing
        LSBN13 = userinput2(LSBN13).strip().split()
        for t in LSBN13:
            # f literal used to return variables
            print(f"ISBN13 {t} validates {is_isbn13(t)}")
    elif slection == '3':
        LSBN10 = userinput(LSBN10)
        convert10(LSBN10)
    elif slection == '4':
        LSBN13 = userinput2(LSBN13)
        convert13(LSBN13)
    elif slection == '0':
        print('Welcome to the hidden option!!!!')
        print('This code was created by an aspiring developer.\nThank you for trying it out.'
              '\nPlease feel free to offer suggestions!')
    else:
        print("Incorrect entry please try again!!!!")
        screen(LSBN10, LSBN13)


# Input for ISBN10 numbers
def userinput(LSBN10):
    LSBN10 = str(input("Enter a valid ISBN10: "))
    return LSBN10


# Input for ISBN13 numbers
def userinput2(LSBN13):
    LSBN13 = str(input("Enter a valid ISBN13: "))
    return LSBN13


# Input for user selection
def userselection(selection):
    selection = input("Please choose an option[1, 2, 3, or 4]: ")
    return selection


# Used to validate ISBN13
def is_isbn13(x):
    # remove uneeded characters
    x = x.replace('-', '').replace(' ', '')
    # If not 13 numbers automatic false
    if len(x) != 13:
        return False
    # Calculation formula used for ISBN13 numbers
    product = (sum(int(ch) for ch in x[::2])
               + sum(int(ch) * 3 for ch in x[1::2]))
    # If modulo = 0 valid and true
    return product % 10 == 0


# ISBN10 validation
def is_isbn10(x):
    # Remove uneeded characters
    x = x.replace('-', '').replace(' ', '')
    # If numbers are not 10 automatic false
    if len(x) != 10:
        return False
    # Forumla needed to calculate ISBN10
    product = sum((i + 1) * int(x) for i, x in enumerate(x))
    # if modulo = 0 true ISBN10
    return product % 11 == 0


# Converts a 10 to a 13
def convert10(LSBN10):
    # adds 978 and removes the check digit
    ISBN13 = '978' + LSBN10[:-1]
    # Set to a sting
    x = str(ISBN13)
    # Variable for check digit
    dig = checkI13(x)
    ISBN_NEW = str(ISBN13) + str(dig)
    print(LSBN10, " Is converted to: ", ISBN_NEW)


# Convert 13 to 10
def convert13(LSBN13):
    # Check for 978 and remove
    if LSBN13[:3] == '978':
        x = str(LSBN13[3:-1])
    else:
        raise Exception("ISBN can not be converted check format")
    # Load check digit function of ISBN10
    dig = checkI10(x)
    # ISBN10 created by combining ISBN without check digit to the check digit.
    ISBN_New = str(x) + str(dig)
    print("ISBN13: ", LSBN13, " is now ISBN10: ", ISBN_New)


# function to find check digit for ISBN10
def checkI10(x):
    ch = list(x)
    sum = 0
    d = 10
    for c in ch:
        sum += d * int(c)
        d -= 1
    check = 11 - (sum % 11)
    if check == 10:
        return "X"
    elif check == 11:
        return "0"
    else:
        return str(check)


# Function to find check digit for ISBN13
def checkI13(x):
    ch = list(x)
    sum = 0
    d = 0
    for c in ch:
        if (d % 2 == 0):
            sum += int(c)
        else:
            sum += 3 * int(c)
        d += 1
    check = 10 - (sum % 10)
    if check == 10:
        return "0"
    else:
        return str(check)


main()
