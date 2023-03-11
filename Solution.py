inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

testCase = int(inputFile.readline())

for i in range(testCase):
    house = int(inputFile.readline())
    totalWalls = 0

    for j in range(house):
        houseData = inputFile.readline().split(',')
        totalWalls += int(houseData[1]) * 3 + \
            int(houseData[2]) * 4 + int(houseData[3]) * 6

    accentQuantity = totalWalls * 0.5
    regularQuantity = totalWalls * 1.5
    totalHours = totalWalls * 3

    outputFile.write(
        f"Case#{i+1}: {totalHours}, {accentQuantity}, {regularQuantity}\n")
