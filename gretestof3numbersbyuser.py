a = int(input("enter first numbers: "))
b = int(input("enter second numbers: "))
c = int(input("enter third numbers: "))

if(a>=b and a>=c):
    print("frist number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third is largest",c)