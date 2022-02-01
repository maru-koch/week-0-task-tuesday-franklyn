def is_prime(num):
    """
        - this function estimates a prime Number
        - in the context of this evaluation, one is considered to be an Invalid input
    """
    prime = [1, num]
    primeFactors = []

    if num >= 1:

        for index in range(1, num+1):

            if num % index == 0:

                primeFactors.append(index)

        if prime == primeFactors:

            return "\t{} is a prime number".format(num)

        else:
            
            return "\t{} is not a prime number.\n\t{}".format(num, primeFactors)
    else:
        return "{} is invalid. Please enter a positive integer greater than 1".format(num)

num = int(input("Enter a number: "))

for x in num:
    print(is_prime(x))

