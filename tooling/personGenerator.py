import random

# Data FIles
DATASIVILNUMBERS = r"data\BurgerServiceNummers.txt"
FEMALEFIRSTNAMES = r"data\female-first-names.txt"
MALEFIRSTNAMES = r"data\male-first-names.txt"
LASTNAMES = r"data\last-names.txt"

class generatePerson:
    def __init__(self):
        self.seed = None   
        self.firstName = None
        self.lastName = None
        self.birtday = None
        self.civilServiceNumber = None
        self.gender = None

    def generate(self):
        if self.seed == None:
            self.seed = random.randint(1000, 9999)
        random.seed(self.seed)
        if self.gender == None:
            self.gender = random.choice(["male","female"])
        
        fileSivilNumbers = open(DATASIVILNUMBERS)
        self.civilServiceNumber = random.choice(fileSivilNumbers.readlines())
        
        if self.gender == "male":
            fileFirstNames = open(MALEFIRSTNAMES)
        elif self.gender == "female":
            fileFirstNames = open(FEMALEFIRSTNAMES)
        self.firstName = random.choice(fileFirstNames.readlines())

        fileLastNames = open(LASTNAMES)
        self.lastName = random.choice(fileLastNames.readlines())

if __name__ == '__main__':
    testPerson = generatePerson()
    testPerson.seed = 1222
    testPerson.generate()
    print(testPerson.lastName)
