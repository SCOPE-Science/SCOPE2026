"""Finite exact checks of local modular Waring numbers for k=2*3**s.

No probabilistic or asymptotic assumptions; integer residues are enumerated.
"""
from math import gcd

def gamma_local(k, modulus):
    powers={pow(x,k,modulus) for x in range(modulus)}
    covered={0}
    # Each step permits a zero summand, hence covered is cumulative.
    for t in range(1,modulus+1):
        covered={(a+b)%modulus for a in covered for b in powers}
        if len(covered)==modulus:
            return t
    raise AssertionError('not generated')

checks=0
for s in range(1,5):
    k=2*3**s
    M=3**(s+1)
    for a in range(1,min(s+3,6)+1):
        n=3**a
        if n>3000: continue
        expected=n-1 if a<=s+1 else M
        actual=gamma_local(k,n)
        assert actual==expected,(s,a,expected,actual)
        print('3-adic', 's',s,'k',k,'n',n,'gamma',actual)
        checks+=1
    for a in range(1,8):
        n=2**a
        expected=n-1 if a<=3 else 8
        actual=gamma_local(k,n)
        assert actual==expected,(s,a,expected,actual)
        checks+=1
    for q in (5,7,11,13,17,19,23):
        for a in (1,2):
            n=q**a
            actual=gamma_local(k,n)
            assert actual<=k+1,(s,q,a,actual,k+1)
            checks+=1
print('ALL_PASS',checks)
