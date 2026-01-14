if __name__=="__main__":
 print("Script is running directly")

#Exercise 1: Create a module that has a class called "exercises". Let this class have 9 functions called "ex1,ex2,...,ex9."Put all your exercises of Day 1 into those functions. Then in a main script run them all.
class Exercises:
 def __init__(self,ex1,ex2,ex3,ex4,ex5):
  self.ex1= ex1
  self.ex2= ex2
  self.ex3= ex3
  self.ex4= ex4
  self.ex5= ex5

 def ex1(a,b,c):
  if a==0:
   print('I cant divide by zero')
  else:
   #Discriminant:
   discr=(b**2)-(4*a*c)
   #Print message in case of no solutions:
   if discr<0:
    print('There are no real solutions') 
   #Calculate the solutions:
   else:
    d=(-b+(discr)**0.5)/(2*a)
    e=(-b-(discr)**0.5)/(2*a)
    return d, e

 def ex2(n):
  #Recaman sequence function:
  an=[0]*n
  for i in range(n):
   if i==0:
    an[i]=0
   else:
    a=an[i-1]-i
    if a>0 and a not in an:
     an[i]=an[i-1]-i
    else:
     an[i]=an[i-1]+i
  return an

 def ex3():
  mylist=[1,-99,89,0,234,77,-748,11]
  #Printing mylist sorted in descending order without modifying the original list:
  return print(sorted(mylist)[::-1])

 def ex4():
  #List 1:
  list1=[1,3,5,6,8,9,4]
  #List 2:
  list2=[1,6,333,777,999,555,22]

  list3=[]
  #Add elements from list 1 and 2 to the new list:
  for i in range(len(list2)):
   list3.append(list2[i])
    
  for i in range(len(list1)):
   list3.append(list1[i])

  #Sort new list:
  list3.sort()

  commonlist=[]
  #Get the difference in sorted new list to find common items:
  for i in range(len(list3)-1):
   dif=list3[i+1]-list3[i]
   if dif==0:
  #List containing common items between the two lists:
    commonlist.append(list3[i])

  #List containing common items between the two is commonlist
  return commonlist

#Function that returns a list of all pairs of factors (as tuples) of a given number using list comprehension:
 def ex5(n):
  lista=[x for x in range(1,n) if n%x==0]
  lista.append(n)
  a=int(len(lista)/2)
  pairs1=lista[0:a]
  pairs2=lista[a:len(lista)]
  pairs2=pairs2[::-1]
  pares=[]
  for i in range(len(pairs1)):
   pair=(pairs1[i],pairs2[i])
   pares.append(pair)
  return pares

 def ex6():
  import time
     
  #Time all of the ways:
  #Naive way:
  #List creation:
  start_time = time.time()
  nums=list(range(0,1000))
  way1=[]
  #Append data in a loop:
  for i in nums:
   if nums[i]%3==0:
    way1.append(nums[i])
  end_time = time.time()
  elapsed_time1 = end_time - start_time

  #Using list comprehension:
  start_time = time.time()
  way2=[x for x in range(1000) if x%3==0]
  end_time = time.time()
  elapsed_time2 = end_time - start_time

  #Slicing an existing list:
  start_time = time.time()
  way3=nums[::3]
  end_time = time.time()
  elapsed_time3 = end_time - start_time
     
  #Directly with range():
  start_time = time.time()
  way4=list(range(0,1000,3))
  end_time = time.time()
  elapsed_time4 = end_time - start_time

  elapsed_times=[elapsed_time1, elapsed_time2, elapsed_time3, elapsed_time4]
  return elapsed_times

 def ex7(a):
 #Function to check if a string is a palindrome:
  flipped=a[::-1]
  if flipped==a:
   phrase='Your string is a palindrome'
  else:
   phrase='Your string is not a palindrome'
  return phrase

 def ex8(a):
 #Function to find a character with a maximum number of occurrences in a string:
  x=max(a, key=a.count)
  return(x, a.count(x))

 def ex9(n):
 #Function that returns first N prime numbers:
  primes=[True]*(n+1)
  nums=[]
  for i in range(2, int(n**0.5)+1):
   if primes[i]:
    for j in range(i*i, n+1, i):
     primes[j]=False
  for i in range(2,n+1):
   if primes[i]:
    nums.append(i)
  return nums

