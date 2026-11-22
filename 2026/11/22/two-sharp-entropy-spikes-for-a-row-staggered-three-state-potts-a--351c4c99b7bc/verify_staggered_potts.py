#!/usr/bin/env python3
"""Exact arithmetic checks for the two-color staggered-field triangular ladder.

Three Potts colors 0,1,2; row-top favors 0 and row-bottom favors 1.
Columns have a rung, two horizontal links, and a forward upper-to-lower link.
No external libraries are needed.
"""
from fractions import Fraction as F
from itertools import product
S=list(product(range(3),repeat=2)); N=9
C=[[int(v[0]==v[1])+int(u[0]==v[0])+int(u[1]==v[1])+int(u[0]==v[1]) for v in S] for u in S]
M=[[int(v[0]==0)+int(v[1]==1) for v in S] for u in S]
endpoints=[
 (F(0),F(0),[F(0)]*9),
 (F(1),F(-2,3),[F(-1,3),F(-4,3),F(-2,3),F(-1,3),F(0),F(-2,3),F(0),F(-1),F(0)]),
 (F(2),F(-2),[F(0),F(-2),F(-1),F(0),F(0),F(0),F(0),F(-1),F(0)])
]

def potential(h):
 if h>=2:
  return F(2)-2*h,endpoints[2][2]
 i=0 if h<=1 else 1
 a,g,p=endpoints[i];b,k,q=endpoints[i+1];t=(h-a)/(b-a)
 return (1-t)*g+t*k,[(1-t)*p[j]+t*q[j] for j in range(9)]

def adjacency(h):
 g,p=potential(h)
 T=[[0]*N for _ in range(N)]
 for u in range(N):
  for v in range(N):
   delta=F(C[u][v])-h*M[u][v]-g+p[u]-p[v]
   assert delta>=0,(h,u,v,delta)
   if delta==0:T[u][v]=1
 return T

def mul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def cp(A):
 B=[[int(i==j) for j in range(N)] for i in range(N)];trace=[0]
 for k in range(1,N+1):
  B=mul(B,A);trace.append(sum(B[i][i] for i in range(N)))
 out=[1]
 for k in range(1,N+1):
  t=-sum(out[k-i]*trace[i] for i in range(1,k+1))
  assert t%k==0
  out.append(t//k)
 return out

def poly(A,B):
 P=[0]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):P[i+j]+=x*y
 return P

def powp(A,n):
 P=[1]
 for _ in range(n):P=poly(P,A)
 return P
specs=[
 (F(1,2),poly(powp([1,0],3),poly(powp([1,-1],2),powp([1,1,1],2)))),
 (F(1),poly(powp([1,0],3),[1,0,0,-3,0,0,1])),
 (F(3,2),poly(powp([1,0],6),poly([1,-1],[1,1,1]))),
 (F(2),poly(powp([1,0],6),[1,-1,-2,-1])),
 (F(3),poly(powp([1,0],8),[1,-1]))
]
for h,expect in specs:
 actual=cp(adjacency(h));assert actual==expect,(h,actual,expect)
 print('EXACT_CHARPOLY_OK',h)
for h,g,p in endpoints:
 assert potential(h)==(g,p)
 adjacency(h)
print('DUAL_ENDPOINT_INEQUALITIES_OK',3*9*9)

index={s:i for i,s in enumerate(S)}
cycles=[[(0,1),(1,2),(2,0)],[(0,1),(0,2),(2,1)],[(0,1)]]
values=[(F(0),F(2,3)),(F(2,3),F(4,3)),(F(2),F(2))]
for states,(e,m) in zip(cycles,values):
 ids=[index[s] for s in states];k=len(ids)
 ce=sum(C[ids[i]][ids[(i+1)%k]] for i in range(k));cm=sum(M[ids[i]][ids[(i+1)%k]] for i in range(k))
 assert (F(ce,k),F(cm,k))==(e,m)
print('THREE_PERIODIC_WITNESSES_OK')

h2=[1,2,3,4,6] # twice the field: 1/2, 1, 3/2, 2, 3
expected=[6,21,3,98,1]
minima=[10**9]*5;counts=[0]*5
for word in product(range(9),repeat=6):
 c=sum(C[word[i]][word[(i+1)%6]] for i in range(6))
 m=sum(M[word[i]][word[(i+1)%6]] for i in range(6))
 for i,h in enumerate(h2):
  energy=2*c-h*m
  if energy<minima[i]:minima[i]=energy;counts[i]=1
  elif energy==minima[i]:counts[i]+=1
assert counts==expected,(counts,expected)
assert minima==[-4,-8,-16,-24,-48],minima
print('EXHAUSTIVE_CLOSED_SIX_COLUMNS_OK',9**6,'counts',counts)
print('ALL_EXACT_CHECKS_PASSED')
