"""Finite checks of local-maximum observations on matching-deleted complete graphs.

Only the Python standard library is needed. Run with python verify.py.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial, comb


def all_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
    else:
        a = vertices[0]
        for j in range(1, len(vertices)):
            b = vertices[j]
            remaining = vertices[1:j] + vertices[j + 1:]
            for rest in all_matchings(remaining):
                yield ((a, b),) + rest


def peaks(order, matching):
    partner = {}
    for a, b in matching:
        partner[a] = b
        partner[b] = a
    rank = {v: i for i, v in enumerate(order)}
    return tuple(sorted(v for v in order if all(rank[v] < rank[w]
                          for w in order if w != v and w != partner[v])))


def double_factorial_odd(u):
    ans = 1
    for k in range(1, u + 1):
        ans *= 2*k-1
    return ans


def optimal_success(q, m):
    p = Fraction(1, q * (2*q - 1))
    # Inclusion-exclusion for the number U of unobserved matched pairs.
    out = Fraction(0)
    distribution = []
    for u in range(q+1):
        pu = comb(q,u)*sum(((-1)**j)*comb(q-u,j)*(1-(u+j)*p)**m
                          for j in range(q-u+1))
        assert pu >= 0
        distribution.append(pu)
        out += pu / double_factorial_odd(u)
    assert sum(distribution) == 1
    return out


def run():
    tested = 0
    for n in (2, 4, 6):
        q=n//2
        for matching in all_matchings(range(n)):
            counts=Counter(peaks(order,matching) for order in permutations(range(n)))
            pairs={tuple(sorted(e)) for e in matching}
            for v in range(n):
                assert Fraction(counts[(v,)],factorial(n)) == Fraction(n-2,n*(n-1))
                tested+=1
            for a in range(n):
                for b in range(a+1,n):
                    prob=Fraction(counts[(a,b)],factorial(n))
                    assert prob == (Fraction(2,n*(n-1)) if (a,b) in pairs else 0)
                    tested+=1
            assert sum(counts.values()) == factorial(n)
            tested+=1
    for q in range(1,8):
        for m in range(7):
            rate = optimal_success(q,m)
            assert Fraction(1, double_factorial_odd(q)) <= rate <= 1
            if m>0: assert rate >= optimal_success(q,m-1)
            tested+=1
    # Explicit n=6, one draw: with probability 1/5 a pair is seen.
    assert optimal_success(3,1) == Fraction(3,25)
    print(f"PASS: {tested} finite exact checks")

if __name__=='__main__':
    run()
