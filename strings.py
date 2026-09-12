#      STRINGS ........
  
# 1... 

x="hello world"  # ( basic syntax)
print(x)

# 2...

y="hello world \n i am neev \n i am here so that i can practise  coding"        # ( \n )   MAKES SENTENCES IN EVERY NEW LINE....
print(y)


# 3...
x1 ="SUCCESS"
print(len(x1))            #   len ()  defines length of string .......

#4...

# ADDITION OF STATEMENTS......
 
l1="he is "
l2="fuckin"
l3="legendary"
final_str=l1+l2+l3
print(final_str)            # SIMPLY BY USING '+' WE CAN REARRANGE WORDS INTO STATEMENTS .....
print(len(final_str))


# 5...
 #   ALSO WE CAN USE "__"   FOR ADDING SPACE BETWEEN OBJECTS.....

l1="he is"
l2="the final"
l3="boss"
final_str1=(l1+" "+ l2 + " "+ l3)
print(final_str1)


#  6....
# STRING SLICING .......    # (ALWAYS USE """"SQUARE BRACKETS""""" WHEN WE DO   "SLICING" .........)
x2= "neev prajapati"        # POSITIVE SLICING          EG :-    neev  -->  1 2 3 4
print( x2[0])
print(x2[0:5])

##    NEEV PRAJAPATI     N -14;E-13;E-12;V-11...........P-4 A-3 T-2 I -1
print(x2[-1:-4])          # NEGATIVE SLICING          EG :-    neev --> -4 -3 -2 -1 
#        *** ALWAYS REMEMBER -VE SLICING MEIN " " OR "None" USE HOGA INSTEAD OF 0    
print(x2[-4:None])         




## *** STRING FUNCTIONS ****

## 1)    x.endswith(y)          BOOLEAN MEIN ANSWERE DEGA IT JUST CHECK GIVEN VALUE HAI KE NAHI IN STRING

x = "he is a legendary and great"
print(x.endswith("great"))
print(x.endswith("and great"))


# 2)   str.capitalize ()

x="i am neev and  wanna become a developer"
x=x.capitalize()
print(x)  
#  OR 
print(x.capitalize())

# 3)   str.replace()
x="he is on another stage "
print(x.replace("stage","level"))


# 4)    str.find("word")   
#    IT WILL TELL THE INDEX OF A GIVEN WORD
      
x="he is on another level, he is legendary u understand  legendary"
print(x.find("legendary"))


# 5)    str.count("word")
x=(" hi i am neev, for now i am studying in LJ university and  i wanna be developer in future")
print(x.count("wanna "))



