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

num=int(input("enter the number:"))
orignal=num
reverse=0

while num >0:
    digit = num%10
    reverse= reverse*10+digit
    num= num//10
if orignal == reverse:
   print("Palindrome")
else:
    print("Not palindrome")

