#!/usr/bin/env python3
"""Exact independent subgroup/operation checks for two cyclic radical rings."""
from itertools import product
from math import gcd

def subgroups(p,n,m):
    modx, mody=p**n,p**m
    for a in range(n+1):
      for b in range(m+1):
        M=min(n-a,m-b)
        for c in range(M+1):
          units=[0] if c==0 else [t for t in range(1,p**c) if t%p]
          for t in units:
            # independently construct subgroup from three generating elements
            gs=[(p**(a+c)%modx,0),(0,p**(b+c)%mody),(p**a*t%modx,p**b%mody)]
            H={(0,0)}
            for (x,y) in gs:
              fresh=set(H); px,py=0,0
              for i in range(max(modx,mody)):
                if (px,py)==(0,0) and i>0: break
                for u,v in H: fresh.add(((u+px)%modx,(v+py)%mody))
                px=(px+x)%modx;py=(py+y)%mody
              H=fresh
            yield (a,b,c,t),tuple(gs),H

def theorem(p,n,m,k,l):
    sub=ide=0
    for a in range(n+1):
      for b in range(m+1):
        M=min(n-a,m-b);s=min(M,k+a,l+b)
        sub+=p**s + (p**(k+a)*max(0,M-k-a) if k+a==l+b else 0)
        ide+=p**min(M,k,l)
    return sub,ide

def test_case(p,n,m,k,l,exhaustive):
  sx,iy=0,0
  modx,mody=p**n,p**m
  seen=set()
  for param,gs,H in subgroups(p,n,m):
    fh=frozenset(H)
    assert fh not in seen, ('Goursat duplicate',p,n,m,param)
    seen.add(fh)
    def mul(x,y): return ((p**k*x[0]*y[0])%modx,(p**l*x[1]*y[1])%mody)
    # Bilinearity ensures generator product test is sufficient
    ring=all(mul(x,y) in H for x in gs for y in gs)
    if exhaustive: assert ring==all(mul(x,y) in H for x in H for y in H)
    ideal=ring and all(mul((1,0),x) in H and mul((0,1),x) in H for x in gs)
    if exhaustive: assert ideal==all(mul((1,0),x) in H and mul((0,1),x) in H for x in H)
    sx+=ring;iy+=ideal
    a,b,c,t=param
    congr=(p**(k+a)*t - p**(l+b))%(p**c)==0 if c else True
    assert ring==congr,(p,n,m,k,l,param,'subring')
    assert ideal==(ring and c<=min(k,l)),(p,n,m,k,l,param,'ideal')
  assert (sx,iy)==theorem(p,n,m,k,l),(p,n,m,k,l,sx,iy,theorem(p,n,m,k,l))
  if n>k and m>l:
    ded=(k>l and m==l+1) or (l>k and n==k+1)
    assert (sx==iy)==ded,(p,n,m,k,l,sx,iy,'Dedekind')
  return (sx,iy)

def main():
  cases=0;full=0;patterns=0
  for p,maxdim in [(2,4),(3,3)]:
    for n in range(2,maxdim+1):
      for m in range(2,maxdim+1):
        for k in range(1,n):
          for l in range(1,m):
            x=test_case(p,n,m,k,l,n<=3 and m<=3)
            cases+=1
            if n<=3 and m<=3: full+=1
            patterns+=sum(1 for _ in subgroups(p,n,m))
  # concrete contrasting adjacent parameters
  good=test_case(2,3,2,2,1,True)
  bad=test_case(2,4,3,2,1,False)
  assert good[0]==good[1] and bad[0]>bad[1]
  print(f'VERIFY_OK cases={cases} exhaustive_cases={full} subgroup_patterns={patterns} example_good={good} example_bad={bad}')
if __name__=='__main__': main()
