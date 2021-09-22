import string
import random

def devide(num,div):
    return [num // div + (1 if x < num % div else 0)  for x in range (div)]

def randomString(size: int, *args, **kwargs):
    # Default returns only lowercase letters
    # Option: "upercase":           0 = no uppercase(default),   1 = random uppercase
    # Option: "numbers":            0 = no numbers(default),     1 = random numbers
    # Option: "symbol"(!@#$):       0 = no specials(default),    1 = random specials
    # Option: "diacritics"          0 = no diacritics(default),  1 = random diacritics # TODO
    # Option: "exclude"             Excludes all given karakters in the result.
    
    options = 0
    stringlist = []
    exclude = ""
    if "exclude" in kwargs:
        exclude = kwargs.get("exclude")
    if "lowercase" in args: 
        options += 1
        lowercase = string.ascii_lowercase
        for x in exclude:
            lowercase = lowercase.replace(x,"")
        stringlist.append(lowercase)
    if "uppercase" in args: 
        options += 1
        uppercase = string.ascii_uppercase
        for x in exclude:
            uppercase = uppercase.replace(x,"")
        stringlist.append(uppercase)
    if "digits" in args:
        options += 1
        digits = string.digits
        for x in exclude:
            digits = digits.replace(x,"")
        stringlist.append(digits)
    if "symbol" in args:
        options += 1
        symbol = string.punctuation
        for x in exclude:
            symbol = symbol.replace(x,"")
        stringlist.append(symbol)
    if "diacritics" in args:
        raise NotImplementedError

    # Error to much or no options
    if options == 0:
        raise Exception("No available options selected")
    if options > size:
        raise Exception("Size not sufficient with options.")
    
    devision = devide(size,options)
    part = 0
    characters = []
    for option in stringlist:
        characters.extend(random.choices(option,k=devision[part]))
        random.shuffle(characters)
        part += 1
    return "".join(map(str,characters))

if __name__ == '__main__':
    print(randomString(8, "lowercase", "uppercase","symbol",exclude="abcdefghi"))
