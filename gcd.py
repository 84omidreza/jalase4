def gcd(a,b):
    if b == 0:
        return   a

     else:
         return gcd(b,a%b)


print("gcd bayn 2 adad")
n1=int(input("pleas enter your first number:"))
n2=int(input("pleas enter your second number:"))


print(gcd(n1,n2))
