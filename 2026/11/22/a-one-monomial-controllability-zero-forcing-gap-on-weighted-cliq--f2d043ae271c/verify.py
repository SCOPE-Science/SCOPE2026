#!/usr/bin/env python3
"""Standalone exact modular recheck of the weighted two-clique bridge controllability census.

Only prime-modular arithmetic is used for the checks. Passing a modular full-rank test
certifies full rank over the rationals; exhaustive agreement is supplementary to the
real-parameter analytic proof in RESULT.md.
"""
from itertools import combinations
from collections import Counter
P=1000003

def laplacian(p,q,a,b,t):
 n=p+q
 A=[[0]*n for _ in range(n)]
 edges=[(u,v,a) for u,v in combinations(range(p),2)] + [(u,v,b) for u,v in combinations(range(p,n),2)] + [(0,p,t)]
 for u,v,w in edges:
  A[u][u]+=w; A[v][v]+=w; A[u][v]-=w;A[v][u]-=w
 return [[int(x)%P for x in row] for row in A]

def rank_span(A,S):
 n=len(A); basis={}
 for s in S:
  vec=[int(i==s) for i in range(n)]
  for k in range(n):
   v=vec[:]
   for i,b in sorted(basis.items()):
    if v[i]:
     z=v[i]; v=[(x-z*y)%P for x,y in zip(v,b)]
   if any(v):
    pivot=next(i for i,x in enumerate(v) if x)
    inv=pow(v[pivot],P-2,P)
    basis[pivot]=[(x*inv)%P for x in v]
    if len(basis)==n:return n
   vec=[sum(A[i][j]*vec[j] for j in range(n))%P for i in range(n)]
 return len(basis)

def predicted(p,q,a,b,S):
 left=set(range(1,p)); right=set(range(p+1,p+q))
 ell=len(left-S); rr=len(right-S)
 if ell>1 or rr>1:return False
 if a*p==b*q and ell==1 and rr==1 and 0 not in S and p not in S:return False
 return bool(S)

def run():
 total=0
 examples=[(3,3,1,1,1),(3,3,1,1,7),(3,3,1,2,2),
 (3,4,1,1,1),(3,4,4,3,1),(3,4,4,3,5),
 (4,4,3,3,2),(4,4,2,3,4),(4,5,5,4,1),
 (4,5,1,1,6),(5,5,1,1,3)]
 for p,q,a,b,t in examples:
  A=laplacian(p,q,a,b,t)
  true=Counter();expected=Counter()
  for mask in range(1<<(p+q)):
   S={i for i in range(p+q) if mask>>i&1}
   e=predicted(p,q,a,b,S)
   r=rank_span(A,S)==p+q
   assert e==r,(p,q,a,b,t,sorted(S),e,r)
   if e:expected[len(S)]+=1
   if r:true[len(S)]+=1
   total+=1
  print(f'p={p} q={q} a={a} b={b} t={t}: {dict(sorted(true.items()))}')
  assert true==expected
 print(f'PASS {total} exact prime-field subset-rank tests')

if __name__=='__main__':run()
