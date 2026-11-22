"""Independent support orbit-block and Möbius verification for del Pezzo twists.

Pure standard-library Python. Does not enumerate all geometric supports.
"""
from itertools import combinations
from collections import Counter
from math import lcm
from json import loads
from pathlib import Path

curves=[]
for i in range(7):curves.append((0,tuple(-int(j==i) for j in range(7))))
for S in combinations(range(7),2):curves.append((1,tuple(int(j in S) for j in range(7))))
for S in combinations(range(7),5):curves.append((2,tuple(int(j in S) for j in range(7))))
for i in range(7):curves.append((3,tuple(2 if j==i else 1 for j in range(7))))
assert len(curves)==56
ids={c:i for i,c in enumerate(curves)}
def meet(i,j):
 d,a=curves[i];e,b=curves[j]
 return d*e-sum(x*y for x,y in zip(a,b))

def blocks_fixed(perm,geiser):
 """Count fixed supports from *orbits of curves*, not geometric supports."""
 vertex=[]
 for d,a in curves:
  b=[0]*7
  for i,j in enumerate(perm):b[j]=a[i]
  if geiser:d,b=3-d,[1-x for x in b]
  vertex.append(ids[(d,tuple(b))])
 remaining=set(range(56));cycles=[]
 while remaining:
  start=min(remaining);orb=[];i=start
  while i in remaining:
   remaining.remove(i);orb.append(i);i=vertex[i]
  assert i==start
  cycles.append(orb)
 blocks=[c for c in cycles if all(meet(a,b)==0 for a,b in combinations(c,2))]
 compatibility=[]
 for a in range(len(blocks)):
  compatibility.append(sum((1<<b) for b in range(a+1,len(blocks)) if all(meet(i,j)==0 for i in blocks[a] for j in blocks[b])))
 count=Counter({0:1})
 def visit(tail,degree):
  while tail:
   bit=tail&-tail;tail-=bit;i=bit.bit_length()-1
   nextdegree=degree+len(blocks[i]);count[nextdegree]+=1
   visit(tail&compatibility[i],nextdegree)
 visit((1<<len(blocks))-1,0)
 return [count[i] for i in range(8)]

def partition_generators(n,upper=None):
 if not n:yield ()
 else:
  for t in range(min(n,upper or n),0,-1):
   for rest in partition_generators(n-t,t):yield (t,)+rest

def permutation_for_partition(p):
 perm=list(range(7));start=0
 for size in p:
  for i in range(size):perm[start+i]=start+(i+1)%size
  start+=size
 return perm

def power(p,n):
 sigma=permutation_for_partition(p);t=list(range(7))
 for _ in range(n):t=[sigma[i] for i in t]
 return t

def mobius(k):
 if k==1:return 1
 sign=1;t=k;p=2
 while p*p<=t:
  if t%p==0:
   t//=p;sign=-sign
   if t%p==0:return 0
  p+=1
 if t>1:sign=-sign
 return sign

def divisors(n):return [j for j in range(1,n+1) if n%j==0]

def run():
 out={}
 for p in partition_generators(7):
  k=','.join(str(x) for x in p);out[k]={}
  for twist in (0,1):
   length=lcm(*p)*(2 if twist else 1)
   # Count geometric supports fixed by the dth power of the action.
   fixed={d:sum(blocks_fixed(power(p,d),bool(twist*d%2))) for d in divisors(length)}
   orbits={d:sum(mobius(d//e)*fixed[e] for e in divisors(d))//d for d in divisors(length)}
   assert all(v>=0 for v in orbits.values())
   assert sum(d*n for d,n in orbits.items())==33645
   out[k]['geiser' if twist else 'ordinary']={'fixed':fixed[1], 'cycle_spectrum':{str(d):v for d,v in orbits.items() if v}}
   print(k,'geiser' if twist else 'ordinary',fixed[1],orbits)
 return out

if __name__=='__main__':
 result=run()
 wanted=loads(Path(__file__).with_name('CHAMBER_SPECTRA.json').read_text(encoding='utf-8'))
 for p in result:
  for t in ['ordinary','geiser']:
   assert result[p][t]['fixed']==wanted[p][t]['fixed'],(p,t)
   assert result[p][t]['cycle_spectrum']==wanted[p][t]['cycle_spectrum'],(p,t)
 print('INDEPENDENT_ORBIT_BLOCK_AND_MOBIUS_30_CASES_OK')
