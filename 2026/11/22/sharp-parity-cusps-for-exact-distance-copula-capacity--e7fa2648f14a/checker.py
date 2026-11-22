"""Independent finite grid diagnostics for the exact-distance coupling theorem.

The mathematical theorem is proved in RESULT.md for all real distances; these
finite checks test its formulas and the explicit extremizing permutations.
"""
from fractions import Fraction
from itertools import permutations


def predicted(d):
    assert Fraction(0) < d < Fraction(1)
    m = d.denominator // d.numerator  # floor(1/d) for reduced positive fraction
    return m*d if m%2==0 else 2-(m+1)*d


def flip_grid(n, s):
    """Piecewise matching on each s-spaced residue class, fixing odd tails."""
    perm = list(range(n))
    for residue in range(s):
        chain = list(range(residue, n, s))
        for j in range(0, len(chain)-1, 2):
            i, k = chain[j], chain[j+1]
            perm[i], perm[k] = k, i
    assert sorted(perm) == list(range(n))
    assert all(perm[perm[i]] == i for i in range(n))
    return perm


def upper_grid(n, s):
    # Each odd-length residue chain necessarily has one unmatched site.
    return Fraction(n - sum(((n - r + s - 1)//s)%2 for r in range(s)), n)


def run():
    checks=0
    # Exact exhaustive search over ALL couplings: Birkhoff implies an
    # optimum at a permutation for uniform discrete marginals.
    for n in range(2, 9):
        for s in range(1, n):
            d=Fraction(s,n)
            expected=predicted(d)
            opt=sum(abs(i-j)==s for i,j in enumerate(flip_grid(n,s)))
            assert Fraction(opt,n)==expected,(n,s,'construction')
            assert upper_grid(n,s)==expected,(n,s,'odd-chain bound')
            checks+=1
            max_brute=max(sum(abs(i-j)==s for i,j in enumerate(p)) for p in permutations(range(n)))
            assert max_brute==opt,(n,s,'global maximum')
            checks+=1
    # Larger rational grids, including exactly reciprocal odd/even distance.
    for n in range(9,129):
        for s in range(1,n):
            d=Fraction(s,n)
            expected=predicted(d)
            p=flip_grid(n,s)
            assert Fraction(sum(abs(i-j)==s for i,j in enumerate(p)),n)==expected
            assert upper_grid(n,s)==expected
            checks+=1
    # Consistency and bounds at all rationals with small denominators.
    for q in range(2,60):
        for p in range(1,q):
            d=Fraction(p,q)
            ans=predicted(d)
            assert Fraction(0)<ans<=1
            checks+=1
    print('PASS',checks,'exact rational and exhaustive finite checks')

if __name__=='__main__':run()
