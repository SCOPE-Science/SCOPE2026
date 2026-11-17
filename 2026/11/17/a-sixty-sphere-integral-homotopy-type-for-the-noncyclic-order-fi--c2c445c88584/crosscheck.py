#!/usr/bin/env python3
"""Independent clique enumeration and mod-prime homology check, standard library only."""
from itertools import combinations
from collections import Counter
L=((0,1,2,3,4),(1,0,3,4,2),(2,3,4,0,1),(3,4,1,2,0),(4,2,0,1,3))
N=25
A=[[False]*N for _ in range(N)]
for u in range(N):
 for v in range(u+1,N):
  r,c=divmod(u,5);s,d=divmod(v,5)
  A[u][v]=A[v][u]=(r==s or c==d or L[r][c]==L[s][d])
F=[[] for _ in range(6)]
for k in range(1,6):
 for vs in combinations(range(N),k):
  if all(A[u][v] for u,v in combinations(vs,2)):
   F[k].append(vs)
assert [len(x) for x in F][1:]==[25,150,250,79,15]
# Independent cochain rank computations in reduced degrees over primes.
def rank(simplices_a,simplices_b,p):
 ids={s:i for i,s in enumerate(simplices_a)}
 piv={}
 for s in simplices_b:
  col={ids[s[:j]+s[j+1:]]: (1 if j%2==0 else p-1) for j in range(len(s))}
  while col:
   lead=min(col)
   if lead not in piv:
    inv=pow(col[lead],-1,p)
    piv[lead]={j:v*inv%p for j,v in col.items() if v%p}
    break
   a=col[lead];rw=piv[lead];
   col={j:(col.get(j,0)-a*rw.get(j,0))%p for j in col.keys()|rw.keys()}
   col={j:v for j,v in col.items() if v%p}
 return len(piv)
for p in (2,3,5,7):
 ranks={k:rank(F[k-1],F[k],p) for k in range(2,6)}
 # Boundary ranks: d1=V-1=24, d2, d3, d4.
 b={1:150-ranks[2]-ranks[3],2:250-ranks[3]-ranks[4],3:79-ranks[4]-ranks[5],4:15-ranks[5]}
 assert b=={1:0,2:60,3:0,4:0},(p,b,ranks)
 print(f'p={p} Betti_1_to_4={tuple(b.values())}')
print('LATIN5_INDEPENDENT_MODULAR_CHECK_PASS')
