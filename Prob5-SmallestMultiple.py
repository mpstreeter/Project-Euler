
def smallestMultiple1to20():
    num = 2000
    while num > 0:
        #print "num: " + str(num)

        isDivisByAll = True
        for i in range(2, 21):
            #print "i " + str(i)
            if not num % i == 0:
                isDivisByAll = False
                break
        if isDivisByAll:
            return num
        
        num += 10

    return num


print smallestMultiple1to20()
