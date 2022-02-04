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

def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min), 2)
        normal_column.append(new_value)
    return normal_column




if __name__ == '__main__':
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,4):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(dataAsRows[i][j]))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))

    print(normalized_data)

    mainMenu()

