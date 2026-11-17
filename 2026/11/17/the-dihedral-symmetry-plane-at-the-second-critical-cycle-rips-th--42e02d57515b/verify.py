from itertools import combinations
from collections import Counter
n=15;r=6
fs=[]
for m in range(1<<n):
 v=[i for i in range(n) if m>>i&1]
 if all(min((b-a)%n,(a-b)%n)<=r for a,b in combinations(v,2)):fs.append(v)
print('faces',len(fs),'fvector',dict(sorted(Counter(len(v)-1 for v in fs).items())))
def sign(a):
 return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def trace(f):
 s=0
 for v in fs:
  img=[f(i) for i in v]
  if sorted(img)==v:
   s+=(-1)**len(v)*sign(img)
 return -s
print('rot',[(a,trace(lambda i,a=a:(i+a)%n)) for a in range(n)])
print('ref',[(a,trace(lambda i,a=a:(a-i)%n)) for a in range(n)])
def orbtrace(f):
 unseen=set(range(n)); orbits=[]
 while unseen:
  i=min(unseen); cyc=[];j=i
  while j not in cyc:cyc.append(j);unseen.remove(j);j=f(j)
  orbits.append(cyc)
 ans=0
 for b in range(1<<len(orbits)):
  v=[j for t,o in enumerate(orbits) if b>>t&1 for j in o]
  if all(min((x-y)%n,(y-x)%n)<=r for x,y in combinations(v,2)):
   ans-=(-1)**sum(bool(b>>t&1) for t in range(len(orbits)))
 return ans
assert all(trace(lambda i,a=a:(i+a)%n)==orbtrace(lambda i,a=a:(i+a)%n) and trace(lambda i,a=a:(a-i)%n)==orbtrace(lambda i,a=a:(a-i)%n) for a in range(n))
print('INDEPENDENT_ORBIT_ENUMERATION_PASS')
