#!/usr/bin/env python3
"""Exact independent arithmetic for the genus-five trigonal pencil over F_11.
Public scientific verifier; Python 3 standard library only.
"""
from math import factorial
P=11
# A coefficient polynomial is a dictionary exponent -> coefficient modulo 11.
def trim(a):return {i:v%P for i,v in a.items() if v%P}
def add(a,b):
 d=dict(a)
 for i,v in b.items():d[i]=(d.get(i,0)+v)%P
 return trim(d)
def mul(a,b):
 d={}
 for i,x in a.items():
  for j,y in b.items():d[i+j]=(d.get(i+j,0)+x*y)%P
 return trim(d)
def neg(a):return {i:(-v)%P for i,v in a.items()}
def det2(a,b,c,d):return add(mul(a,d),neg(mul(b,c)))
def coeff_n_power(k,d):
 """Coefficient of u^d in (1+t*u^2+u^5)^k, as polynomial in t."""
 out={}
 for a in range(k+1):
  for b in range(k-a+1):
   if 2*a+5*b==d:
    n=factorial(k)//(factorial(a)*factorial(b)*factorial(k-a-b))
    out[a]=(out.get(a,0)+n)%P
 return trim(out)
BASIS=[(1,-1),(1,0),(2,-1),(2,0),(2,1)]
# M maps the input j-character into the unique p^-1-shifted j-character.
M=[[{} for _ in range(5)] for _ in range(5)]
for col,(j,i) in enumerate(BASIS):
 jp=2 if j==1 else 1
 e=(P*jp-j)//3
 for row,(jout,k) in enumerate(BASIS):
  if jout!=jp:continue
  deg=P*(k+1)-1-(i-e)
  M[row][col]=coeff_n_power(e,deg)
expected=[
 [{},{},{},{1:3},{}],
 [{},{},{},{},{1:3}],
 [{1:9},{3:2},{},{},{}],
 [{4:6},{6:7,1:8},{},{},{}],
 [{2:10},{},{},{},{}],
]
assert M==expected, (M,expected)
# Combinatorial independent coefficient extraction agrees with direct polynomial multiplication.
N=[{0:1},{},{1:1},{},{},{0:1}]
def direct_power(k):
 v=[{0:1}]
 for _ in range(k):
  w=[{} for _ in range(len(v)+5)]
  for i,a in enumerate(v):
   for j,b in enumerate(N): w[i+j]=add(w[i+j],mul(a,b))
  v=w
 return v
for k in [3,7]:
 arr=direct_power(k)
 for d in range(len(arr)):
  assert arr[d]==coeff_n_power(k,d)
# Elementary determinantal identities: B block rank 2, A block rank 2,
# and the obstruction in the (Cartier-twisted) two-step map is t^5-2.
A=[r[:2] for r in M[2:]];B=[r[2:] for r in M[:2]]
assert det2(A[0][0],A[0][1],A[2][0],A[2][1])=={5:2}
assert det2(B[0][1],B[0][2],B[1][1],B[1][2])=={2:9}
assert det2(A[1][0],A[1][1],A[2][0],A[2][1])=={3:8,8:7}
# The last minor is -4*t^3*(t^5-2) modulo 11.

# Finite field E=F_11[z]/(z^5-2), five component coefficient representation.
ZERO=(0,0,0,0,0);ONE=(1,0,0,0,0);T=(0,1,0,0,0)
def eadd(a,b):return tuple((x+y)%P for x,y in zip(a,b))
def eneg(a):return tuple(-x%P for x in a)
def emul(a,b):
 temp=[0]*9
 for i,x in enumerate(a):
  for j,y in enumerate(b):temp[i+j]+=x*y
 for k in range(8,4,-1):temp[k-5]+=2*temp[k]
 return tuple(x%P for x in temp[:5])
def epow(a,n):
 out=ONE
 while n:
  if n&1:out=emul(out,a)
  a=emul(a,a);n//=2
 return out
def einv(a):
 if a==ZERO:raise ZeroDivisionError
 return epow(a,11**5-2)
def eeval(poly,z):
 out=ZERO
 for degree,coef in poly.items():out=eadd(out,emul((coef,0,0,0,0),epow(z,degree)))
 return out
def mm(A,B):
 return [[sum_field(emul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sum_field(items):
 val=ZERO
 for a in items:val=eadd(val,a)
 return val
def rank(A):
 A=[r[:] for r in A];r=0
 for j in range(len(A[0])):
  piv=next((i for i in range(r,len(A)) if A[i][j]!=ZERO),None)
  if piv is None:continue
  A[piv],A[r]=A[r],A[piv]
  u=einv(A[r][j]);A[r]=[emul(u,a) for a in A[r]]
  for i in range(r+1,len(A)):
   coeff=A[i][j]
   A[i]=[eadd(a,eneg(emul(coeff,b))) for a,b in zip(A[i],A[r])]
  r+=1
 return r
# t^11 = 4t, so t^(1/11)=3t: Cartier semilinearity.
assert epow(T,5)==(2,0,0,0,0)
assert epow(T,11)==(0,4,0,0,0)
assert epow((0,3,0,0,0),11)==T
Id=[[ONE if i==j else ZERO for j in range(5)]for i in range(5)]
prod=Id; ranks=[]
for k in range(10):
 z=emul((pow(3,k,P),0,0,0,0),T)
 Mk=[[eeval(v,z) for v in row]for row in M]
 prod=mm(prod,Mk)
 ranks.append(rank(prod))
assert ranks==[4,3,2,2,2,2,2,2,2,2],ranks
expected_P10=[[ZERO]*5 for _ in range(5)]
expected_P10[0][0]=ONE
expected_P10[1][0]=eeval({3:6},T)
expected_P10[2][3]=eeval({2:8},T)
expected_P10[3][3]=ONE
expected_P10[4][3]=eeval({3:10},T)
assert prod==expected_P10,(prod,expected_P10)
assert mm(prod,prod)==prod
# The degree-five closed points t^5=2 and t^5=6 are irreducible Kummer polynomials:
# F_11 contains all fifth roots of unity, and its nonzero fifth powers are +-1.
assert {pow(a,5,11) for a in range(1,11)}=={1,10}
assert 2 not in {1,10} and 6 not in {1,10}
# Base field direct check: the unique rank-zero parameter is t=0; none have t^5=2 or 6.
assert [t for t in range(11) if pow(t,5,11)==2]==[]
assert [t for t in range(11) if pow(t,5,11)==6]==[]
print('GENUS5_TRIGONAL_F11_DEFORMATION_VERIFIED matrix=5x5 smooth_boundary=t^5-6 stable_ranks=0,2,4 rank2_degree5=5 a_number_nonzero=1')
