
q=[2,1,3,4,5]

s=list(q)
n=len(q)
s.sort()
print(q)
print(s)

a=[*enumerate(q)]
print(a)
#while i<len(q):
vis = {k:False for k in range(n)}
print(vis)
print(a[2])
#    if s[i]==q[i]:
if a[2]==2:
	print("True")
else:
	print("False") #       i+=1
  #  else:
#            print("Too chaotic")
            
  #      else:
   #    
     #   i=i+1
#print(count)