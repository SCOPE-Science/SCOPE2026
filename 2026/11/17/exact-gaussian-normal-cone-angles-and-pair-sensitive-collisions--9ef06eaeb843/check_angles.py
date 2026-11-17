"""Exact finite verification of a Gaussian normal-cone formula for sparse-paving base polytopes.

Enumerates ALL weight orders using unique subset-sum weights, brute-forces all
permitted bases, and compares exact winning counts to a closed expression.
This is supplementary finite evidence, not a proof for arbitrary dimensions.
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, factorial


def test_case(n, r, forbidden):
    F = {frozenset(B) for B in forbidden}
    assert len(F) == len(forbidden) and 3 <= r <= n - 3
    assert all(len(A & B) <= r-2 for A, B in combinations(F, 2))
    bases = [frozenset(B) for B in combinations(range(n), r) if frozenset(B) not in F]
    allowed = set(bases)
    N, k = comb(n, r), r * (n - r)
    degrees = {B: sum(len(B & H) == r-1 for H in F) for B in bases}
    assert all(deg <= min(r,n-r) for deg in degrees.values())
    counts = {B: 0 for B in bases}
    # Scores are superincreasing binary weights. This checks the maximizer of
    # the actual linear objective for every total order, without using the
    # second-best-swap argument employed in the general mathematical proof.
    for order in permutations(range(n)):
        weights = [0] * n
        for i, element in enumerate(order):
            weights[element] = 1 << (n-i-1)
        winner = max(bases, key=lambda B: sum(weights[i] for i in B))
        counts[winner] += 1
    number_orders = factorial(n)
    assert sum(counts.values()) == number_orders
    for B in bases:
        predicted = Fraction(1, N) * (1 + Fraction(degrees[B], k))
        observed = Fraction(counts[B], number_orders)
        assert observed == predicted, (n,r,F,B,observed,predicted)
    lam = len(F)
    mu = sum(len(A & B) == r-2 for A,B in combinations(F,2))
    collision_observed = sum(Fraction(c,number_orders)**2 for c in counts.values())
    collision_predicted = (Fraction(N,1) + lam * (1 + Fraction(1,k)) + Fraction(8*mu,k*k)) / (N*N)
    assert collision_observed == collision_predicted
    return dict(n=n,r=r,forbidden=lam,mu=mu,bases=len(bases),orders=number_orders,
                degree_histogram={j:sum(x==j for x in degrees.values()) for j in sorted(set(degrees.values()))},
                collision=str(collision_observed))


def main():
    cases = [
        (6,3,[(0,1,2),(3,4,5)]),
        (6,3,[(0,1,2),(0,3,4)]),
        (6,3,[(0,1,2)]),
        (7,3,[(0,1,2),(0,3,4),(0,5,6)]),
        (7,4,[(0,1,2,3),(0,1,4,5)]),
        (8,3,[(0,1,2),(0,3,4),(0,5,6)]),
        (8,4,[(0,1,2,3),(0,1,4,5),(2,3,6,7)]),
    ]
    for n,r,F in cases:
        print('CASE_PASS',test_case(n,r,F))
    # Explicit witness: the same lambda=2 but different mu.
    a=test_case(6,3,[(0,1,2),(3,4,5)])
    b=test_case(6,3,[(0,1,2),(0,3,4)])
    assert a['collision']=='1/18' and b['collision']=='113/2025'
    assert a['degree_histogram']=={1:18} and b['degree_histogram']=={0:4,1:10,2:4}
    print('SPARSE_PAVING_GAUSSIAN_ANGLE_PASS cases=7 example=exact')


if __name__=='__main__':
    main()
