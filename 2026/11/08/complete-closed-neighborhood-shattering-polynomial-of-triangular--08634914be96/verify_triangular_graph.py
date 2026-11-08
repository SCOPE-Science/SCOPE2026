#!/usr/bin/env python3
"""Brute-force, independent closed-neighborhood trace census for J(n,2)."""
from itertools import combinations
from math import comb

def choose(n,k): return comb(n,k) if n>=k>=0 else 0

def theorem(n):
 s1=choose(n,2) if n>=4 else 0
 s2=n*choose(n-1,2)*(n>=5)+3*choose(n,4)*(n>=6)
 s3=n*choose(n-1,3)*(n>=6)+n*choose(n-1,2)*choose(n-3,2)*(n>=7)
 s4=choose(n,2)*choose(n-2,2)*choose(n-4,2)*(n>=8)
 return (1,s1,s2,s3,s4)

def brute(n):
 vertices=list(combinations(range(n),2))
 m=len(vertices)
 contains=[]
 for edge in vertices:
  mask=0
  for ci,c in enumerate(vertices):
   if c[0] in edge or c[1] in edge: mask|=1<<ci
  contains.append(mask)
 all_bits=(1<<m)-1
 coeffs=[1,0,0,0,0]
 for k in range(1,5):
  for supp in combinations(range(m),k):
   inter=all_bits
   for idx in supp:inter &= contains[idx]
   if not inter:continue
   for target in range(1<<k):
    possible=all_bits
    for bit,idx in enumerate(supp):
     possible &= contains[idx] if (target>>bit)&1 else ~contains[idx]
     if not possible:break
    if not possible:break
   else:coeffs[k]+=1
 return tuple(coeffs)

if __name__=='__main__':
 tests=range(2,11)
 supports=0
 for n in tests:
  val=brute(n); target=theorem(n)
  assert val==target,(n,val,target)
  m=choose(n,2)
  supports+=sum(choose(m,k) for k in range(1,5))
  print('n',n,'|V|',m,'coefficients',val)
 print('ALL_TRIANGULAR_CLOSED_NEIGHBORHOOD_CHECKS_PASS',len(tests),'graphs',supports,'supports')
