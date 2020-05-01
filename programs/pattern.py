#Have to print this pattern: 
#N will be user input.
#Have to print the right triangle pattern with N-1 lines.
#Sample Input: 
N=5 
#Sample Output:
1
22
333
4444

#program:

N=int(input("enter the number:"))
for i in range(1,N):
    for j in range(1,i+1):
         print(i,end=" ")
    print()
    
  #output:
  enter the number:5
  1
  2 2
  3 3 3
  4 4 4 4
  
