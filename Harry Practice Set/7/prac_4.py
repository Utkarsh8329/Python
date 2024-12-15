while True:
    ques = input("You want to check a number prime or not Yes/No: ").lower()
    if(ques == "no" or ques != ("yes" and "no")):
        break

    n = int(input("Enter a number to check whether it is prime or not: "))
    prime = True
    for i in range(2,n):
        if(n % i ==0):
            prime = False
            break
        
    if prime:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")