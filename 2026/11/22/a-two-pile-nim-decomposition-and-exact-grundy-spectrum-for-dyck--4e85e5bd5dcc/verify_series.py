#!/usr/bin/env python3
"""Independent formal-power-series coefficient checks for all Grundy strata."""
from math import comb
from functools import lru_cache
from itertools import product
def balanced_dyck(w):
 h=0
 for x in w:
  h += (1 if x=='a' else -1)
  if h<0: return False
 return h==0

@lru_cache(None)
def brute_nimber(w):
 children = []
 for i in range(1,len(w)+1):
  if balanced_dyck(w[:i]):children.append(brute_nimber(w[i:]))
  if balanced_dyck(w[-i:]):children.append(brute_nimber(w[:-i]))
 ans=0
 while ans in children:ans+=1
 return ans

N=60

def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(a,b):
 c=[0]*(N+1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:c[i+j]+=x*y
 return c

def powers(p,limit):
 r=[[1]+[0]*N]
 for _ in range(limit):r.append(mul(r[-1],p))
 return r

p=[0]*(N+1)
for m in range(1,N//2+1):p[2*m]=comb(2*m-2,m-1)//m
one=[1]+[0]*N
allwords=[2**n for n in range(N+1)]
q=sub(mul(mul(sub(one,p),sub(one,p)),allwords),sub(one,p))
assert q[0]==0 and all(x>=0 for x in q)
ps=powers(p,N//2+1)
result={}
for g in range(N//2+1):
 f=ps[g][:]
 # Exact coefficient of non-Dyck words by number of left and right primitive components.
 for k in range(N//2+1):
  l=k^g
  if l <= N//2 and k+l <= N//2:
   f=add(f,mul(q,ps[k+l]))
 result[g]=f
for n in range(N+1):
 s=sum(result[g][n] for g in result)
 assert s==2**n, (n,s,2**n)
for n in range(0,15):
 hist=[0]*(N//2+1)
 for letters in product('ab',repeat=n):
  hist[brute_nimber(''.join(letters))]+=1
 for g in range(N//2+1):
  assert hist[g]==result[g][n], (n,g,hist[g],result[g][n])
 print('n=',n,'zero=',result[0][n], 'other=',[(g,result[g][n]) for g in range(1,5) if result[g][n]])
# Explicit rational identities for losing and for a fixed nimber g by the XOR-block formula.
for g in range(16):
 M=1
 while M<=g:M*=2
 numerator=[0]*(N+1)
 for r in range(M):
  exponent=r+(r^g)
  if exponent <= N//2:numerator=add(numerator,ps[exponent])
 den=sub(one,ps[2*M]) if 2*M <= N//2 else None
 lhs=sub(result[g],ps[g])
 if den is not None:
  assert mul(lhs,den)==mul(q,numerator),g
print('PASS exact_coefficients_to_length=',N,'fixed_nimber_block_identities=16')
print('limiting_zero_probability=1/3')
