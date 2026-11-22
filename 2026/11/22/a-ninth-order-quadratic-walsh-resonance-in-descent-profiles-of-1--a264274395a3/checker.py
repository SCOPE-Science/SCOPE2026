from itertools import permutations, combinations
from math import comb
from collections import Counter

def cat(n):return comb(2*n,n)//(n+1)
def avoid132(p):
 n=len(p)
 for j in range(1,n-1):
  left_min=min(p[:j]); top=p[j]
  for k in range(j+1,n):
   if left_min<p[k]<top:return False
 return True

def fwht(a):
 a=a[:]; m=len(a); step=1
 while step<m:
  for base in range(0,m,step*2):
   for i in range(base,base+step):
    u,v=a[i],a[i+step];a[i]=u+v;a[i+step]=u-v
  step*=2
 return a

def brute(n):
 a=[0]*(1<<(n-1))
 for p in permutations(range(n)):
  if not avoid132(p):continue
  des=sum(1<<i for i in range(n-1) if p[i]>p[i+1])
  a[des]+=1
 assert sum(a)==cat(n)
 return fwht(a)

from functools import lru_cache
@lru_cache(None)
def recurrent(n,mask):
 if n<=1:return 1
 return sum(recurrent(l,mask&((1<<max(l-1,0))-1)) * recurrent(r, mask>>(l+1)) *(-1 if r>0 and ((mask>>l)&1) else 1) for l in range(n) for r in [n-l-1])

for n in range(2,10):
 b=brute(n)
 for s in range(1<<(n-1)):
  assert b[s]==recurrent(n,s),(n,s,b[s],recurrent(n,s))
 ps=[s for s in range(len(b)) if s.bit_count()==2 and b[s]==0]
 print(n,'catalan',cat(n),'two-character zeros', [(i+1,j+1) for s in ps for i,j in [tuple(k for k in range(n-1) if s&(1<<k))]],'onezero',[i+1 for i in range(n-1) if b[1<<i]==0])
 for s in (3,5):
  if n>=s.bit_length()+1:
   assert b[s]==cat(n)-4*cat(n-1)+2*cat(n-2)
for n in range(4,35):
 target=cat(n)-4*cat(n-1)+2*cat(n-2)
 assert recurrent(n,3)==recurrent(n,5)==target
print('PASS: independent brute, two-coordinate table and infinite-formula finite replay')
