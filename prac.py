# A= int(input("enter number"))
# if A % 2==0:
#     print("Number is even")
# else:
#     print("Number is odd")


num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")