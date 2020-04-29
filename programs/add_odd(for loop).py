>>Write a python script to add only odd numbers.

x=int(input("enter the number:"))
i=0
for i in range(x):
    if i%2!=0:
      print(i)
      i=i+1
      
  #output:
  enter the number:10
  1
  3
  5
  7
  9
