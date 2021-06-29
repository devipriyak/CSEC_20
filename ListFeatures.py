numbers_list=[10,20,456,40]
print "Original List"
print numbers_list#[10, 20, 456, 40]
print numbers_list[1]
#Modify the Second element i.e 20 will be changed with 70
numbers_list[1]=70
#List is a Mutable Object
print "After Modifying List"
print numbers_list#[10, 70, 456, 40]
#Traverse the List
print "Traverse-Element by Element"
for i in numbers_list:
      print i
      
'''
10
70
456
40
'''
