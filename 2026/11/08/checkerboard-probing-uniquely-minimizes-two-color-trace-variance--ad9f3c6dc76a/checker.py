"""Exact-rational finite checks of cyclic Green kernels and two-color probing.
These tests illustrate, but do not replace, the proof for all even dimensions.
"""
from fractions import Fraction as F
from itertools import product


def green(n, r):
    c = r / ((1-r*r)*(1-r**n))
    return [c*(r**d + r**(n-d)) for d in range(n)]


def variance(n, g, signs):
    return sum(4*g[(j-i)%n]**2 for i in range(n)
               for j in range(i+1,n) if signs[i] == signs[j])


def variance_alt(n, g):
    return 2*n*sum(g[d]**2 for d in range(2,n,2))


def variance_formula(n,r):
    c = r / ((1-r*r)*(1-r**n))
    m = n//2
    return 4*n*c*c*(r**4*(1-r**(2*n-4))/(1-r**4)+(m-1)*r**n)

count = 0
for n in (4,6,8,10,12):
    for r in (F(1,5),F(1,2),F(4,5)):
        g=green(n,r); mu=(1-r)**2/r
        # The exact circulant Green kernel inverts the SPD screened cycle.
        for i in range(n):
            for j in range(n):
                val=(mu+2)*g[(i-j)%n]-g[(i-j-1)%n]-g[(i-j+1)%n]
                assert val==int(i==j)
                count+=1
        a=tuple((-1)**j for j in range(n))
        va=variance(n,g,a)
        assert va==variance_alt(n,g)==variance_formula(n,r)
        count+=2
        # Same two linear solves: patterned probes versus two ordinary probes.
        v2=n*sum(g[d]**2 for d in range(1,n))
        assert 0<va<v2
        count+=1
        # The alternating partition, and only its global sign reversal, minimize.
        for s in product((-1,1),repeat=n):
            vv=variance(n,g,s)
            assert vv>=va
            assert (vv==va) == (s==a or s==tuple(-x for x in a))
            count+=2
print(f'PASS {count} exact-rational assertions: n=4,6,8,10,12 and r=1/5,1/2,4/5')
