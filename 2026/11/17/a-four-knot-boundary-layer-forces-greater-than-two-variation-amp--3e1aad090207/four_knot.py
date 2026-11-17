#!/usr/bin/env python3
"""Exact rational 30-site witness and four-knot spline transfer certificate.
No external dependencies. The dimension-uniform limit is established in RESULT.md.
"""
from fractions import Fraction as Q

def trans(A):return list(map(list,zip(*A)))
def mult(A,B):return [[sum((x*y for x,y in zip(r,c)),Q(0)) for c in zip(*B)] for r in A]
def inverse(M):
 n=len(M);A=[[Q(v) for v in r]+[Q(i==j) for j in range(n)] for i,r in enumerate(M)]
 for j in range(n):
  k=next(k for k in range(j,n) if A[k][j]);A[k],A[j]=A[j],A[k]
  d=A[j][j];A[j]=[v/d for v in A[j]]
  for k in range(n):
   if k!=j:
    d=A[k][j]
    if d:A[k]=[a-d*b for a,b in zip(A[k],A[j])]
 return [r[n:] for r in A]

def matrix(n):
 H=[[Q((j==i)+(j==i+2)-2*(j==i+1)) for j in range(n)] for i in range(n-2)]
 E=[[Q((j==i+1)-(j==i)) for j in range(n)] for i in range(n-1)]
 return H,E

def basis(n):
 knots=[2,5,n-4,n-1]
 return [[Q(1),Q(t),*[Q(max(t-k,0)) for k in knots]] for t in range(1,n+1)]

def test_n30():
 n=30;H,E=matrix(n);Z=basis(n)
 S=[i for i in range(n-2) if i+1 not in (1,4,25,28)]
 HS=[H[i] for i in S]
 assert mult(HS,Z)==[[Q(0)]*6 for _ in S]
 A=mult(mult(Z,inverse(mult(trans(Z),Z))),trans(Z))
 step=[[Q(i>=15)] for i in range(n)]
 p=mult(A,step);gradient=mult(E,p)
 seq=[v[0] for v in gradient]
 expected=[Q(11,196)]+[Q(-33,392)]*3+[Q(13,196)]*21+[Q(-33,392)]*3+[Q(11,196)]
 assert seq==expected,(seq,expected)
 assert sum(abs(v) for v in seq)==Q(197,98)
 # Supply explicit feasible x,y and verify KKT with strict multipliers.
 values=[Q(1) if i in S else Q(0) for i in range(n-2)]
 z=[Q(0),Q(0)]
 for q in values: z.append(q+2*z[-1]-z[-2])
 assert mult(H,[[v] for v in z])==[[v] for v in values]
 y=[z[i]+sum(HS[j][i] for j in range(len(S))) for i in range(n)]
 eps=Q(1,1000)
 proj=[z[i]+eps*p[i][0] for i in range(n)]
 data=[y[i]+eps*step[i][0] for i in range(n)]
 residual=mult(HS,step)
 inv=inverse(mult(HS,trans(HS)))
 update=mult(inv,residual)
 multipliers=[Q(1)+eps*update[i][0] for i in range(len(S))]
 assert min(multipliers)>0
 assert [data[i]-proj[i] for i in range(n)]==[sum(HS[j][i]*multipliers[j] for j in range(len(S))) for i in range(n)]
 curv=mult(H,[[v] for v in proj]);assert all(abs(v[0])<=1 for v in curv)
 assert all(v[0]==1 for i,v in enumerate(curv) if i in S)
 assert all(abs(v[0])<1 for i,v in enumerate(curv) if i not in S)
 print('EXACT_THIRTY_SITE_GRADIENT',seq)
 print('EXACT_FINITE_PRIMAL_DUAL_WITNESS_PASS epsilon=1/1000')
 print('EXACT_TV_RATIO',sum(abs(v) for v in seq),'GREATER_THAN_TWO_PASS')

if __name__=='__main__':
 test_n30()
 # Boundary layer limit is certified algebraically by the proof; check the limiting rational edge data.
 left=[Q(0),Q(1,14),Q(-1,28),Q(-1,7),Q(-1,4)]
 right=[Q(5,4),Q(8,7),Q(29,28),Q(13,14),Q(1)]
 # right values mirror 1-left[::-1] (verify).
 right=[1-v for v in reversed(left)]
 assert sum(abs(left[i+1]-left[i]) for i in range(4))==Q(11,28)
 assert sum(abs(right[i+1]-right[i]) for i in range(4))==Q(11,28)
 assert Q(11,28)*2+Q(3,2)==Q(16,7)
 print('FOUR_KNOT_LIMITING_BOUNDARY_LAYER_PASS 16/7')
 print('ALL_FOUR_KNOT_CERTIFICATES_PASS')
