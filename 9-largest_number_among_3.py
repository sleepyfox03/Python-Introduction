from ast import Or


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter last number: "))

if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c: 
    print(b) 
elif c>a:
    print(c)  
    
    
    
    # or
    
    
a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c= int(input("Enter the third number: "))


largest_number = a


if b > largest_number:
    largest_number = b


if  c> largest_number:
    largest_number = c  
    

print("The largest number is:", largest_number)




# or    By using built-in functions


a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c= int(input("Enter the third number: "))

LARGEST=max(a,b,c)
print(LARGEST)