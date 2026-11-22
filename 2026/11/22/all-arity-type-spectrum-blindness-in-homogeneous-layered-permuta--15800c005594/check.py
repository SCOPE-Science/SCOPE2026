#!/usr/bin/env python3
"""Exact independent brute-force verification of extension-type enumerator for finite layered permutations."""
from itertools import permutations,product,combinations
from math import factorial,comb
from fractions import Fraction

def expected(parts,r):
 n=sum(parts);k=len(parts)
 a=n-1;b=k+1
 # [z^r](1-z)^(-a)*(1-2z)^(-b), with a=0 allowed
 return factorial(r)*sum((comb(a+i-1,i) if a else int(i==0))*comb(b+r-i-1,r-i)*2**(r-i) for i in range(r+1))

def brute(parts,r):
 n=sum(parts);m=n+r;total=0
 old_structure=[]
 for ix,p in enumerate(parts):old_structure.extend([ix]*p)
 for word in permutations(range(m)):
  if tuple(x for x in word if x<n)!=tuple(range(n)):continue
  for cuts in product((0,1),repeat=m-1):
   block=[0]
   for flag in cuts:block.append(block[-1]+flag)
   old=[block[i] for i,x in enumerate(word) if x<n]
   old_compress=[0]
   for i in range(1,n):old_compress.append(old_compress[-1]+(old[i]!=old[i-1]))
   if old_compress==old_structure:total+=1
 return total

def popularity(parts,r):
    # Independently count occurrences of the old pattern inside each canonical
    # layered permutation with n+r (unlabeled) positions; label the complement.
    n=sum(parts);m=n+r
    total=0
    for cuts in product((0,1),repeat=m-1):
        block=[0]
        for c in cuts:block.append(block[-1]+c)
        for idx in combinations(range(m),n):
            observed=[0]
            for j in range(1,n):observed.append(observed[-1]+(block[idx[j]]!=block[idx[j-1]]))
            expected=[]
            for j,a in enumerate(parts):expected.extend([j]*a)
            if observed==expected:total+=1
    return factorial(r)*total

if __name__=='__main__':
 cases=[]
 for n in range(1,5):
  for mask in range(1<<(n-1)):
   parts=[1]
   for i in range(n-1):
    if mask>>i&1:parts.append(1)
    else:parts[-1]+=1
   for r in range(4 if n<3 else 3):
    if n+r>6:continue
    ans=brute(parts,r);pred=expected(parts,r)
    assert ans==pred,(parts,r,ans,pred)
    assert popularity(parts,r)==pred,(parts,r,popularity(parts,r),pred)
    cases.append((parts,r,ans))
 print('VERIFIED_CASES',len(cases),'THREE_METHOD_AGREEMENT')
 print('N3_K2',[(p,r,v) for p,r,v in cases if p in ([1,2],[2,1]) and r==2])
 print('T1_T2_N2K2', expected([1,1],1),expected([1,1],2))
 print('T1_T2_N4K1', expected([4],1),expected([4],2))
 print('CHECK_OK')
