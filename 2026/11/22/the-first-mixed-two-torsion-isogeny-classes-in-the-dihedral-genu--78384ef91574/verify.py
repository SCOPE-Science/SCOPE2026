#!/usr/bin/env python3
"""Exact character sums and degree-two factor certificates for dihedral genus-two curves."""
from collections import Counter

def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def quadratic_factorization(s, p):
    # Find all monic quadratic factors of x^4+s*x^2+1 by exhaustive division.
    answer = []
    for a in range(p):
        for b in range(p):
            if b == 0:
                continue
            # (x^2+a*x+b)(x^2-a*x+d), d=b^{-1}; x coefficient a*(d-b) must vanish.
            d = pow(b, -1, p)
            if a * (d - b) % p or (b + d - a*a - s) % p:
                continue
            answer.append((a,b,(-a)%p,d))
    return answer

def torsion_count(degrees):
    perm = list(range(6))
    j = 0
    for d in degrees:
        for i in range(d):
            perm[j+i] = j + (i+1) % d
        j += d
    assert j == 6
    classes = {min(m, m ^ 63) for m in range(64) if m.bit_count() % 2 == 0}
    assert len(classes) == 16
    return sum(min(sum(1<<perm[i] for i in range(6) if (m>>i)&1),
                   (sum(1<<perm[i] for i in range(6) if (m>>i)&1))^63) == m
               for m in classes)

def compute(p):
    out = []
    for s in range(p):
        if s in (2,p-2):
            continue
        f = lambda x: (x*x + 1) * (x**4 + s*x*x + 1)
        # genus-two sextic has two rational infinity points for c=1.
        S = sum(chi(f(x),p) for x in range(p))
        n = p+2+S
        assert (p+1-n) % 2 == 0
        t = (p+1-n)//2
        # Independent count on the genus-one quotient E:y^2=(u+1)(u^2+s*u+1).
        epoints = p+1+sum(chi((u+1)*(u*u+s*u+1),p) for u in range(p))
        assert t == p+1-epoints
        roots = [x for x in range(p) if (x**4+s*x*x+1)%p == 0]
        assert len(roots) in (0,4)
        factors = quadratic_factorization(s,p)
        assert factors
        if roots:
            degrees = [1]*6
        else:
            # An exhaustive quadratic decomposition certifies degrees (2,2).
            assert any(chi(a*a-4*b,p)==-1 and chi(c*c-4*d,p)==-1
                       for a,b,c,d in factors)
            degrees = [1,1,2,2]
        j2 = torsion_count(degrees)
        assert j2 == (16 if roots else 4)
        # The non-square quadratic twist reverses the trace and retains the branch locus.
        nonsquare = next(k for k in range(1,p) if chi(k,p)==-1)
        twisted_n = p+sum(chi(nonsquare*f(x),p) for x in range(p))
        assert (p+1-twisted_n)//2 == -t
        out.append((s,t,j2,n))
    return out

def main():
    low=compute(5)
    high=compute(13)
    assert low==[(0,-2,4,10),(1,-2,4,10),(4,0,4,6)]
    target=[(0,-2,4,18),(1,-2,16,18),(3,2,4,10),
            (4,-6,4,26),(5,-6,4,26),(6,-2,4,18),
            (7,0,4,14),(8,4,4,6),(9,2,4,10),
            (10,-4,4,22),(12,2,16,10)]
    assert high==target,(high,target)
    assert sum(j==16 for _,_,j,_ in high)==2
    mixed={t for _,t,_,_ in high if any(u==t and j==16 for _,u,j,_ in high)
           and any(u==t and j==4 for _,u,j,_ in high)}
    assert mixed=={-2,2}
    assert {t for _,t,_,_ in low if any(u==t and j==16 for _,u,j,_ in low)}==set()
    # Check all 22 (s,c-square-class) marked equations: 7 Weil types, trace multiset.
    spec=Counter(t for _,t,_,_ in high)+Counter(-t for _,t,_,_ in high)
    assert dict(sorted(spec.items()))=={-6:2,-4:2,-2:6,0:2,2:6,4:2,6:2}
    # All 22 have j2 in {4,16} and exactly four marked equations have 16.
    assert sum(j==16 for _,t,j,_ in high)*2==4
    print('D4_F13_WEIL_TORSION_FIRST_PRIME_VERIFIED')
    print('p=5',low)
    print('p=13',high)
    print('22 marked traces',dict(sorted(spec.items())))
    print('mixed square-class trace bins',sorted(mixed))
if __name__=='__main__':main()
