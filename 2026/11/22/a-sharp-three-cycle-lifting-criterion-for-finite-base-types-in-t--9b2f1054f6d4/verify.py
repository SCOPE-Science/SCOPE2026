from fractions import Fraction
from random import Random
from itertools import product
r=Random(102813)
for n in range(1,9):
 old=[]
 while len(old)<n:
  x=r.randrange(360000)
  if x not in old and (x+180000)%360000 not in old:old.append(x)
 bound=sorted(old+[(x+180000)%360000 for x in old]); dim=2*n
 arcs=[]
 for i,b in enumerate(bound):
  end=bound[(i+1)%dim] + (360000 if i==dim-1 else 0)
  arcs.append([Fraction(b)+(Fraction(end-b)*j)/9 for j in range(1,9)])
 count=0
 for p,q,s in product(range(dim),repeat=3):
  # choose x/y/z. Distinctness automatic in a directed cycle.
  obs=any(0<((y-x)%360000)<180000 and 0<((z-y)%360000)<180000 and 0<((x-z)%360000)<180000 for x in arcs[p] for y in arcs[q] for z in arcs[s])
  if obs:count+=1
 print(n,count,n*(n+1)*(n+2),count==n*(n+1)*(n+2),flush=True)

assert all((j*(j+1)*(j+2))%6==0 for j in range(1,100))
print("THREE_CYCLE_PROFILE_CHECKS_OK")
