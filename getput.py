def dumpit(fn,s):
	fd=open(fn,"w")
	fd.write(s)
	fd.close()

def getit(fn):
	fd=open(fn)
	s=fd.read()
	fd.close()
	return s	
	
