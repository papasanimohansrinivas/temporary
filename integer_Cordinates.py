from __future__ import division
import cStringIO

import sys

sys.setrecursionlimit(10000)

edges = []

file = open("graph.txt","r")


vertices = []



dump = file.next()
edge = file.next()

for line in file:
	v1,v2,weight = line.split()
	v1,v2,weight = int(v1),int(v2),int(float(weight)*100)
	if weight!=0:
		edges.append((v1,v2,weight))
	else:
		weight = int(float(line.split()[2])*1000)
		edges.append((v1,v2,weight))



# print edges
corrdinates = [t for t in xrange(int(dump))]

# x,y,r =[int(z) for z in raw_input().split()]

def cor_dinates(corrdinates,x,y,r):
	# file = cStringIO.StringIO()
	for x_cord in xrange(x-r,x+r+1):
		for y_cord in xrange(y-r,y+r+1):
			if (x_cord-x)**2+(y_cord-y)**2==r**2:
				# file.write(" "+str(x_cord)+" "+str(y_cord)+" "+"\n")
				if (x_cord,y_cord) not in corrdinates:
					return (x_cord,y_cord)
	return None




count = 0



def recursion(count,corrdinates,edges):

	if count==len(edges):
		print corrdinates
		return corrdinates


	if len(corrdinates)>0:
		if corrdinates[len(corrdinates)-1]==None:
			# print "sadf"
			return corrdinates
	x,y = 0,0

	if len(corrdinates)!=0:
		x,y = corrdinates[len(corrdinates)-1]

	r = edges[count][2]
	if cor_dinates(corrdinates,x,y,r)!=None:
		cord=cor_dinates(corrdinates,x,y,r)
		corrdinates[edges[0]]=cord
	else:
		print cor_dinates(corrdinates,x,y,r),corrdinates,edges[count],count,len(edges)
		return corrdinates


	recursion(count+1,corrdinates,edges)


# print corrdinates

# print count
# print file.getvalue()


# print recursion(0,corrdinates,edges)


list3 = [1,2,3,3,]

# next(list3)