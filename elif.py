'''
if  condition:
	statement(s)
elif condition:
	Statements(s)
elif  condition:
	statement(S)
.....
else:
     Statement(s)
'''
#Whether given number is divisible by 2 or 3 or 4 or 5
#other wise not divisble by 2 to 5
no=int(raw_input())#input from STDIN
if no%2==0:
      print('Divisible by 2')
elif no%3==0:#15 --condition is true
     print('Divisible by 3')
elif no%4==0:
     print('Divisible by 4')
elif no%5==0:
     print('Divisible by 5')
else:
      print('Number is not divisible by 2,3,4,5')

'''Output
case 1:
2
Divisible by 2
Case2:
9
Divisible by 3
15
Divisible by 3
25
Divisible by 5
'''
      








