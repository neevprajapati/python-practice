#1....

# SIMPLE INTEREST CALCUATOR .....
#  interest = p r n /100    
x=float(input("enter p : "))
y=float(input("enter r : "))
z=float(input("enter n : "))
print("the net interest is ",(x*y*z)/100)

# 2...


x=int(input("enter a :"))
y=int(input("enter b :"))
print("before swapping",x)
print("before swapping",y)
temp=x
x=y
y=temp
print("after wapping",x)
print("after swapping",y)



# 3...
# celcius to fahrenheit converter
#    F =(C*9/5)+32)
x=int(input("enter for 1 celsius to fahrenheit\nenter 2 for fahrenheit to celsius"))
if ( x==1):
      c=float(input("assign the value of celsius :"))
      print("the value of fahrenheit is",(c*9/5)+32 )
elif( x==2):
    f=float(input("assign the value of fahrehite  :"))
    print("the value of celsius is",(f-32)*5/9)
else:
    print("none")


#  4....
# CONVERT TOTAL DAYS INTO YEARS , MONTHS AND DAYS 
d=int(input("enter days :"))
y=d//365
m=d%365//30
d=(d%365)%30
print(y,m,d)


# 5....

# BMI CALCULATOR
# BMI=WEIGHT(KG)/(HEIGHT^2)(M)
x=int(input("enter your weight : "))
y=int(input("enter your height : "))
print("your BMI is ",x/(y*y))



# 6....
#   GRADING SYSTEM .....

x=int(input("ENTER YOUR MARKS : "))
if(x>=90):
    print("you got A grade")
elif(x<90 and x>=80):
    print("you got B grade")
elif(x<80 and x>=70):
    print("you got C grade")
else:
    print("you got D grade")



# 7.....
#    CHECK A NUMBER IT IS ODD OR EVEN


x=int(input("ENTER A VALUE :"))
if(x%2==0):
    print("it is even number")
else:
    print("it is odd number")  



# 8....
# WAP TO FIND THE GREATEST OF 3 NUMBER ENTERED BY USER 
x=int(input("enter the value of a :"))
y=int(input("enter the value of b :"))
z=int(input("enter the value of c :"))

if(x>y and x>z):
    print(x," greatest")
elif(y>z):
    print(y," is greatest")
else:
    print(z,"is greatest")

# 9 ....
# WAP TO CHECK A NUMBER IF A NUMBER IS A MULTIPLE OF 7 OR NOT
x=int(input("ENTER A NUMBER = "))
if(x%7==0):
    print("it is multiple of  7")
else:
    print(" it is not multiple of 7 ")