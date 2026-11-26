"""Verification of the three-round first-order theory of aperiodic Brandt semigroups.

All operations use exact finite integer tuples. No external dependencies.
"""
from itertools import product

ZERO = None

def universe(n):
    assert n >= 1
    return [ZERO] + list(product(range(n), repeat=2))

def multiply(x, y):
    if x is ZERO or y is ZERO:
        return ZERO
    return (x[0], y[1]) if x[1] == y[0] else ZERO

def atomic_signature(t):
    t = (ZERO,) + tuple(t)
    eq = tuple(x == y for x in t for y in t)
    r = tuple(multiply(x, y) == z for x in t for y in t for z in t)
    return (eq, r)

def full_rank_three_type(n):
    U = universe(n)
    triple = {t:atomic_signature(t) for t in product(U, repeat=3)}
    pair = {}
    for x,y in product(U, repeat=2):
        pair[x,y] = (atomic_signature((x,y)),
                     frozenset(triple[x,y,z] for z in U))
    single = {}
    for x in U:
        single[x] = (atomic_signature((x,)),
                     frozenset(pair[x,y] for y in U))
    return frozenset(single.values())

def normal(t):
    dictionary = {}
    ans = []
    for x in t:
        if x is ZERO:
            ans.append(ZERO)
            continue
        z=[]
        for a in x:
            if a not in dictionary:
                dictionary[a] = len(dictionary)
            z.append(dictionary[a])
        ans.append(tuple(z))
    return tuple(ans)

def pair_orbits(n):
    return {normal((x,y)) for x,y in product(universe(n), repeat=2)}

def extension_profiles(n):
    U = universe(n)
    return {t:frozenset(atomic_signature(t+(z,)) for z in U)
            for t in pair_orbits(n)}

def D(x):
    return x is not ZERO and multiply(x,x) is ZERO

def E(x):
    return x is not ZERO and multiply(x,x) == x

def Z(x,y):
    return multiply(x,y) is ZERO and multiply(y,x) is ZERO

def F(x,y,U):
    return (D(x) and D(y) and x!=y and Z(x,y)
            and all(multiply(x,z)!=y and multiply(z,x)!=y for z in U))

def H(x,y,z):
    return (E(z) and all(multiply(w,z) is ZERO and multiply(z,w) is ZERO
                         for w in (x,y)))

def thresholds(n):
    U = universe(n)
    p2 = any(D(x) for x in U)
    p3 = any(D(x) and D(y) and x!=y and Z(x,y) for x in U for y in U)
    p4 = any(F(x,y,U) for x in U for y in U)
    p5 = any(F(x,y,U) and any(H(x,y,z) for z in U) for x in U for y in U)
    return (p2,p3,p4,p5)

def verify():
    profiles={}
    for n in range(1,8):
        profiles[n]=extension_profiles(n)
        assert thresholds(n) == tuple(n>=t for t in (2,3,4,5))
        print('THRESHOLD_FORMULAS_OK n=%d flags=%s' % (n,thresholds(n)))
    for n in (5,6):
        assert profiles[n].keys() == profiles[n+1].keys()
        assert profiles[n] == profiles[n+1]
    print('PAIR_EXTENSION_STABILIZATION_OK n=5,6,7 orbit_representatives=%d' % len(profiles[5]))
    results=[]
    for n in range(1,7):
        results.append(full_rank_three_type(n))
        print('EXACT_FULL_STRUCTURE_OK n=%d size=%d type_count=%d' %
              (n,n*n+1,len(results[-1])))
    assert len(set(results)) == 5
    assert results[4] == results[5]
    print('EXACT_RANK_THREE_CLASSIFICATION_OK classes=5 representatives=1,2,3,4,5')
    print('SHARP_BRANDT_REPRESENTATIVE_OK n=5 size=26')
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
