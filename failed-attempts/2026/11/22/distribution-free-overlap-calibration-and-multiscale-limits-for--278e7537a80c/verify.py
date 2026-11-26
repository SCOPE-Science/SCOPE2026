"""Exact rational verification of common-edge laws for exchangeable matchings.

Run with Python 3: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def falling(x, r):
    ans = 1
    for t in range(r):
        ans *= x - t
    return ans


def all_matchings(n):
    def generate(vertices):
        if not vertices:
            yield ()
            return
        v, *rest = vertices
        for tail in generate(rest):
            yield tail
        for j, w in enumerate(rest):
            remaining = rest[:j] + rest[j + 1:]
            for tail in generate(remaining):
                yield ((v, w),) + tail
    return [frozenset(m) for m in generate(list(range(n)))]


def exact_factorial(n, a, b, r):
    if r > min(a, b):
        return Fraction(0)
    return Fraction(2**r * falling(a, r) * falling(b, r), falling(n, 2*r))


def exact_pmf(n, a, b):
    # E[z**H] = sum_r E[(H)_r](z-1)**r/r!
    return tuple(sum(Fraction((-1)**(r-k) * comb(r,k), factorial(r))
        * exact_factorial(n,a,b,r) for r in range(k, min(a,b)+1))
        for k in range(min(a,b)+1))


def circular_matching(order, spacing_ranks):
    n = len(order)
    assert n == len(spacing_ranks)
    result = []
    for i in range(n):
        if spacing_ranks[i] < spacing_ranks[(i-1)%n] and spacing_ranks[i] < spacing_ranks[(i+1)%n]:
            result.append(tuple(sorted((order[i],order[(i+1)%n]))))
    return frozenset(result)


def test():
    checks = 0
    for n in range(2,8):
        matchings = all_matchings(n)
        by_size = {k:[m for m in matchings if len(m)==k] for k in range(n//2+1)}
        for a in by_size:
            for b in by_size:
                obs = Counter(len(x&y) for x in by_size[a] for y in by_size[b])
                den = len(by_size[a])*len(by_size[b])
                expected = exact_pmf(n,a,b)
                assert sum(expected)==1
                assert all(Fraction(obs[k],den)==expected[k] for k in range(min(a,b)+1)), (n,a,b,obs,expected)
                checks += 1
    for n in (5,6):
        label_order = (0,) + tuple(range(1,n))
        distribution = Counter()
        for order_tail in permutations(range(1,n)):
            order = (0,) + order_tail
            for gaps in permutations(range(n)):
                distribution[circular_matching(order,gaps)] += 1
        total = factorial(n-1)*factorial(n)
        assert sum(distribution.values())==total
        for k in range(n//2+1):
            counts = [distribution.get(m,0) for m in all_matchings(n) if len(m)==k]
            assert len(set(counts))==1, (n,k, min(counts),max(counts))
            checks += 1
        E = sum(Fraction(len(m)*freq,total) for m,freq in distribution.items())
        Ef2 = sum(Fraction(len(m)*(len(m)-1)*freq,total) for m,freq in distribution.items())
        Var = Ef2 + E-E*E
        assert E==Fraction(n,3)
        assert Var==Fraction(2*n,45)
        checks += 2
        second = sum(Fraction(freq*freq2*len(m & m2),total**2)
            for m,freq in distribution.items() for m2,freq2 in distribution.items())
        assert second == Fraction(2*n,9*(n-1))
        checks += 1
        p_edge = Fraction(2, 3*(n-1))
        conditional_means = {
            m:sum(Fraction(freq2*len(m & m2),total)
                for m2,freq2 in distribution.items())
            for m in distribution}
        assert all(v==p_edge*len(m) for m,v in conditional_means.items())
        covariance = sum(Fraction(freq,total)*v*v for m,v in conditional_means.items() for freq in [distribution[m]])-second**2
        assert covariance == Fraction(8*n,405*(n-1)**2)
        checks += 2
    print(f'PASS: {checks} exact distribution/moment/frequency checks; n up to 7 for matchings and 6 for circular configurations')

if __name__=='__main__':
    test()
