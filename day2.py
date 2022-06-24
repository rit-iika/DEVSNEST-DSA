# input command 
x= input("your name: ")
print("hii "+ x +" !!")
# /t , /n - indentation
# input command, user can take inout during runtime, but in string form only. 

#  for integer
y=int(input()) 
# to take integer as input
# print(y)
# print("hey"+y)
print("hey"+str(y))

# MUTABILITY AND IMMUTABILITY -
# A DATA THAT CAN BE CHANGES IS MUTABLE, IF IT CANT BE CHANGES IT IS IMMUTABLE
# immutable datatypes- numbers, int, float bool, string
# mutable datatypes- list
# when i want to change immutable data i need to redeclare, but in mutable ones, no need to this
# when i do x=1, y=1, python refers both them to same address for efficient memory storage

# collection - is a bag of same data types
# example- list is a (mutable) collection of different kind of data types
# list behaves similar to Vectors in c++
# list is also ordered, like strings
# 
# 
# 
# 
# 

list1=[1,2, "hello", 00]
print(list1)
print(list1[2])
list1.append("gullyboy")
print(list1)
print(len(list1)) #list-size
# explore more functions of list in python

# if, else, elif
# z=int(input())
# if (z>10):
#     print("less than 10")
# elif (z>=5):
#     print("less than 5")
# else :
#     print("nothing beo")

# is keyword
a=int(input())
b=int(input())
if a==b:
    print("same")
print(x is y)

# DRY PRINCIPLE in coding - DONT REPEAT YOURSELF
# loops in python- while loop, for loop
# while condition: write somthing to false the condition, otherwise loop will run infinite times
k=5
while k>0:
    print(k)
    k-=1
# 
# 
# 
l=[1,2,3,4,5]
for x in l:
    print(x, id(x))
