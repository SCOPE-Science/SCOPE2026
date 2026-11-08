#!/usr/bin/env python3
"""Independent 4-state transfer calculation and cyclic-word enumeration for wheel chip firing."""
from itertools import product
from collections import defaultdict

def plus(a,b):
 r=defaultdict(int,a)
 for e,c in b.items():r[e]+=c
 return {e:c for e,c in r.items() if c}
def times(a,b):
 r=defaultdict(int)
 for e,c in a.items():
  for d,k in b.items():r[e+d]+=c*k
 return dict(r)
def matmul(A,B):
 n=len(A)
 return [[sum_poly(times(A[i][k],B[k][j]) for k in range(n)) for j in range(n)] for i in range(n)]
def sum_poly(it):
 d={}
 for x in it:d=plus(d,x)
 return d

def trace(m,yexp):
 pairs=((0,0),(0,1),(1,0),(1,1))
 M=[[{} for _ in range(4)] for _ in range(4)]
 for i,(p,c) in enumerate(pairs):
  for e in (0,1):
   j=pairs.index((c,e))
   if c:
    count=2-p-e
    wt={3+h:1 for h in range(count)}
   else:
    count=1+p+e
    wt={2-p-e+h:1 for h in range(count)}
    wt={e+yexp:k for e,k in wt.items()}
   M[i][j]=plus(M[i][j],wt)
 P=[[{0:int(i==j)} if i==j else {} for j in range(4)] for i in range(4)]
 for _ in range(m):P=matmul(P,M)
 return sum_poly(P[i][i] for i in range(4))

def transfer(m):
 a,b=trace(m,0),trace(m,1)
 D=defaultdict(int,a)
 for e,c in b.items():D[e]-=c
 Q={};last=0
 for e in range(max(D)+1):
  last=D[e]+last
  Q[e]=last
 assert last==0 and Q[max(Q)]==0
 del Q[max(Q)]
 return {m+e:2*c for e,c in Q.items() if c}

def enumerated(m):
 H=defaultdict(int)
 for w in product((0,1),repeat=m):
  b=m-sum(w)
  if b==0:continue
  d={0:1}
  for i,c in enumerate(w):
   p,e=w[(i-1)%m],w[(i+1)%m]
   if c:
    v={3+j:1 for j in range(2-p-e)}
   else:
    v={2-p-e+j:1 for j in range(1+p+e)}
   d=times(d,v)
  d=times(d,{m+j:1 for j in range(b)})
  for k,v in d.items():H[k]+=2*v
 return dict(H)

if __name__=='__main__':
 for m in range(3,13):
  H=transfer(m);E=enumerated(m)
  assert H==E,(m,H,E)
  r=m//2
  lo=3*m-r;hi=4*m+r-1
  assert set(H)==set(range(lo,hi+1))
  assert H[lo]==H[hi]==(4 if m%2==0 else 2*m)
  assert all(H[k]==H[7*m-1-k] for k in H)
  print(f'm={m} transfer=word-enumeration, support=[{lo},{hi}], endpoints={H[lo]}, mass-symmetry=OK, total={sum(H.values())}')
 print('ALL CHECKS PASSED')
