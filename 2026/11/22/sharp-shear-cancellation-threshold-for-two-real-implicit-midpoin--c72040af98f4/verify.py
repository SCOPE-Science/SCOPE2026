"""Reproducible finite and exact-algebra checks for a two-Cayley Jordan shear.

This verifier supplies examples and rational certificate checks; the global
quantifier is established by the accompanying symbolic proof, not this grid.
"""
from fractions import Fraction as F
from math import sqrt
import random


def direct(x, beta, y):
    d = (1 - x + y) / (1 + x + y)
    v = 2 * beta * x * (1 - y) / (1 + x + y)**2
    return d, v


def opnorm(d, v):
    return (sqrt(4 * float(d)**2 + float(v)**2) + abs(float(v))) / 2


def check():
    count = 0
    # Exact rational identities for the Cayley product and the threshold.
    for x in [F(21, 10), F(5, 2), F(3), F(4), F(7), F(10)]:
        q = (x - 2) / (x + 2)
        ymax = x*x/4
        for j in range(101):
            y = ymax*F(j,100)
            d, v = direct(x,F(3),y)
            assert (1+x+y)*d == 1-x+y
            assert (1+x+y)**2*v == 6*x*(1-y)
            # The squared-distance certificate is polynomial/rational exact.
            lhs = (q*q - d*d)*(x+2)**2*(1+x+y)**2
            rhs = 4*x*(y-1)*(x*x-2*y-2)
            assert lhs == rhs
            if y>1:
                threshold = 2*(x*x-2*y-2)/(x*x-4)
                assert F(1) <= threshold < 2
                assert abs(v) >= q - d*d/q
            elif y<1:
                assert d < -q
            else:
                assert d == -q and v == 0
            assert opnorm(d,v) >= float(q)-1e-12
            count += 1
    # Threshold necessity: below beta=2 the unique shear-canceling
    # candidate y=1 is strictly improvable by a nearby feasible y>1.
    for x in [F(5,2),F(3),F(4),F(8)]:
        for beta in [F(0),F(1,2),F(1),F(3,2),F(199,100)]:
            ymax=x*x/4
            delta=min((ymax-1)/1000,(2-beta)*(x*x-4)/100)
            y=1+delta
            threshold=2*(x*x-2*y-2)/(x*x-4)
            assert beta < threshold
            d,v=direct(x,beta,y)
            assert opnorm(d,v) < float((x-2)/(x+2))
            count += 1
    # The strict global uniqueness check for representative continuous
    # parameters, with no claim that the grid proves infinitely many cases.
    random.seed(23058)
    for _ in range(5000):
        x = 2+10**random.uniform(-2,2)
        beta = 2+20*random.random()
        y=x*x*random.random()/4
        d,v=direct(x,beta,y)
        q=(x-2)/(x+2)
        assert opnorm(d,v)>=q-2e-12
        count += 1
    # Independently assemble matrix products for a=1, s=3, H=6.
    a,s,H=1,3,6
    h1,h2=3-sqrt(5),3+sqrt(5)
    def single(h):
        t=a*h/2
        return ((1-t)/(1+t), h*s/(1+t)**2)
    def compound(h1,h2):
        u,v=single(h1),single(h2)
        return u[0]*v[0],u[0]*v[1]+u[1]*v[0]
    z=compound(h1,h2)
    eq=compound(3,3)
    one=compound(0,6)
    assert abs(z[0]+.2)<1e-12 and abs(z[1])<1e-12
    assert abs(opnorm(*eq)-.5787645095261801)<1e-12
    assert abs(opnorm(*one)-1.3150996611745185)<1e-12
    print('CHECKS_OK',count,'optimal_norm',opnorm(*z), 'equal_norm',opnorm(*eq), 'single_norm',opnorm(*one))

if __name__=='__main__':
    check()
