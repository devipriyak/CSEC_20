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
res=s.startswith("p",0,4)
print "Starts with () start and end index"
print res
res=s.startswith("p")
print res#True


