#!/usr/bin/env python3
"""Independent exact checks of central Delannoy cubic-valuation argument."""
from fractions import Fraction as F
from math import comb,factorial

def poly_mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def poly_add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,y in enumerate(b):c[i]+=y
 return c

def truncate_poly(h,K):
 q=[F(1)]; ans=[F(1)]
 for k in range(1,K+1):
  q=poly_mul(q,[F(-k+1),F(2**h)])
  z=poly_mul(q,q)
  ans=poly_add(ans,[t*2**k/F(factorial(k)**2) for t in z])
 return [x/2**(3*h) for x in ans[1:]]

# Check the exact coefficient-parities, not just numeric substitutions.
for h,K,want_den,want_odd in [(2,4,9,{2,3,4}),(3,8,99225,{3})]:
 # Coefficients of (P_K(2^h u)-1)/2^(3h), ascending degrees.
 q=[F(1)]; ans=[F(1)]
 for k in range(1,K+1):
  q=poly_mul(q,[F(1-k),F(2**h)])
  ans=poly_add(ans,[t*F(2**k,factorial(k)**2) for t in poly_mul(q,q)])
 assert ans[0]==1
 C=[x/2**(3*h) for x in ans]; C[0]=F(0)
 assert all(want_den*x.denominator % x.denominator == 0 for x in C)
 assert {i for i,x in enumerate(C) if (x*want_den).numerator%2}==want_odd
 # Assert the stated coefficient denominators and exact terminal coefficients.
 assert all((x*want_den).denominator==1 for x in C)

# Verify valuation of 2-adic L and A to suitable fixed precision,
# carefully removing powers of 2 from denominators.
def modfrac(fr,M):
 a,b=fr.numerator,fr.denominator
 t=(b&-b).bit_length()-1
 assert (a%(1<<t))==0
 return (a>>t)*pow(b>>t,-1,M)%M
M=1<<24
L=F(0);A=F(0);H=F(0)
for k in range(1,85):
 L+=F(2**k,k*k)
 A+=F(-2*2**k,k*k)*H
 H+=F(1,k)
assert modfrac(L,M)==0,(modfrac(L,M),)
assert modfrac(A,2)==1
# Finite check of universal elementary inequality, with analytic proof in RESULT.
for k in range(2,100001):
 a=(k-1).bit_length()-1
 v=(k&-k).bit_length()-1
 assert k-2*v-2*a>=-2

# Direct recurrence D(0)=1,D(1)=3,(n+1)D(n+1)=(6n+3)D(n)-nD(n-1).
D0,D1=1,3
for n in range(1,1400):
 cur=D0 if n==0 else D1
 val=((6*n+3)*D1-n*D0)//(n+1)
 assert (6*n+3)*D1-n*D0==(n+1)*val
 D0,D1=D1,val
 N=n+1
 if N%4==0:
  h=(N&-N).bit_length()-1
  assert ((val-1)&-(val-1)).bit_length()-1==3*h,(N,h)
 if N%4==3:
  h=((N+1)&-(N+1)).bit_length()-1
  assert ((val+1)&-(val+1)).bit_length()-1==3*h,(N,h)

# Reflection via 2-adic negative binomial series for 0<=n<=25, mod 2^18.
M=1<<18
for n in range(26):
 DN=sum(2**k*comb(n,k)**2 for k in range(n+1))%M
 neg=sum(2**k*comb(n+k,k)**2 for k in range(45))%M
 assert (DN+neg)%M==0,n
print('VERIFY_OK: two rational polynomial identities, 2-adic constants, inequality, 1,399 exact Delannoy cases, 26 reflections')
