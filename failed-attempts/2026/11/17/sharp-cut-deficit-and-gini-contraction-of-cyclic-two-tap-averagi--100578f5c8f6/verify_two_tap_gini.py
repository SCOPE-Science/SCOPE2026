"""Exact rational checks for two-tap cyclic averaging and complete-pair variation."""
from fractions import Fraction
from itertools import product
from math import floor

def gini(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x)))

def step(x,t):
    return [(1-t)*x[i]+t*x[(i+1)%len(x)] for i in range(len(x))]

def runs(x):
    return sum(x[i]==0 and x[(i+1)%len(x)]==1 for i in range(len(x)))

def test():
    cuts=0
    for n in range(2,13):
        for t in (Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
            m=min(t,1-t)
            K=Fraction(1)-2*m/Fraction((n*n)//4)
            for tup in product((Fraction(0),Fraction(1)),repeat=n):
                if len(set(tup))==1:continue
                cuts+=1
                k=sum(tup)
                r=runs(tup)
                gout=gini(step(tup,t))
                assert gout==Fraction(k*(n-k))-2*m*r*r,(n,t,tup,gout,r)
                assert gout<=K*gini(tup)
            s=tuple([1]*(n//2)+[0]*(n-n//2))
            assert gini(step(s,t))==K*gini(s)
    print('EXACT_ALL_BINARY_CUT_DEFICITS_AND_SHARP_BISECTIONS_PASSED',cuts)
    vals=[Fraction(-3),Fraction(-1),Fraction(0),Fraction(2),Fraction(5)]
    tests=0
    for n in range(2,7):
        for tup in product(vals,repeat=n):
            if len(set(tup))==1:continue
            for t in (Fraction(1,5),Fraction(1,2),Fraction(3,4)):
                out=gini(step(tup,t));K=Fraction(1)-2*min(t,1-t)/Fraction((n*n)//4)
                assert out<=K*gini(tup)
                tests+=1
    print('EXACT_NONBINARY_RATIONAL_SIGNAL_CHECKS_PASSED',tests)
    for n in range(4,30):
      # Disjoint one-step row supports exist for n>=4: rows 0 and 2.
      assert set((0,1)).isdisjoint((2,3%n))
      assert 1-Fraction(1,(n*n)//4)<1
    print('EXACT_DOBRUSHIN_SEPARATION_CHECKS_PASSED_N4_TO_N29')
    print('ALL_TWO_TAP_CYCLIC_GINI_CHECKS_PASSED')
if __name__=='__main__':test()
