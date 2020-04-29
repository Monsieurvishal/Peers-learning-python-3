>>Write a python script to take input from the user and print till that number.
#Ex: if input is 10 print from 1 till 10.
    
n=int(input("enter the number:"))
i=0
for i in range(n):
    print(i)
    i=i+1
print("finished")

#output:
enter the number:
0
1
2
3
4
5
6
7
8
9
finished
