import csv

myDict = {}

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)


def mainMenu():
    print(dataAsRows[askUserInput()])
    print(dataAsRows[askUserInput()])

def askUserInput():
    print("Please enter the index of the dataset you wish to compare (1-90): ")
    Index = int(input("Enter number : "))
    while True:
        if Index >= 1 and Index <= 90:
            return Index
        else:
            print("That was an invalid number, please re-enter (1-90): ")
            Index = int(input("Enter number : "))


if __name__ == '__main__':
    open('auto-mpg.csv')
    mainMenu()
