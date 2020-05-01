>>Task
#Read an integer x. and start printing its squares starting from 0 till entered no.
 
#Use for loop

#Sample Input 
5


#Sample Output 
0
1
4
9
16

#program
x=int(input("enter the input:"))
for val in range(x):
      sq=val*val
      print(sq)
      
#output:
enter the input:5
0
1
4
9
16
