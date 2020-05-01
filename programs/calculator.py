#Creating a Calculator 
 
#This lesson is about an example Python project: a simple calculator.   
  Each part explains a different section of the program.  
  The first section is the overall menu. This keeps on accepting user input until the user enters "quit", so a while loop is used.
  
#Complete the below code and discuss in the discussion group:
 print("Options:") 
   print("Enter 'add' to add two numbers") 
   print("Enter 'subtract' to subtract two numbers") 
   print("Enter 'multiply' to multiply two numbers") 
   print("Enter 'divide' to divide two numbers") 
   print("Enter 'quit' to end the program") 
   while True: 
    user_input = input(": ") 
 
   if user_input == "quit": 
      break 
   elif user_input == "add":
      first_no=int(input())
      second_no=int(input())
      print("the result of addition is:",first_no+second_no)
   elif user_input == "subtract":
    first_no=int(input())
      second_no=int(input())
      print("the result of subtraction is:",first_no-second_no) 
   elif user_input == "multiply":
   first_no=int(input())
      second_no=int(input())
      print("the result of multiplication is:",first_no*second_no) 
   elif user_input == "divide": 
   first_no=int(input())
      second_no=int(input())
      print("the result of division is:",first_no/second_no) 
   else: 
      print("Unknown input")
      continue
      
      
  #output:
  options:
  Enter 'add' to add two numbers.
  Enter 'subtract' to subtract two numbers.
  enter 'multiply' to multiply two numbers.
  Enter 'divide' to divide two numbers.
  Enter 'quit' to end the program.
  add
  4
  8
  the result of addition is:12
  subtract
  9
  5
  the result of subtraction is:4
  multiply
  6
  5
  the result of multiplication is:30
  divide
  25
  5
  the result of division is:5.0
  agf
  unknown input
  quit
