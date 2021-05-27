'''Cotrol Structures

If condition
Else condition
Elif ladder

Nested if
An if contains another if
if(condition) :
   if(condition) :
   Statements
else-if-elif
'''

username=raw_input()
if(username=="CSEC"):#Outer if block
      password=raw_input()
      if(password=="AEC"):#inner if block
            print "Valid Student"
      else:#executed when inner if block is false
            print("Invalid Password")

else:#executed when outer if block is false
      print("Invalid UserName!please check it")
      
      














