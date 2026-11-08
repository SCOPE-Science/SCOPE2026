"""Exact cyclotomic tests for residue-perturbed cubic moment curves.

The character-sum algorithm below is independent of the stationary-phase
formula: it forms each exponent histogram and reduces it modulo the exact
prime-square cyclotomic polynomial using integer arithmetic.
"""
from itertools import product
import random


def rootless(p, u, v, w):
    return not any((u + 2*v*r + 3*w*r*r) % p == 0 for r in range(p))


def expected_zero(p, u, v, w):
    a, b, c = u % p, v % p, w % p
    if (a, b, c) != (0, 0, 0):
        return rootless(p, a, b, c)
    uu, vv, ww = u // p, v // p, w // p
    return len({(uu*r + vv*r*r + ww*r*r*r) % p for r in range(p)}) == p


def theoretical_nullity(p):
    if p == 2: return 20
    if p == 3: return 168
    nrootless = (p-1) + p*(p-1)**2//2
    perm = (p-1)*(1+p*(p % 3 == 2))
    return p**3*nrootless+perm


def curve(p, hs):
    h1,h2,h3 = hs
    mod = p*p
    return [((x+p*h1[x%p])%mod,
             (x*x+p*h2[x%p])%mod,
             (x*x*x+p*h3[x%p])%mod) for x in range(mod)]


def direct_cyclotomic_zero(p, pts, u, v, w):
    m = p*p
    counts = [0]*m
    for a, b, c in pts:
        counts[(u*a+v*b+w*c)%m] += 1
    # Phi_(p^2)(z) = 1+z^p+...+z^((p-1)p).
    # Degree <p^2 divisibility is equivalently constant counts
    # along every arithmetic progression r, r+p, ..., r+(p-1)p.
    return all(len({counts[r+p*k] for k in range(p)})==1 for r in range(p))


def verify_case(p, hs, exhaustive):
    pts = curve(p, hs)
    assert len(set(pts)) == p*p
    rng = range(p*p)
    checks = product(rng,repeat=3) if exhaustive else (
        tuple(random.randrange(p*p) for _ in range(3)) for _ in range(2000))
    z = 0
    n = 0
    for u,v,w in checks:
        lhs = direct_cyclotomic_zero(p,pts,u,v,w)
        rhs = expected_zero(p,u,v,w)
        assert lhs == rhs, (p, hs, u,v,w, lhs,rhs)
        z += lhs;n+=1
    if exhaustive:
        assert z == theoretical_nullity(p),(p,hs,z,theoretical_nullity(p))
    print('EXACT_CYCLOTOMIC_OK',p,'deformation',','.join(str(sum(h)) for h in hs),
          'frequencies',n,'zeros',z if exhaustive else 'sampled')


def main():
    random.seed(20261101)
    for p in (2,3,5,7,11,13):
        # Indep. count of primitive derivative rootless triples and permutation cubics.
        nrootless = sum(rootless(p,*abc) for abc in product(range(p),repeat=3)
                        if abc != (0,0,0))
        np = sum(len({(u*r+v*r*r+w*r*r*r)%p for r in range(p)})==p
                 for u,v,w in product(range(p),repeat=3))
        assert p**3*nrootless+np == theoretical_nullity(p)
        print('RESIDUE_CENSUS_OK',p,'rootless',nrootless,'permutation',np,
              'nullity',theoretical_nullity(p))
    for p in (2,3):
        allh = list(product(range(p),repeat=p))
        cases = ([([0]*p,[0]*p,[0]*p)] +
                 [tuple(map(list, triple)) for triple in product(allh,repeat=3)] if p==2
                 else [[list(a) for a in triple] for triple in (
                      (allh[0],allh[0],allh[0]),
                      (allh[1],allh[3],allh[5]),
                      (allh[-1],allh[13],allh[7]))])
        for hs in cases:verify_case(p,hs,True)
    for p in (5,7):
        zs=[0]*p
        verify_case(p,(zs,zs,zs),True)
        if p==5:
            hs=([r*r%p for r in range(p)], [3*r+1 for r in range(p)],
                [(r*r*r+1)%p for r in range(p)])
            verify_case(p,hs,True)
    for p in (7,11):
        for _ in range(3):
            hs=tuple([random.randrange(p) for i in range(p)] for j in range(3))
            verify_case(p,hs,False)
    print('ALL_EXACT_CUBIC_MOMENT_CHECKS_OK')

if __name__=='__main__':main()
