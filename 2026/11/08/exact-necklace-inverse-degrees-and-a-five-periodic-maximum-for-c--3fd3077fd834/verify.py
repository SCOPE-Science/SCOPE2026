"""Standalone independent finite checks for cyclic Rule 12 inverse-degree theorem."""
from collections import defaultdict
from functools import lru_cache
from math import gcd

def rotations(w):return [w[i:]+w[:i] for i in range(len(w))]
def canon(w):return min(rotations(w))
def rule12(w):
 n=len(w)
 return tuple(int(w[i]==1 and w[(i-1)%n]==0) for i in range(n))
def necklace(k,a):
 return sum(a**gcd(j,k) for j in range(k))//k

def inverse_degree(y):
 n=len(y); pos=[i for i,b in enumerate(y) if b]
 if not pos:return 2
 gaps=[(pos[(i+1)%len(pos)]-pos[i])%n for i in range(len(pos))]
 if len(pos)==1:gaps=[n]
 if min(gaps)<2:return 0
 k=len(gaps)
 ell=next(t for t in range(1,k+1) if k%t==0 and all(gaps[i]==gaps[i%t] for i in range(k)))
 h=k//ell
 a=1
 for d in gaps[:ell]:a*=d-1
 return necklace(h,a)

def predicted(n):
 small={1:2,2:2,3:2,4:3,5:4,6:5,7:6,8:8,9:12,10:15,11:20,12:24,13:36,14:48,15:60,16:80,17:108,18:144,19:192,20:240}
 if n<=20:return small[n]
 k,r=divmod(n,5)
 return (243*4**(k-4),81*4**(k-3),27*4**(k-2),9*4**(k-1),3*4**k)[r]

@lru_cache(None)
def compositions(n,least):
 if n==0:return [()]
 return [ (d,)+p for d in range(least,n+1) for p in compositions(n-d,d)]

def partition_max(n):
 best=2
 for p in compositions(n,2):
  if not p:continue
  prod=1
  for d in p:prod*=d-1
  if len(set(p))>1:degree=prod
  else:degree=necklace(len(p),p[0]-1)
  best=max(best,degree)
 return best

def brute(n):
 fibers=defaultdict(set)
 for xmask in range(1<<n):
  x=tuple((xmask>>i)&1 for i in range(n))
  fibers[canon(rule12(x))].add(canon(x))
 for y,pre in fibers.items():
  assert len(pre)==inverse_degree(y),(n,y,len(pre),inverse_degree(y))
 return max(map(len,fibers.values())),len(fibers)

if __name__=='__main__':
 total=0
 for n in range(1,15):
  maximum,count=brute(n)
  assert maximum==predicted(n),(n,maximum,predicted(n))
  total+=count
 for n in range(1,26):
  p=partition_max(n)
  assert p==predicted(n),(n,p,predicted(n))
 print('VERIFY_OK cyclic_necklaces=',total,'brute_lengths=1..14','partition_lengths=1..25')
