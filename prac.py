# Even or Odd

# A= int(input("enter number"))
# if A % 2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

#  Prime number

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")



# Palindrome number

# num=int(input("enter the number:"))
# orignal=num
# reverse=0

# while num >0:
#     digit = num%10
#     reverse= reverse*10+digit
#     num= num//10
# if orignal == reverse:
#    print("Palindrome")
# else:
#     print("Not palindrome")


#Amstrong number

# num=int(input("enter the number:"))

# orignal= num
# power= len(str(num))

# total=0

# while num>0:
#     digit= num%10
#     total += digit**power
#     num//=10
# if total == orignal:
#     print("Amstrong Number")
# else:
#     print("Not an amstrong")


# Factorial number

# num=int(input("enter a number:"))
# fact=1
# if num<0:
#     print("Factorial not define")
# else:
#     for i in range(1, num+1):
#         fact= fact*i
#     print("Factorial", fact)

#fibonaxi series

# n = int(input("enter number of terms:"))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")

#     a, b = b ,a + b

#Resverse number

# num = int(input("Enter the number:"))

# reverse = 0

# while num>0:
#     digit=num%10
#     reverse = reverse *10 + digit
#     num = num//10
# print("reverse",reverse) 

#Add number

num=int(input("enter the number:"))

total =0
while num>0:
    digit=num%10
    total+=digit
    num =num//10
print("sum:",total)