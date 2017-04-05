def primenumbers(n):
    primes = []
    for num in range(0,n):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if (prime and num!=0 and num!=1):
            primes.append(num)
     return primes
