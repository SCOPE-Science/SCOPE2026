"""Check exact secrecy-event size spectra in finite full-product simplicial models.

Independent checks: brute-force evaluation of the (SN) clause, and a separate
inclusion-exclusion polynomial, followed by checks of the sharp top coefficient.
Python 3.9+; no external dependencies.
"""
from itertools import product
from math import comb, factorial
from collections import Counter


def onto_count(t, s):
    """Number of surjections [t] -> [s], by inclusion-exclusion."""
    return sum((-1)**(s-j) * comb(s,j) * j**t for j in range(s+1))


def predicted_counts(dims, owner=0):
    """Coefficients of complement-size polynomial by inclusion-exclusion."""
    assert len(dims) >= 2 and min(dims) >= 1
    na = dims[owner]
    other = [dims[j] for j in range(len(dims)) if j != owner]
    outside = (na-1)
    for q in other: outside *= q
    coefficients = [0]*(outside+1)
    for allowed in product(*(range(q+1) for q in other)):
        sign = (-1)**sum(q-t for q,t in zip(other,allowed))
        mult = sign
        for q,t in zip(other,allowed): mult *= comb(q,t)
        e = (na-1)
        for t in allowed: e *= t
        for h in range(e+1):
            coefficients[h] += mult * comb(e,h)
    return coefficients


def brute_counts(dims, owner=0):
    """Evaluate each possible U directly against the original star and SN clause."""
    facets = list(product(*(range(x) for x in dims)))
    star = [x for x in facets if x[owner] == 0]
    outside = [x for x in facets if x[owner] != 0]
    out = Counter()
    for mask in range(1 << len(outside)):
        H = {outside[j] for j in range(len(outside)) if mask>>j & 1}
        U = set(facets)-H
        # Ordinary knowledge: each facet in the owner's star belongs to U.
        if not all(x in U for x in star): continue
        # Original external uncertainty condition (SN), not its projection reformulation.
        good = all(any(x[b] == y[b] and y not in U for y in facets)
                   for x in star for b in range(len(dims)) if b != owner)
        if good: out[len(H)] += 1
    return [out[j] for j in range(len(outside)+1)]


def extremal_count(dims, owner=0):
    na = dims[owner]
    others = [(j,dims[j]) for j in range(len(dims)) if j != owner]
    t = max(q for j,q in others)
    if na == 1: return t, 0
    anchor = next(j for j,q in others if q == t)
    total = (na-1)**t
    for j,q in others:
        if j != anchor: total *= onto_count(t,q)
    return t,total


def main():
    cases = []
    for k in (2,3,4):
        for dims in product(range(1,5) if k==2 else range(1,4), repeat=k):
            outside = (dims[0]-1)
            for q in dims[1:]: outside *= q
            if outside <= 12: cases.append(dims)
    checked = 0
    exhaustive_events = 0
    for dims in cases:
        predicted = predicted_counts(dims)
        brute = brute_counts(dims)
        assert predicted == brute, (dims, predicted, brute)
        t, n = extremal_count(dims)
        if dims[0] == 1:
            assert not any(predicted), dims
        else:
            assert all(x==0 for x in predicted[:t]), dims
            assert predicted[t] == n, (dims, predicted, t, n)
            assert predicted[-1] == 1, dims
        checked += 1
        exhaustive_events += 2 ** ((dims[0]-1) * __import__('math').prod(dims[1:]))
    assert predicted_counts((2,2,2)) == [0,0,2,4,1]
    assert sum(predicted_counts((3,3))) == 27
    assert predicted_counts((3,2,2))[2] == 8
    # A separate medium symbolic computation beyond the exhaustive range.
    dims = (4,3,5,2)
    coef = predicted_counts(dims)
    t, n = extremal_count(dims)
    assert min(i for i,c in enumerate(coef) if c) == t
    assert coef[t] == n
    assert sum(coef) > 0
    print('PASS: %d parameter vectors, %d candidate-event inspections' % (checked, exhaustive_events))
    print('grid (2,2,2):', predicted_counts((2,2,2)))
    print('grid (3,3): total', sum(predicted_counts((3,3))))
    print('grid (3,2,2): min-witness count', predicted_counts((3,2,2))[2])
    print('grid (4,3,5,2): min missing facets=%d, extremal event count=%d' % (t, n))

if __name__ == '__main__': main()
