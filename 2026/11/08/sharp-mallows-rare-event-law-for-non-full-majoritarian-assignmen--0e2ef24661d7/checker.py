"""Standalone exact-arithmetic checks of majoritarian top-cycle rare-event formulas.
Run: python checker.py. No external dependencies.
"""
from fractions import Fraction as F
from math import factorial
from itertools import permutations

def inv(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def formulas(n,q):
    a=(F(1)-q)/(F(1)-q**n) if q!=1 else F(1,n)
    b=(F(1)-q)/(F(1)-q**(n-1)) if q!=1 else F(1,n-1)
    A=factorial(n)*a**n*q**(n*(n-1)//2)
    s=sum((q**(c+h-2-2*(h>c)) for c in range(1,n+1) for h in range(1,n+1) if h!=c),F(0))
    E=A*b*b*s/2
    return A,E

def rank_data(n,q):
    d={}
    z=sum((q**inv(p) for p in permutations(range(1,n+1))),F(0))
    for p in permutations(range(1,n+1)):
        d[(p[0],p[1])]=d.get((p[0],p[1]),F(0))+q**inv(p)/z
    return d

def independent(n,q):
    d=rank_data(n,q)
    p={c:sum((v for (j,h),v in d.items() if j==c),F(0)) for c in range(1,n+1)}
    A=sum((__import__('functools').reduce(lambda x,y:x*p[y],t,F(1)) for t in permutations(range(1,n+1))),F(0))
    # For E choose two duplicate-top agents; remaining top houses bijectively cover n-2 other houses.
    E=F(0)
    for c in range(1,n+1):
      for h in range(1,n+1):
        if h==c:continue
        for t in permutations([j for j in range(1,n+1) if j not in (c,h)]):
          prod=F(1)
          for j in t:prod*=p[j]
          E+=d[(c,h)]**2*prod
    E*=n*(n-1)//2
    return A,E

def main():
  checked=0
  for n in range(3,7):
    for q in [F(1,3),F(1,2),F(2,3),F(1)]:
      a,e=formulas(n,q);aa,ee=independent(n,q)
      assert (a,e)==(aa,ee),(n,q,(a,e),(aa,ee))
      assert 0<a and 0<=e and a+e<=1
      checked+=1
  for q in [F(1,2),F(2,3),F(1,5)]:
    C=(3*q*q+2*q+1)/(q*(1+q))
    # E_n/A_n converges to (1+q^2)/(2q(1+q))
    target=(1+q*q)/(2*q*(1+q))
    errs=[]
    for n in [5,10,20,40,80]:
      a,e=formulas(n,q)
      errs.append(abs(e/a-target))
    assert all(errs[i+1]<errs[i] for i in range(len(errs)-1)),(q,errs)
    assert C==2*(1+target)
  for n in range(3,16):
    a,e=formulas(n,F(1))
    assert a==F(factorial(n),n**n)
    assert e/a==F(n,2*(n-1))
  print('PASS: 16 independent exact Mallows permutation enumerations; 15 finite-size asymptotic tests; 13 impartial-culture identities.')
if __name__=='__main__':main()
