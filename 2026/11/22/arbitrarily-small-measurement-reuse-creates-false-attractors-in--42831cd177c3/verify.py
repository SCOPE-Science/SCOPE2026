"""Exact checks for a screened scalar row oracle with partial independent refresh."""
from fractions import Fraction as F
from itertools import product
from math import pi

checks=0
for m in range(2,9):
    k=F(1)-F(2,2**m)
    for p in [F(0),F(1,9),F(1,3),F(1,2),F(7,8),F(1)]:
        for sign in [-1,1]:
            # Test the m candidate noise outcomes, with the smaller-residual winner.
            E=F(0); E2=F(0)
            for sample in product((-1,1), repeat=m):
                winner=sign if sign in sample else -sign
                E+=F(1,2**m)*winner
                E2+=F(1,2**m)*winner**2
            assert E==sign*k and E2==1
            checks+=2
            for s in range(1,9):
                # Conditional iid update queries have mean p*winner, variance 1-p^2.
                mean=p*E
                var=(1-p*p)/s+p*p*(E2-E*E)
                assert mean==sign*p*k
                assert var==(1-p*p)/s+p*p*(1-k*k)
                checks+=2
                if s in (1,2,4):
                    # Direct exact enumeration of the joint one-winner, s-query law.
                    got0=F(0); got1=F(0); got2=F(0)
                    for sample in product((-1,1),repeat=m):
                        w=sign if sign in sample else -sign
                        for ys in product((-1,1),repeat=s):
                            weight=F(1,2**m)
                            for y in ys:
                                weight*= (1+p)/2 if y==w else (1-p)/2
                            avg=F(sum(ys),s)
                            got0+=weight;got1+=weight*avg;got2+=weight*avg*avg
                    assert got0==1 and got1==mean and got2-mean*mean==var
                    checks+=3
assert (1-pi*pi/96) > .89
print('VERIFY_OK', checks)
