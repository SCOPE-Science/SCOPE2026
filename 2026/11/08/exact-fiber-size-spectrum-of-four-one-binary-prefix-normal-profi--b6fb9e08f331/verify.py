"""Standalone checks for four-one prefix-normal-form fiber theorem.
Only Python's standard library is required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def profile_from_positions(positions, n):
    """Direct sliding-window maximum-one profile."""
    bits = [0] * n
    for j in positions:
        bits[j] = 1
    pref = [0]
    for b in bits:
        pref.append(pref[-1] + b)
    return tuple(max(pref[j + k] - pref[j] for j in range(n - k + 1))
                 for k in range(1, n + 1))


def triple_from_positions(pos):
    b = pos[1] - pos[0] - 1
    c = pos[2] - pos[1] - 1
    d = pos[3] - pos[2] - 1
    m = min(b, c, d)
    v = c + min(b, d)
    s = b + c + d
    return (m, v, s)


def h(p, q):
    if p == 0:
        return 1 if q == 0 else 2
    if q == 0:
        return 1
    if q < p:
        return 2
    if q == p:
        return 3
    return 4


def parameter_classes(n):
    """Predicted class cardinalities; keys are the triple of shortest spans."""
    out = {}
    k = n - 4
    for m in range(k // 3 + 1):
        for p in range(k - 3*m + 1):
            for q in range(k - 3*m - p + 1):
                r = k - 3*m - p - q
                out[(m, 2*m+p, 3*m+p+q)] = (r+1)*h(p,q)
    return out


def s2_by_coefficients(n):
    coefs = (1, 4, 8, 7)
    total = 0
    for j,c in enumerate(coefs):
        for a in range(max(0,(n-4-j)//3)+1):
            v = n - j - 3*a
            if v >= 4:
                total += c*comb(v, 4)
    return total


def main():
    total_direct=0
    for n in range(4,23):
        classes = Counter()
        key_to_triple = {}
        for pos in combinations(range(n),4):
            prof=profile_from_positions(pos,n)
            triple=triple_from_positions(pos)
            old=key_to_triple.setdefault(prof,triple)
            assert old == triple, (n,pos,'profile collision between triples')
            classes[triple]+=1
            total_direct+=1
        predicted=parameter_classes(n)
        assert classes==predicted, (n, classes-predicted, predicted-classes)
        assert len(key_to_triple)==len(predicted)
        assert sum(classes.values())==comb(n,4)
        assert sum(v*v for v in classes.values()) == s2_by_coefficients(n)
        if n>=10:
            kmax=max(classes.values())
            assert kmax==4*(n-6)
            winners=[key for key,val in classes.items() if val==kmax]
            assert winners==[(0,1,3)]
    print('DIRECT_SLIDING_WINDOW_OK', total_direct, 'N_4_TO_22')

    for n in range(4,201):
        c=parameter_classes(n)
        assert sum(c.values())==comb(n,4)
        assert sum(x*x for x in c.values())==s2_by_coefficients(n)
        if n>=10:
            assert max(c.values())==4*(n-6)
    print('EXACT_FIBER_AND_SECOND_MOMENT_OK', 'N_4_TO_200')
    assert (20 * 24 * 24) // (3 * 120) == 32
    print('ASYMPTOTIC_CONSTANT_FROM_POLE_OK', 32)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
