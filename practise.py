# 1) ... WAP A USER'S FIRST NAME AND TYPE IT'S LENGTH 
x=input("ENTER YOUR NAME :")
print(len(x))

# 2).... WAP TO FIND OCCURANCE OF "$" IN A STRNG
x="M$dhon"
print(x.find("$"))

## 3) WAP TO ASK USER THREE FAV. MOVIE AND STORE THEM IN LIST


movie=[]
x1=input("ENTER YOUR FAV. MOVIE")
x2=input("ENTER YOUR FAV. MOVIE")
x3=input("ENTER YOUR FAV. MOVIE")
movie.append(x1)
movie.append(x2)
movie.append(x3)
print(movie)


### 4 ))
# WAP TO CHECK IF A LIST CONTAINES A PALIDROME  OF ELEMENT 


### WAP TO CHECK IF A LIST CONTAINES A PALIDROME  OF ELEMENT 
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
print(copy_list)
if(copy_list==list):
    print("it is palidrome")
else:
    print("it is not palidrome")


## 5)  
## wap to count the number of student getting A grade
x=["C","A","C","D","A","A","B"]

print(x.count("A"))


 ## SORT THAT LIST IN ASSENDING ORDER

x.sort()
print(x)

##3 IN DESENDING ORDER

x.sort(reverse=True)
print(x)