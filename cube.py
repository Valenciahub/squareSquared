def printSquares(outerLength, innerLength):
    line = []
    for yAxis in range(0, outerLength):

        for xAxis in range(0, outerLength):

            if (yAxis == 0 or yAxis == outerLength-1 or xAxis == 0 or xAxis == outerLength-1):

                line.append("* ")

            elif (xAxis == int((outerLength - innerLength)/2) and yAxis >= int((outerLength - innerLength)/2) and yAxis <= int((outerLength - innerLength)/2) + innerLength-1):

                line.append("* ")

            elif (yAxis == int((outerLength - innerLength)/2) and xAxis >= int((outerLength - innerLength)/2) and xAxis <= int((outerLength - innerLength)/2) + innerLength-1):

                line.append("* ")

            elif (xAxis == int((outerLength - innerLength)/2) + innerLength-1 and yAxis >= int((outerLength - innerLength)/2) and yAxis <= int((outerLength - innerLength)/2) + innerLength-1):

                line.append("* ")

            elif (yAxis == int((outerLength - innerLength)/2) + innerLength-1 and xAxis >= int((outerLength - innerLength)/2) and xAxis <= int((outerLength - innerLength)/2) + innerLength-1):

                line.append("* ")

            else:

                line.append("  ")

        squares = "".join(line)
        print(squares)
        line.clear()


outerLength = 7
innerLength = 4

printSquares(outerLength, innerLength)

