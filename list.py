#    LIST IN PYTHON......
x=["neev","tarang","harshil","mitul","yug"]
print(x)
print(x[0])
print(x[0:3])
print(len(x))


# LIST ARE MUTABLE

y=["dog","cat","bear","python"]
print(y[0])
y[0]="wistel"
print(y)

# LIST SLICING.......
x=["apple","banana","orange","kiwi","stawberry","pinnaple"]
print(x[0])
print(x[1:4])
print(x[0:])
print(x[-1:-3])   ## NEGATIVE SLICING   ## ALWAYS LEFT TO RIGHT ALWAYS
print(x[-3:None])
print(x[-4:0])     ### --->> THIS WILL NOT VALID SO WE ALWAYS HAVE TO RIGHT None instead og 0
print(x[-4:None])


##   LIST METHODS.....
# 1)    APPEND METHOD

list=[1,2,3,4,5,6]
list.append(45)
print(list)

list=["neev","cat","seven","dad"]
list.append("can")
print(list)

'''
list=["neev","cat","seven","dad"]
list.append("can","do")                 # THIS IS NOT POSSIBLE    2 OR MORE  STRING OR VALUES CAN'T ASSIGN IN APEND FUNCTION
print(list)
'''

# 2))   SORT

x=[1,3,2,4,2,5,6,8,5,23]
x.sort()
print(x)

x=['d','c','b','a','A','B']    #    THE STRINGS CAN ALSO AAIGN IN ORDER THROUGH ASCII VALUES........
x.sort()
print(x)

X=['neev','logarithum','frustation','google','chess']
X.sort()
print(X)


### DESENDING ORDER OF SORTATION................

x=[1,3,2,4,2,5,6,8,5,23]
x.sort(reverse=True)      
print(x)

### REVERSE LISTING
x=[1,2,3,4,5]
x.reverse()
print(x)


############ (most forgettable method)---->   3)))  insert()
'''
HOW INSERT METHOD WORKS?
SO   BASICALLY,
                    insert(index,element)'''
x=[1,23,4,5,6,6]
x.insert(2,55)
print(x)
x=["neev","jayesh","bhavesh","mahesh","narsesh"]
x.insert(1,"satvi")
print(x)



### 4))   REMOVE METHOD......
'''    SYNTAX  OF REMOVE(ELEMENT IN THE LIST)'''
x=[1,3,5,6,8,34,21]
x.remove(3)
print(x)


###   5)    pop method
x=[1,2,3,4,5]
x.pop(2)
print(x)




###  TUPLE METHOD......###
''' IT IS IMMUTABLE JUST AS STRING'''


#### STRING SLICING...
x=(1,2,3,4,5,6)
print(x[0])
print(x[0:2])
print(x[2:3])
print(x[1:4])    #### it has the same slicing syntax as LIST.....



#### define 1 elent in TUPLE    and define 1 elememt in list
x=(1,)
print(type(x))
x=[1]
print(type(x))


### TUPLE METHOD

# 1)     ELEMENT--> INDEX

x=(1,2,4,3,56)
print(x.index(56))


# 2) COUNT METHOD....(it count how many repeateted times does the element is repeated)
x=(1,2,3,4,5,6,7,8,9,10)
print(x.count(6))
x=(1,1,1,2,2,3,3,33,3,3,3,3,3,4,5,6,7,8,9,9,9,9,9,10)
print(x.count(3))
print(x.count(9))