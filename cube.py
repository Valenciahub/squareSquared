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

# func square(_ a: Int) -> Void{
#    let num = a - 1
#
#  var shape = [""]
# for i in 0 ... num{
#    shape.insert("*", at: i)

#   }
#   var i = 0; while i <= a{
#      i += 1
#     for i in 0...a-2{
#        if shape[i].count <= a-2{
#           if (i > 0 && i < num){
#              shape[i].append(" ")
#         }
#    }
#    }
# }
# for i in 1 ... num{
#    shape[0].append(contentsOf: "*")
#   shape[num].append(contentsOf: "*")
#  if (i > 0 && i < num){
#                shape[i].append("*")
# }
# }
# for i in  0 ... num{
#   print(shape[i])
# }
#    print(shape)
# }


# def betterPattern(a ,b):
#	square = []
#	for i in range()
