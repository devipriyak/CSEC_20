#reverse()
list1=[123,456,768,231,5678,101]
print "Original List"
print list1
print "reverse()"
list1.reverse()#Reverse the List
print list1

print "Sort"
list1.sort(reverse=True)
print list1
'''
Original List
[123, 456, 768, 231, 5678, 101]
reverse()
[101, 5678, 231, 768, 456, 123]
Sort
[5678, 768, 456, 231, 123, 101]
'''
