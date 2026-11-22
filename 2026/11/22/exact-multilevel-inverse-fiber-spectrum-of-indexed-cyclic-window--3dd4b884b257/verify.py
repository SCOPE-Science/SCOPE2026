"""Reproduce exact inverse-fiber counts for cyclic integer window-sum reads.

Run: python3 verify.py
Only standard-library arithmetic and exhaustive enumeration are used.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, gcd


def predicted_histogram(q, n, ell):
    """Count inverse lists by normalized pattern widths, without forward readout."""
    d = gcd(n, ell)
    m = n // d
    types = [(q - 1 - h, (h+1)**m - 2*h**m + (h-1)**m)
             for h in range(1, q)]
    types.insert(0, (q-1, 1))
    # (tuple of convolution coefficients) -> number of normalized configurations
    states = { (1,): 1 }
    for _ in range(d):
        nxt = defaultdict(int)
        for coeffs, count in states.items():
            for width, multiplicity in types:
                if not multiplicity:
                    continue
                convolution = [0] * (len(coeffs) + width)
                for j, cj in enumerate(coeffs):
                    for k in range(width + 1):
                        convolution[j+k] += cj
                nxt[tuple(convolution)] += count*multiplicity
        states = nxt
    histogram = Counter()
    for coeffs, number in states.items():
        for fiber_size in coeffs:
            histogram[fiber_size] += number
    return histogram


def direct_histogram(q, n, ell):
    """Build the ordered cyclic output for each source, by literal window addition."""
    counts = Counter()
    for x in product(range(q), repeat=n):
        y = tuple(sum(x[(i+j) % n] for j in range(ell)) for i in range(n))
        counts[y] += 1
    return Counter(counts.values())


def check():
    cases = 0
    sources = 0
    for q, limit in ((2, 12), (3, 9), (4, 7), (5, 6)):
        for n in range(2, limit+1):
            for ell in range(1, n+1):
                actual = direct_histogram(q, n, ell)
                predicted = predicted_histogram(q, n, ell)
                assert actual == predicted, (q, n, ell, actual, predicted)
                d, m = gcd(n, ell), n//gcd(n, ell)
                a = q**m-(q-1)**m
                capacity = a**(d-1)*(q**m + (d-1)*(q-1)**m)
                assert sum(actual.values()) == capacity, (q, n, ell)
                assert sum(j*count for j,count in actual.items()) == q**n
                central = sum(1 for z in product(range(q), repeat=d)
                              if sum(z) == (d*(q-1))//2)
                assert max(actual)==central, (q, n, ell, central, actual)
                cases += 1
                sources += q**n
    # Specific size frequencies of ternary three-residue channels
    for m in (1,2,3):
        n=3*m
        h=direct_histogram(3,n,3)
        u=2**m-2
        v=3**m-2**(m+1)+1
        expect={
           1:2*u**3+6*u*u*v+6*u*u+6*u*v*v+12*u*v+6*u+v**3+9*v*v+6*v+2,
           2:3*v*(u*u+4*u+2),
           3:2*u**3+6*u*u+6*u+3*v+2,
           4:3*u*u,
           5:6*u,
           6:2,
           7:1
        }
        assert all(h.get(j,0)==x for j,x in expect.items()), (m,h,expect)
    print('VERIFY_OK', 'parameter_cases=',cases,'source_instances=',sources,
          'q_ranges=2:2..12,3:2..9,4:2..7,5:2..6',
          'three_residue_ternary=1..3')

if __name__=='__main__':
    check()
