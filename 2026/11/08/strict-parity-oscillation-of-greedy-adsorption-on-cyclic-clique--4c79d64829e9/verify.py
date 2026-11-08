"""Exact finite-graph independent-set checks and high-precision interval-law comparisons."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache


def greedy_expectation(m, r):
    n = m*(r-1)
    adj = [0]*n
    for i in range(m):
        clique = [i, (i+1)%m] + [m+(r-2)*i+j for j in range(r-2)]
        for a in clique:
            for b in clique:
                if a != b: adj[a] |= 1 << b
    closed = [a | (1 << i) for i, a in enumerate(adj)]
    @lru_cache(None)
    def expected(mask):
        if mask == 0: return Fraction(0)
        s, total = mask, Fraction(0)
        while s:
            bit = s & -s
            v = bit.bit_length()-1
            total += expected(mask & ~closed[v])
            s -= bit
        return 1 + total / mask.bit_count()
    return expected((1 << n)-1) / n


def J(k, lam):
    with localcontext() as ctx:
        ctx.prec = 86
        lam = Decimal(lam)
        z = Decimal(2)/lam
        term = Decimal(1)
        total = Decimal(0)
        for j in range(240):
            total += term/(lam*(k+j)-1)
            term *= z/Decimal(j+1)
        return +(total * (-z).exp())


def expected_density(m, r):
    lam=r-1
    base = (Decimal(1)-J(2,lam))/Decimal(lam)
    denom = 1
    for k in range(2,m): denom *= lam*k-1
    delta = (Decimal((-1)**(m-1)*2**(m-2))/Decimal(lam*denom))*(Decimal(1)/Decimal(lam*m)-J(m,lam))
    return base+delta,delta


def run():
    total=0
    for r in range(3,6):
        for m in range(3,7):
            if m*(r-1)>24: continue
            actual = greedy_expectation(m,r)
            predicted, correction = expected_density(m,r)
            err=abs(Decimal(actual.numerator)/Decimal(actual.denominator)-predicted)
            assert err < Decimal('1e-24'), (r,m,actual,predicted,err)
            assert (correction>0) == (m%2==1), (r,m,correction)
            total+=2
    for m in range(3,9):
        for r in range(3,10):
            _,diff=expected_density(m,r)
            assert (diff>0)==(m%2==1)
            total+=1
    print('PASS:',total,'exact-state/numerical and correction-sign assertions')

if __name__=='__main__': run()
