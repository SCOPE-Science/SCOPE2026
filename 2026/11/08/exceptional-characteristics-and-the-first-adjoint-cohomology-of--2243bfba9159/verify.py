"""Exact integer-linear-algebra verification for the indicated 8-dimensional Leibniz algebra.

Requires Python 3 and SymPy; all computations use integers or exact modular arithmetic.
"""
from collections import Counter
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Each tuple (left basis index, right basis index, output-coefficient dictionary).
PRODUCTS = [
 (1,1,{8:4}),(1,2,{3:1}),(1,3,{4:1}),(1,4,{6:1}),
 (1,5,{8:6}),(1,6,{8:1}),
 (2,1,{3:-1,7:-9,8:1}),(2,2,{7:-6,8:-1}),
 (2,3,{5:1}),(2,4,{7:3}),(2,5,{8:1}),(2,6,{8:2}),
 (3,1,{4:-1}),(3,2,{5:-1,8:-6}),(3,3,{7:-1,8:2}),
 (3,4,{8:1}),(4,1,{6:-1}),(4,2,{7:-1,8:-4}),
 (4,3,{8:-2}),(5,1,{7:-2,8:-2}),(5,2,{8:-1}),
 (6,1,{8:-1}),(6,2,{8:1}),(7,1,{8:-1})
]
N=8
c=[[[0]*N for _ in range(N)] for _ in range(N)]
for i,j,outputs in PRODUCTS:
    for k,value in outputs.items(): c[i-1][j-1][k-1]=value

# Leibniz right-multiplication identity ((xy)z) = x(yz)+(xz)y.
for i in range(N):
 for j in range(N):
  for k in range(N):
   for t in range(N):
    lhs=sum(c[i][j][r]*c[r][k][t] for r in range(N))
    rhs=sum(c[j][k][r]*c[i][r][t]+c[i][k][r]*c[r][j][t] for r in range(N))
    assert lhs==rhs,(i,j,k,t,lhs,rhs)

# Coordinates D_{v,u}: images D(e_u)=sum_v D_{v,u}e_v; column index v*8+u.
rows=[]
for i in range(N):
 for j in range(N):
  for k in range(N):
   v=[0]*(N*N)
   for r in range(N):
    v[k*N+r]+=c[i][j][r]
    v[r*N+i]-=c[r][j][k]
    v[r*N+j]-=c[i][r][k]
   if any(v):rows.append(v)

# The inner-derivation map x -> R_x, with R_x(y)=yx, flattened identically.
inner_cols=[]
for j in range(N):
 inner_cols.append([c[i][j][k] for k in range(N) for i in range(N)])
inner_rows=list(map(list,zip(*inner_cols)))

def invariants(A):
 s=smith_normal_form(Matrix(A),domain=ZZ)
 vals=[abs(int(s[i,i])) for i in range(min(s.rows,s.cols)) if s[i,i]!=0]
 return Counter(vals)
assert invariants(rows)==Counter({1:55,2:2,66:1}),invariants(rows)
assert invariants(inner_rows)==Counter({1:5,11:1}),invariants(inner_rows)

# Direct, independent modular ranks of the original integer matrices.
def rank_mod_p(matrix,p):
 a=[[x%p for x in row] for row in matrix]
 m=len(a);n=len(a[0]); rank=0
 for j in range(n):
  pivot=next((i for i in range(rank,m) if a[i][j]!=0),None)
  if pivot is None:continue
  a[rank],a[pivot]=a[pivot],a[rank]
  inv=pow(a[rank][j],-1,p)
  a[rank]=[(v*inv)%p for v in a[rank]]
  for i in range(rank+1,m):
   if a[i][j]:
    coeff=a[i][j]
    a[i]=[(u-coeff*v)%p for u,v in zip(a[i],a[rank])]
  rank+=1
 return rank
for p, expected_der, expected_inner in [(2,9,6),(3,7,6),(5,6,6),(7,6,6),(11,7,5),(13,6,6),(17,6,6)]:
 assert 64-rank_mod_p(rows,p)==expected_der
 assert rank_mod_p(inner_rows,p)==expected_inner

# An explicit derivation in characteristic eleven, with non-nilpotent action
# on the two-dimensional abelianization. Matrix columns are D(e_j).
D11=[
 [8,4,3,3,4,5,3,0],
 [0,5,6,7,10,6,7,0],
 [0,0,2,6,8,7,6,0],
 [0,0,0,10,4,6,8,0],
 [0,0,0,0,7,0,1,9],
 [0,0,0,0,0,7,1,0],
 [0,0,0,0,0,0,4,0],
 [0,0,0,0,0,0,0,1]
]
# D11[j][k] is coefficient of e_k in D(e_j).
for i in range(N):
 for j in range(N):
  for k in range(N):
   delta=sum(c[i][j][r]*D11[r][k] for r in range(N))
   delta-=sum(D11[i][r]*c[r][j][k]+D11[j][r]*c[i][r][k] for r in range(N))
   assert delta%11==0,(i,j,k,delta)
assert D11[0][0]%11==8 and D11[1][1]%11==5
assert all(D11[j][k]%11==0 for j in range(2) for k in range(2) if (j,k)==(1,0))
print('VERIFY_OK Leibniz_triples=512 derivation_equations=512 nonzero_rows=%d' % len(rows))
print('SMITH_DER 1^55 2^2 66^1 0^6')
print('SMITH_INNER 1^5 11^1 0^2')
print('H1_DIM char0=0 char2=3 char3=1 char11=2 otherwise=0')
print('CHAR11_DERIVATION_NONNILPOTENT_ON_ABELIANIZATION verified')
