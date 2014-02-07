
#Returns boolean
def isPrime( n ):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    
    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True


#Return largest prime factor (single number)    
def findLargestPrimeFactor( n ):
    test_divisor = 2 
    largest_divisor = n
    num = n
    
    while not isPrime(num):
        if num % test_divisor == 0:
            largest_divisor = test_divisor
            num = num / test_divisor
            test_divisor = 2
        else:
            test_divisor += 1

    return num

#print findLargestPrimeFactor( 105 )

print findLargestPrimeFactor( 600851475143 )

    
    

