"""Independent modular-power cross-check for the quartic four-word spectrum.
No primitive roots, discrete logs, third-party imports, or precomputed coset tables.
"""
from math import isqrt

def isprime(n):
    if n < 2: return False
    for d in range(2,isqrt(n)+1):
        if n%d == 0:return False
    return True

def coverage(p):
    assert isprime(p) and p%4 == 1
    c = [-1]*p
    H = {pow(x,4,p) for x in range(1,p)}
    q = next(x for x in range(2,p) if pow(x,(p-1)//2,p) == p-1)
    for k in range(4):
        coef=pow(q,k,p)
        for h in H:
            a=coef*h%p
            assert c[a]==-1
            c[a]=k
    assert sorted(c[1:])==[i for i in range(4) for _ in range((p-1)//4)]
    return {64*c[n]+16*c[n+1]+4*c[n+2]+c[n+3] for n in range(1,p-3)}

if __name__=='__main__':
    P=[p for p in range(5,4001) if p%4==1 and isprime(p)]
    bad=[p for p in P if len(coverage(p))!=256]
    assert bad[-1] == 3361 and len(bad)==144
    assert 195 not in coverage(3361) and len(coverage(3361))==255
    assert 0 in coverage(3361) and 0 not in coverage(2689)
    assert len(coverage(3373))==256
    for p in (5009, 10009, 65537, 131101, 262657):
        if isprime(p) and p%4==1:
            assert len(coverage(p))==256
    print(f'INDEPENDENT_OK primes_through_4000={len(P)} failures={len(bad)} last_failure={bad[-1]} last_zero_failure=2689')
