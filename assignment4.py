import copy
#Q.1- Reverse the whole list using list methods.
l=[1,2,3,4,5,6]
print("list is:",l)
l.reverse()
print("reversed list is",l)


#Q.2- Print all the uppercase letters from a string.
s=input("enter the string in which you want to check uppercase letters")
def upper_characters(s):
    ans=""
    for x in s:
        if(x.isupper()==True):
            ans +=x
    return ans
c=upper_characters(s)

print("the entered string was :",s)
print("it contains these uppercase letters",c)



#QUESTION: 3  Split and Store the Values After TypeCasting
l=input()#enter no 45,46,47  
a=l.split(',')
l2=[]
for x in a:
    b=int(x)
    l2.append(b)
print(l2)


#Q.4- Check whether a string is palindromic or not.
a=input("enter any string or number to be checked as pailnfrom ")
b=len(a)
flag=0
i=0
while(i!=b):
    if(a[i]!=a[b-i-1]):
        flag=1
        break
    else:
         flag=0
    i=i+1
if(flag):
    print("not a pailndrom")
else:
    print("pailndrom")

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
    # Python code to demonstrate copy operations
l1= [1, 2, [3,5], 4] 
l2= copy.deepcopy(l1)
print(l1)
l2[2][0] = 7
print(l2)
# Change is NOT reflected in original list l1
# as it is a deep copy
print(l1)

#diff between deep and shallow copy:
#1. In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
#  In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
#2.In python, this is implemented using “deepcopy()” function.
#   In python, this is implemented using “copy()” function.
#3.*******************************************************
#l1= [1, 2, [3,5], 4]
#l2= copy.deepcopy(l1)
#print(l1)
#l2[2][0] = 7
#print(l2)
# Change is NOT reflected in original list l1 # as it is a deep copy
#print(l1)
#output:
#1 2 [3, 5] 4
#1 2 [7, 5] 4
#1 2 [3, 5] 4
#**********************************
#li1 = [1, 2, [3,5], 4]/////eg of shallow cpy
#li2 = copy.copy(li1)
#print(li1)
#li2[2][0] = 7
#print(li1)
#output
#1 2 [3, 5] 4
#1 2 [7, 5] 4


