#Qustion:    Python program to Check whether the String is Palindrome or not

print("For Performing Palindrome Operations")
n=input("Enter a string-:")
m=reversed(n)
if list(n)==list(m):
    print(n,"is a palindrome string")
else:
    print(n,"is not a palindrome string")
