import string
def randomString(size: int, **kwargs):
    # Default returns only lowercase letters
    # Option: "upercase":           0 = no uppercase(default),   1 = random uppercase
    # Option: "numbers":            0 = no numbers(default),     1 = random numbers
    # Option: "symbol"(!@#$):       0 = no specials(default),    1 = random specials
    # Option: "diacritics"          0 = no diacritics(default),  1 = random diacritics # TODO
    # Option: "exclude"             Excludes all given karakters in the result.
    
    options = 0 # Default lowercasess
    lowercase, upercase,numbers,symbol,diacritics, exclude = "","","","","",""



    if "lowercase" in kwargs: 
        options += 1
        lowercase = string.ascii_lowercase
        for x in exclude:
            lowercase.replace(x,"")        
    if "upercase" in kwargs: 
        options += 1
        upercase = string.ascii_uppercase
        for x in exclude:
            upercase.replace(x,"")
    if "numbers" in kwargs:
        options += 1
        numbers = string.digits
        for x in exclude:
            numbers.replace(x,"")
    if "specials" in kwargs:
        options += 1
        symbol = string.punctuation
        for x in exclude:
            symbol.replace(x,"")
    # if "diacritics" in kwargs:
    #     options += 1

    # Error for no or to much options
    if options == 0:
        raise Exception("No available options selected")
    if options > size:
        raise Exception("Size not sufficient with options.")

    

    return output


if __name__ == '__main__':
    print(randomString(8))
