#conditional statements questions
#..1.using if-else
#(i)
a=int(input("enter the value of a:"))
if a%2==0: 
    print("even")
else:
    print("odd")
#(ii)
n=int(input("enter the value of n:"))
m=int(input("enter the value of m:"))
if n>m:
    print(" n is greator than m")
else:
    print(" m is greator than n")
#(iii)
age=int(input("enter your age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible")
#..2.if-elif-else
#(i)
marks=int(input("enter your marks:"))
if 90>=marks>=100:
    print("grade A")
elif 80>=marks>=89:
    print("grade B")
elif 70>=marks>=79:
    print("grade C")
elif 60>=marks>=69:
    print("grade D")
else:
    print("you are faillllll ")


