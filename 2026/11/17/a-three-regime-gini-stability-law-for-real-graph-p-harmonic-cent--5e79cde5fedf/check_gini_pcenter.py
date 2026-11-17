"""Finite exact and numerical checks for the Gini stability of real p-centers."""
from fractions import Fraction
from itertools import combinations
from math import isclose
from scipy.optimize import brentq
import random

def gini(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x)))

def cut_norm(weights):
    n=len(weights)
    best=Fraction(0)
    for k in range(1,n):
        for ids in combinations(range(n),k):
            c=sum((weights[i] for i in ids), Fraction(0))
            h=k*(1-c)+(n-k)*c
            best=max(best,Fraction(1)+h/Fraction(k*(n-k)))
    return best

def center(p,a):
    lo,hi=min(a),max(a)
    if hi==lo:return lo
    def f(c):return sum((abs(c-v)**(p-1) if c>v else -abs(c-v)**(p-1)) for v in a)
    return brentq(f,lo,hi,xtol=1e-15)

for n in range(2,12):
    w_uniform=[Fraction(1,n)]*n
    assert cut_norm(w_uniform)==Fraction(1)+Fraction(2,n)
    w_extreme=[Fraction(1,2),Fraction(1,2)]+[Fraction(0)]*(n-2)
    assert cut_norm(w_extreme)==Fraction(1)+Fraction(n,2*(n-1))
    # All explicitly enumerated probability weights on the 1/6 grid with max <=1/2.
    if n<=5:
      def comp(total,parts):
        if parts==1:
          yield (total,)
          return
        for i in range(total+1):
          for tail in comp(total-i,parts-1):yield (i,)+tail
      for ints in comp(6,n):
        if max(ints)<=3:
          ws=[Fraction(k,6) for k in ints]
          assert cut_norm(ws)<=Fraction(1)+Fraction(n,2*(n-1))
print('EXACT_COMPLETE_CUT_NORM_FORMULAS_AND_CAPPED_WEIGHTS_PASS')

random.seed(1729)
for n in range(3,9):
    for p in (1.25,1.6,2.,2.5,3.,4.,8.):
        cap=2 if p<2 else (1+2/n if p==2 else 1+n/(2*(n-1)))
        for _ in range(100):
            a=[random.uniform(-3,3) for i in range(n)]
            b=[random.uniform(-3,3) for i in range(n)]
            ca,cb=center(p,a),center(p,b)
            observed=(gini([ai-bi for ai,bi in zip(a,b)]+[ca-cb])/gini([ai-bi for ai,bi in zip(a,b)]))
            assert observed<cap+1e-8,(n,p,observed,cap)
print('NONLINEAR_RANDOM_TWO_INPUT_GINI_UPPER_BOUNDS_PASS')

for n in range(3,11):
    for p in (2.2,3.,5.):
        # At (1,-1,0,...,0), the exact derivative of the p-center
        # places equal mass on the two nonzero residuals for every p>2.
        ws=[Fraction(1,2),Fraction(1,2)]+[Fraction(0)]*(n-2)
        assert cut_norm(ws)==Fraction(1)+Fraction(n,2*(n-1))
    for p in (1.25,1.5,1.8):
        t=(n-2)**(-1/(p-1))
        a=[0.,1.]+[-t]*(n-2)
        b=a.copy();b[0]+=1e-8
        q=gini([ai-bi for ai,bi in zip(a,b)]+[center(p,a)-center(p,b)])/gini([ai-bi for ai,bi in zip(a,b)])
        assert q>1.8,(n,p,q)
print('THREE_REGIME_SHARP_WITNESS_CHECKS_PASS')
print('ALL_P_CENTER_GINI_CHECKS_PASS')
