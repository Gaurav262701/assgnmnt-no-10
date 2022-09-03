#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer no 1
#progrram to find sum of elements in list
total = 0
list = [11,12,13,14,15]
for i in range(0,len(list)):
    total = total + list[i]
    
print("sum of all elements is given list:",total)


# In[3]:


#answer no 2
#Python program to Multiply all numbers in the list
def multiplyList(mylist):
    result = 1
    for i in mylist:
        result = result * i
    return result
list1 = [1,2,3]
list2 = [4,5,6]
print(multiplyList(list1))
print(multiplyList(list2))


# In[4]:


#Answer no 3 
#Write a Python program to find smallest number in a list
list = [10,20,30,5]
list.sort()
print("smallest element is:",list[:1])


# In[8]:


#Answer no 4
#Write a Python program to find smallest number in a list
list = [10,20,30]
print(max(list))


# In[9]:


#Answer no 5
#Write a Python program to find second largest number in a list
list = [10,20,30,40]
mx = max(list[0],list[1])
secondmax = min(list[0],list[1])
n = len(list)
for i in range(2,n):
    if list[i] > mx:
        secondmax = mx
        mx = list[i]
        
    elif list[i] > secondmax and mx != list[i]:
        secondmax = list[i]
        
    elif mx == secondmax and secondmax != list[i]:
        secondmax = list[i]
        
print("second highest number is :",str(secondmax))


# In[10]:


#Answer no 6
#Write a Python program to find N largest elements from a list
def Nmaxelements(list1 , N):
    final_list = []
    for i in range(0,N):
        max1 = 0
        
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
                
        list1.remove(max1)
        final_list.append(max1)
        
    print(final_list)
    
list1 = [2,4,51,62,73,10,9,8]
N=2

Nmaxelements(list1,N)


# In[11]:


#Answer no 7
#Write a Python program to print even numbers in a list
list = [10,21,4,45,66,93]
for num in list:
    if num % 2 == 0:
        print(num,end=" ")


# In[12]:


#Answer no 8
#Write a Python program to print odd numbers in a List
list = [10,21,4,45,66,93]
for num in list:
    if num % 2 != 0:
        print(num,end=" ")


# In[14]:


#Answer no 9
#Write a Python program to Remove empty List from List
t_List = [5,6,[],3,[],9]
print("The original list is:" + str(t_List))
result = [ele for ele in t_List if ele != []]
print("list after empty list removal:"+ str(result))


# In[16]:


#Answer no 10
#Write a Python program to Cloning or Copying a list
def cloning(lis):
    li_copy = lis[:]
    return li_copy
lis = [4,8,2,10,15,18]
lis1 = cloning(lis)
print("original list:",lis)
print("after cloning:",lis1)


# In[18]:


#Answer no 11
#Write a Python program to Count occurrences of an element in a list
def countX(lst,x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count

lst = [2,3,4,5,6,7,8,8,9,10]
x = 8
print('{} has occurred {} times'.format(x,countX(lst,x)))


# In[ ]:




