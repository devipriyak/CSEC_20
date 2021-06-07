#Nested For loop
innerloop=0
outerloop=0
print "i","j"

for i in range(6):#Outer for loop-executed 3 times
      outerloop+=1
      for j in range(8):#inner for loop is executed 48 times
            print i,j
            innerloop+=1
            
print("----Loops completed--- ")
print("Outer loop is executed %d times" %(outerloop))
print("Inner loop is executed %d times" %(innerloop))
'''
1.Inner loop execution is based on the outer loop condition
2.Every time the inner loop is newly executed based on
   the outerloop
i=0---->j=0,print 0,0
   ---->j=1,print 0,1
   ---->j=2,print 0,2
   ---->j=3 conditionfalse:Inner loop is terminated
i=1---->j=0,print 1,0
   ---->j=1,print 1,1
   ---->j=2,print 1,2
   ---->j=3 conditionfalse:Inner loop is terminated
i=2---->j=0,print 2,0
   ---->j=1,print 2,1
   ---->j=2,print 2,2
   ---->j=3 conditionfalse:Inner loop is terminated
i=3--->Condition is false:Outer loop is terminated
''' 
