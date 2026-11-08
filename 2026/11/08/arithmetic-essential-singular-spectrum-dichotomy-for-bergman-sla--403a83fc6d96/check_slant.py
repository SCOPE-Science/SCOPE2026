#!/usr/bin/env python3
"""Finite exact tests of monomial slant-coordinate product relations."""
checks=0

def verify(condition,msg):
 global checks
 assert condition,msg
 checks+=1

def u(k,r,j):
 return (j+r)//k if (j+r)%k==0 else None

def compose(k,m,n,j):
 t=u(k,n,j)
 return u(k,m,t) if t is not None else None

for k in range(2,11):
 for m in range(0,27):
  for n in range(0,27):
   if m==n: continue
   res_a=(-n-k*m)%(k*k)
   res_b=(-m-k*n)%(k*k)
   verify((res_a==res_b)==((m-n)%(k*k)==0),"residue equivalence")
   for j in range(0,72):
    a=compose(k,m,n,j)
    b=compose(k,n,m,j)
    verify((a is not None)==((j+n+k*m)%(k*k)==0),"first product support")
    verify((b is not None)==((j+m+k*n)%(k*k)==0),"second product support")
    if a is not None: verify(k*k*a==j+n+k*m,"first product coordinate")
    if b is not None: verify(k*k*b==j+m+k*n,"second product coordinate")
    if a is not None and b is not None:
     verify(a-b==(k-1)*(m-n)//(k*k),"equal-residue output translation")
print('SLANT_RESIDUE_EXACT_FINITE_OK',checks)
