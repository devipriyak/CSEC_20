#remove()and pop()
list1=[123,456,768,231,5678,101,132,123,123,768]

print "Original List"
print list1
#L.remove(element)
#Removes the first item with the specified value
list1.remove(123)
print "After Modification List of elements"
print list1#[456, 768, 231, 5678, 101, 132, 123, 123, 768]
#L.pop([index])
#Removes the element at the specified position
remove_element=list1.pop()
print "Pop() with out index"
print remove_element
print "Pop(2) with index"
remove_element=list1.pop(2)
print remove_element
print list1

remove_element=list1.pop(24)#IndexError: pop index out of range

list2=[]
remove_element=list2.pop()#IndexError: pop index out of range









