import random
def passwordGeneretor():

    lowerchars = ['a','b','c','d','e']
    upperchars = ['A','B','C','D','E']

    spaeicalchars=['@','#','%','*','&']

    numericchars= ['1','2','3','4','5']

    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)

    password = password + password + password + password


    return password