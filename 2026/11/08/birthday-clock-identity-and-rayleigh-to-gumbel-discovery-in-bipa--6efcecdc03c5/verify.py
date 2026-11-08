"""Exact finite checks for sequential bipartite internal DLA class-completion law.

Python 3 standard library only. This file does not attempt infinite certification.
"""
from fractions import Fraction as Q
from math import comb


def product_cdf(a, b, j):
    assert a >= 2 and b >= 1 and 0 <= j <= b
    if j == b:
        return Q(1)
    value = Q(0)
    for k in range(a):
        z = Q(a-k, a)
        term = Q(1)
        for r in range(j+1):
            term *= Q(b-r, 1) / (b-z*r)
        value += (-1)**k * comb(a-1, k) * term
    return value


def independent_state_cdf(a, b):
    """First-discovery kernel derived directly from the two-sided walk."""
    states = {(1, 0): Q(1)}
    first_hit = [Q(0)]*(b+1)
    for j in range(b+1):
        for i in range(1, a+1):
            p = states.get((i, j), Q(0))
            if i == a or j == b:
                first_hit[j] += p
                continue
            d = a*b-i*j
            p_b = Q(a*(b-j), d)
            p_a = Q(j*(a-i), d)
            assert p_a+p_b == 1
            states[(i, j+1)] = states.get((i, j+1), Q(0))+p*p_b
            states[(i+1, j)] = states.get((i+1, j), Q(0))+p*p_a
    out, s = [], Q(0)
    for z in first_hit:
        s += z
        out.append(s)
    return out


def run():
    checks=0
    for a in range(2,9):
        for b in range(1,17):
            direct=independent_state_cdf(a,b)
            previous=Q(0)
            for j in range(b+1):
                q=product_cdf(a,b,j)
                assert q==direct[j], (a,b,j,q,direct[j])
                assert previous<=q<=1
                if j<b:
                    # An individual remaining A vertex is unseen if every
                    # collision label avoids it.
                    single=Q(1)
                    for r in range(j+1):
                        single*=Q(b-r,1)/(b-Q(a-1,a)*r)
                    assert 1-q <= (a-1)*single
                previous=q
                checks+=1
            assert direct[-1] == Q(1)
            checks+=1
    # Cross-check the geometric failure mean and variance at small r/b.
    for b in range(2,19):
        for r in range(b):
            # F is failures before a success, with P(F>=n)=(r/b)^n.
            p=Q(r,b)
            assert p/(1-p) == Q(r,b-r)
            assert p/(1-p)**2 == Q(r*b,(b-r)**2)
            checks+=2
    print('VERIFY_OK', checks, 'exact assertions')

if __name__=='__main__':
    run()
