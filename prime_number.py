def is_prime(num):
    """
        - this function estimates a prime Number
    """
    prime = [1, num]
    primeFactors = []

    if type(num) == int and num >= 1:

        for index in range(1, num+1):

            if num % index == 0:
                
                primeFactors.append(index)

        if prime == primeFactors:

            return "{} is a prime number".format(num)

        else:
            
            return "\t{} is not a prime number.\n\t{}".format(num, primeFactors)
    else:
        return "{} is invalid. Please enter a positive integer greater than 1".format(num)

print(is_prime(8.0))

