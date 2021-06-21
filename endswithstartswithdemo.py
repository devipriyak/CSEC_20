#startswith#(prefix,[start,[end]]
#endswith
s="python"
#Checking the String s is started with K or not
res=s.startswith("K")
print "startswith()"
print res #False
print "starts with()"
res=s.startswith("P")#capital-P
print res #False
res=s.startswith("p",1,4)
print "Starts with () start and end index"
print res
res=s.startswith("p",0,4)#true
print "Starts with () start and end index"
print res
res=s.startswith("p")#true
print res#True
#endswith()
s='python'
res=s.endswith('n')#true
print (res)
res=s.endswith('N')#false
print (res)
res=s.endswith('n',0,6)#true
print (res)
res=s.endswith('n',1,5)#false
print (res)
'''
startswith()
False
starts with()
False
Starts with () start and end index
False
Starts with () start and end index
True
True
True
False
True
False
'''
