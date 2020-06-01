# Modular programming
# JRDay
# 07.02.2020

def positive_float(prompt):
    ''' Get a positive float
    from user'''
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                break
            else:
                print ("Non-negative number only!")
        except ValueError:
            print ('Must be numeric!')
    return number

def positive_int(prompt):
    ''' Get a positive integer
    from user'''
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                break
            else:
                print ("Non-negative number only!")
        except ValueError:
            print ('Must be numeric!')
    return number

def any_float(prompt):
    ''' Get any float number
    from user'''
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print ('Must be numeric!')
    return number


def alpha_string(prompt):
    ''' Get an alphabetical string
    from user '''
    while True:
        string = input(prompt)
        remove_spaces = string.replace(" ", "")
        if len(string) > 0 and remove_spaces.isalpha():
            break
        else:
            print("Letters only please...")
    return string

def any_string(prompt):
    while True:
        string = input(prompt)
        if len(string) > 2:
            break
        else:
            print('Not a valid input')
    return string

def yes_no(prompt):
    ''' Get yes or no answer'''
    while True:
        q = input(prompt)
        q = q.lower()
        if q == 'y' or q == 'yes':
            answer = 'y'
            break
        elif q == 'n' or q == 'no':
            answer = 'n'
            break
        else:
            print ('Not a valid answer')
    return answer

def get_letter(prompt):
    '''Get a single letter from user'''
    while True:
        l = input(prompt)
        l = l.upper()
        if len(l) == 1:
            break
        else:
            print ('Invalid entry')
    return l