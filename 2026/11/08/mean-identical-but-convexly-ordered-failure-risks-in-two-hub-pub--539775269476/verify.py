"""Exact finite checks for two-hub public-output reliability.

Python 3, standard library only. Run: python verify.py
The mathematical conclusions for arbitrary order follow from the proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def largest_component(n, edges, present):
    present = set(present)
    if not present:
        return 0
    adjacency = {u: [] for u in present}
    for u, v in edges:
        if u in present and v in present:
            adjacency[u].append(v)
            adjacency[v].append(u)
    seen = set()
    result = 0
    for origin in present:
        if origin in seen:
            continue
        stack = [origin]
        seen.add(origin)
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        result = max(result, size)
    return result


def double_star(n, a):
    # Two joined centers, with a leaves on the first and b on the second.
    b = n - 2 - a
    return [(0, 1)] + [(0, i) for i in range(2, 2 + a)] + [(1, i) for i in range(2 + a, n)]


def direct_law(n, a, m):
    edges = double_star(n, a)
    hist = Counter(largest_component(n, edges, subset)
                   for subset in combinations(range(n), m))
    assert sum(hist.values()) == comb(n, m)
    return hist


def closed_sum(n, m):
    N = n - 2
    choose = lambda k: comb(N, k) if 0 <= k <= N else 0
    return m * choose(m-2) + (m+1) * choose(m-1) + (choose(m) if m else 0)


def second_moment(hist):
    return Fraction(sum(y*y*c for y,c in hist.items()), sum(hist.values()))


def mean(hist):
    return Fraction(sum(y*c for y,c in hist.items()), sum(hist.values()))


def variance(hist):
    return second_moment(hist) - mean(hist)**2


def sum_hinge(hist, threshold):
    return sum(max(0, x-threshold)*count for x, count in hist.items())


def percolation_law(n, a, survival):
    result = Counter()
    for m in range(n+1):
        for x, count in direct_law(n, a, m).items():
            result[x] += count * survival**m * (1-survival)**(n-m)
    return result


def closed_pgf(n, a, survival):
    b=n-2-a
    s=survival
    t=1-s
    out=Counter()
    # Both hubs survive: 2 + Binomial(n-2, s).
    for j in range(n-1):
        out[2+j] += s*s*comb(n-2,j)*s**j*t**(n-2-j)
    # Exactly one hub survives.
    for side in (a,b):
        for j in range(side+1):
            out[1+j] += s*t*comb(side,j)*s**j*t**(side-j)
    # Neither hub survives: output is 1 unless no leaf survives.
    out[0] += t*t * t**(n-2)
    out[1] += t*t * (1-t**(n-2))
    return +out


def run():
    histogram_checks=0
    mean_checks=0
    convex_checks=0
    variance_checks=0
    pgf_checks=0
    for n in range(4,10):
        N=n-2
        for m in range(n+1):
            laws={a:direct_law(n,a,m) for a in range(N+1)}
            for a,h in laws.items():
                assert sum(x*c for x,c in h.items()) == closed_sum(n,m), (n,m,a)
                mean_checks+=1
                histogram_checks+=1
            # Moving one leaf from the smaller side toward the larger
            # gives a convexly more variable law.
            for a in range((N+1)//2, N):
                low=laws[a]
                high=laws[a+1]
                assert mean(low)==mean(high), (n,m,a)
                for t in range(n+1):
                    assert sum_hinge(low,t) <= sum_hinge(high,t), (n,m,a,t)
                    convex_checks+=1
                if n>=4:
                    coeff=Fraction(m*(m-1)*(m-2)*(n-m),n*(n-1)*(n-2)*(n-3))
                    expected=coeff*((a+1)**2+(N-a-1)**2-a*a-(N-a)**2)
                    assert variance(high)-variance(low)==expected, (n,m,a,variance(high)-variance(low),expected)
                    variance_checks+=1
        for s in (Fraction(1,3),Fraction(1,2),Fraction(3,4)):
            means=[]
            for a in range(N+1):
                h=percolation_law(n,a,s)
                g=closed_pgf(n,a,s)
                assert h==g, (n,a,s,h,g)
                assert sum(h.values())==1, (n,a,s)
                means.append(sum(x*c for x,c in h.items()))
                pgf_checks+=1
            assert len(set(means))==1, (n,s,means)
    print('PASS exact finite checks:')
    print('  profile histograms:',histogram_checks)
    print('  mean identities:',mean_checks)
    print('  convex-order hinge inequalities:',convex_checks)
    print('  variance-difference identities:',variance_checks)
    print('  independent-survival PGF comparisons:',pgf_checks)

if __name__=='__main__':
    run()
