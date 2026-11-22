"""Exact rational checks of moment identifiability and four-strain examples.

Run using Python 3: python verify.py
All equalities are exact (fractions.Fraction). The general theorem is proved
in RESULT.md; these enumerations are independent finite sanity checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def subsets(n):
    return range(1 << n)


def p_t(t):
    assert F(0) <= t <= F(1,4)
    return {mask: (t if mask.bit_count() % 2 else F(1,4)-t) for mask in subsets(3)}


def moment(p, mask):
    return sum((v for bits,v in p.items() if bits & mask == mask), F(0))


def susceptibility(p, c):
    return sum((v*c**bits.bit_count() for bits,v in p.items()), F(0))


def kernel_coefficients(sigma, n):
    return {a: sum(((-1)**(a.bit_count()-b.bit_count()))*sigma[b]
                   for b in subsets(n) if b & a == b)
            for a in subsets(n)}


def run():
    checks = 0
    for c in (F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)):
        for k in range(17):
            t=F(k,64)
            p=p_t(t)
            assert sum(p.values())==1
            checks+=1
            for mask in subsets(3):
                if mask.bit_count()<=2:
                    assert moment(p,mask)==F(1,2**mask.bit_count())
                    checks+=1
            expected=(1+3*c*c)/4 + t*(c-1)**3
            assert susceptibility(p,c)==expected
            checks+=1
        assert susceptibility(p_t(F(0)),c)-susceptibility(p_t(F(1,4)),c)==(1-c)**3/4
        checks+=1
    c=F(1,2)
    low=p_t(F(1,16)); high=p_t(F(3,16))
    assert all(v>0 for v in low.values()) and all(v>0 for v in high.values())
    assert susceptibility(low,c)==F(55,128)
    assert susceptibility(high,c)==F(53,128)
    s=F(63,64); beta=F(4096,1701); removal=F(1)
    assert beta*s*susceptibility(low,c)-removal==F(1,54)
    assert beta*s*susceptibility(high,c)-removal==-F(1,54)
    checks+=6
    for m in range(1,8):
        for c in (F(1,2), F(2,3)):
            sigma={mask:c**mask.bit_count() for mask in subsets(m)}
            coeff=kernel_coefficients(sigma,m)
            for a,v in coeff.items():
                assert v==(c-1)**a.bit_count()
                checks+=1
            for mask in subsets(m):
                assert sum((coeff[a] for a in subsets(m) if (a&mask)==a),F(0))==sigma[mask]
                checks+=1
    # Parity moment trade on all active sets A, including proper non-initial segments.
    for m in range(1,7):
        for a in subsets(m):
            r=a.bit_count()
            if r==0: continue
            even={bits:F(1,2**(r-1)) for bits in subsets(m) if bits&a==bits and bits.bit_count()%2==0}
            odd={bits:F(1,2**(r-1)) for bits in subsets(m) if bits&a==bits and bits.bit_count()%2==1}
            assert sum(even.values())==sum(odd.values())==1
            checks+=1
            for b in subsets(m):
                if b.bit_count()<r:
                    assert moment(even,b)==moment(odd,b)
                    checks+=1
    print('PASS: exact rational checks:',checks)
    c=F(1,2)
    print('Sharp H interval at c=1/2:',susceptibility(p_t(F(1,4)),c),susceptibility(p_t(F(0)),c))
    print('Positive-compartment initial growth rates:',F(1,54),-F(1,54))


if __name__=='__main__':run()
