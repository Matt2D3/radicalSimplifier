import math
def simp(num,mult):
    print(num)
    numberToBeFactored = num
    multiplier = mult
    lowRange = 0
    highRange = numberToBeFactored
    finalAnswer = "could not find a solution"
    initialIsSquare = False
    foundAnswer = False
    square = math.sqrt(numberToBeFactored)
    if int(square + 0.5)**2 == int(numberToBeFactored):
        finalAnswer = ("answer is "+str(square * multiplier))
        initialIsSquare = True 
    while(lowRange<=highRange and not initialIsSquare):
      if lowRange == 0:
            lowRange = lowRange+1
      currentFactor = numberToBeFactored/lowRange
      if(currentFactor.is_integer()):
        print("the factors are "+str(lowRange)+" and "+str(currentFactor))
        square = math.sqrt(currentFactor)
        if int(square + 0.5)**2 == int(currentFactor) :
            print("square root found: "+str(square))
            print("answer is " + str(square*multiplier) + "-/"+str(lowRange) )
            if not (square == 1) and not foundAnswer:
                finalAnswer = ("answer is " + str(square*multiplier) + "-/"+str(lowRange) )
                foundAnswer = True
      lowRange=lowRange+1
    print("________________________")
    print("")
    print(finalAnswer)
    print("________________________")
    return(finalAnswer)