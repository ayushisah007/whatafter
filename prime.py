num=int(input("Enter the number: "))
flag = False
if num > 1:
    for i in range(2, int(num/2+1)):
        if(num % i) == 0:
            flag = True
            break
if flag:
    print("The number entered is not a prime number")
else:
    print("The number entered is a prime numbers")