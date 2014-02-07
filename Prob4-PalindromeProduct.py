
def getLargestPalindromeProduct():
    num = 999999
    while num > 99999:
        print "num is: " + str(num)
        divisor = 999
        while divisor > 99:
            #print "divisor is: " + str(divisor)
            if num % divisor == 0:
                if len(str(num / divisor)) == 3:
                    print "divisor is: " + str(divisor)
                    print "multiple is: " + str(num/divisor)
                    return num
            divisor -= 1
        num = getNextPalindrome(num)
        
    return num

#Returns next palindrome with lesser value (assuming num has len 6)
def getNextPalindrome( num ):
    strNum = str(num)
    firstHalf = strNum[0:3]
    firstHalf = str(int(firstHalf) - 1)
    print firstHalf
    
    if not firstHalf[2] == 0:
        secondHalf = firstHalf[::-1]
        newNum = firstHalf + secondHalf
        return int(newNum)
    else:
        #990 --> 989
        firstHalf = int(firstHalf) - 1
        secondHalf = firstHalf[::-1]
        newNum = firstHalf + secondHalf
        return int(newNum)
    

#print getNextPalindrome( 990099 )

def isPalindrome( num ):
    strNum = str(num)
    for i in range(0, len(strNum)/2+1):
        if not strNum[i] == strNum[ len(strNum)-i-1 ]:
            return False

    return True


print getLargestPalindromeProduct()
