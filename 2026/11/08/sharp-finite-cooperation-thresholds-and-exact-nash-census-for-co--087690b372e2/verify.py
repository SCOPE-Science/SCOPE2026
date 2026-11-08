#!/usr/bin/env python3
"""Direct-payoff exhaustive exact-arithmetic checks for a pair-and-triple game."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb

S=F(-1,2); T=F(3,2); G=F(5,2); W=F(0)

def advantages(n,weight,j):
    L=n-1
    return -F(L,2)+weight*(3*j*(L-j)-F(L*(L-1),4))

def actual_payoff(profile,player,action,weight):
    others=[profile[v] for v in range(len(profile)) if v!=player]
    val=F(0)
    for v in others:
        if action: val += 1 if v else S
        else: val += T if v else 0
    for u,v in combinations(others,2):
        if action:
            val += weight * ((1 if u+v==2 else G) if u+v>=1 else S)
        else:
            val += weight * (T if u+v==2 else (W if u+v==1 else 0))
    return val

def pure(profile,weight):
    return all(actual_payoff(profile,i,profile[i],weight)>=actual_payoff(profile,i,1-profile[i],weight)
               for i in range(len(profile)))

def predicted(n,weight,k):
    if k==0: return True
    if k==n: return False
    return advantages(n,weight,k-1)>=0 and advantages(n,weight,k)<=0

def critical(n):
    L=n-1; M=3*(L*L//4)-F(L*(L-1),4)
    return F(L,2*M)

def count_formula(n,weight):
    return 1+sum(comb(n,k) for k in range(1,n) if predicted(n,weight,k))

tests=0
for n in range(3,9):
    c=critical(n)
    weights={F(0),F(1,20),F(1,10),F(1,5),F(1,3),F(1,2),F(1),F(2),F(7),c,c/2,c*F(99,100),c*F(101,100),c*2}
    for weight in sorted(weights):
        count=0
        for p in product((0,1),repeat=n):
            count += pure(p,weight)
            assert pure(p,weight)==predicted(n,weight,sum(p)),(n,weight,p)
            for i in range(n):
                j=sum(p)-p[i]
                assert actual_payoff(p,i,1,weight)-actual_payoff(p,i,0,weight)==advantages(n,weight,j)
                tests+=1
        assert count==count_formula(n,weight),(n,weight,count)
        assert count_formula(n,c)==(1+comb(n,(n+1)//2) if n%2 else 1+comb(n,n//2)+comb(n,n//2+1))
        assert count_formula(n,c*F(99,100))==1
for n in range(3,40):
    L=n-1; crit=critical(n)
    assert (advances := max(advantages(n,crit,j) for j in range(L+1)))==0
    assert all(advantages(n,crit*F(999,1000),j)<0 for j in range(L+1))
    if n>=13:
        assert advantages(n,F(0),L-1)<0
        assert advantages(n,F(100000),L-1)<0
    else:
        t=F(2*L,(L-1)*(12-L))
        assert predicted(n,t,n-1)
        assert not predicted(n,t*F(99,100),n-1)
print('VERIFY_OK',tests,'exact payoff-advantage comparisons; n=3..39 threshold and one-defector checks')
