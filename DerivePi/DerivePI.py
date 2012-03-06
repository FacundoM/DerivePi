class derivePi():
    n = 1
    pi = 0
    operator = 1
    float(pi)
    while n < 1000:
        estimate = 4.0 /((2.0 * (n-1.0)) + 1.0)
        if (operator == 1):
            pi = pi + estimate
            operator = 2
        else:
            pi = pi - estimate
            operator = 1
        n+= 1
        print pi
               


    
    







