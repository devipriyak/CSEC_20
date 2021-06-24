mainstring=raw_input("Enter main string")
searchstring=raw_input("Enter search string")
max_string=max(mainstring)#function
min_string=min(mainstring)#function
print "Max()"
print max_string#
print "Min()"
print min_string
#Verify particular characters are existed
#in -membership operator
if searchstring in mainstring:#substring is existed in the mai string
      print "Search string is existed"
else :
      print "Search string is not existed"
'''Enter main stringdhfh  dbfjb
Enter search stringjdbj
Max()
j
Min()
 
Search string is not existed

'''
