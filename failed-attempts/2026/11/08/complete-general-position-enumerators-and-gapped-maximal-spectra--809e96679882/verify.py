#!/usr/bin/env python3
"""Independent exact checks of rook-graph general-position enumerators.

Python 3 standard library only. All assertions concern finite test cases;
they do not replace the unrestricted combinatorial proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def plus(p, q):
    result = p.copy()
    for degree, count in q.items():
        result[degree] = result.get(degree, 0) + count
    return {i: a for i, a in result.items() if a}


def times(p, q):
    result = {}
    for i, a in p.items():
        for j, b in q.items():
            result[i + j] = result.get(i + j, 0) + a * b
    return {i: a for i, a in result.items() if a}


def scaled(p, a):
    return {degree: count * a for degree, count in p.items() if count * a}


def exponential_coefficients(m, n, mode):
    """[x^i y^j] exp(B) for i<=m,j<=n; exact rational arithmetic.

    Modes: all star components, only left-centered nontrivial stars,
    or only right-centered nontrivial stars.
    """
    terms = {}
    if mode == "all":
        terms[(1, 1)] = {1: Fraction(1)}
    if mode in ("all", "left"):
        for j in range(2, n + 1):
            terms[(1, j)] = {j: Fraction(1, factorial(j))}
    if mode in ("all", "right"):
        for i in range(2, m + 1):
            terms[(i, 1)] = {i: Fraction(1, factorial(i))}
    coefficients = {(0, 0): {0: Fraction(1)}}
    # For F=exp(B), x*dF/dx=x*B_x*F.
    for i in range(1, m + 1):
        for j in range(n + 1):
            result = {}
            for (a, b), p in terms.items():
                if a <= i and b <= j and (i-a, j-b) in coefficients:
                    result = plus(result, scaled(times(p, coefficients[i-a, j-b]), Fraction(a, i)))
            coefficients[(i, j)] = result
    return coefficients


def predicted(m, n):
    """All/maximal GP polynomials via independently coded bivariate EGFs."""
    all_stars = exponential_coefficients(m, n, "all")
    left = exponential_coefficients(m, n, "left")
    right = exponential_coefficients(m, n, "right")
    general = {}
    for i in range(m + 1):
        for j in range(n + 1):
            p = all_stars.get((i, j), {})
            if p:
                general = plus(general, scaled(p, Fraction(factorial(m)*factorial(n), factorial(m-i)*factorial(n-j))))
    maximal = scaled(all_stars[(m,n)], factorial(m)*factorial(n))
    for i in range(m):
        maximal = plus(maximal, scaled(left.get((i,n), {}), Fraction(factorial(m)*factorial(n), factorial(m-i))))
    for j in range(n):
        maximal = plus(maximal, scaled(right.get((m,j), {}), Fraction(factorial(m)*factorial(n), factorial(n-j))))
    if any(a.denominator != 1 for a in list(general.values()) + list(maximal.values())):
        raise AssertionError("nonintegral labeled counts")
    return ({k:int(v) for k,v in general.items()},
            {k:int(v) for k,v in maximal.items()})


def direct(m, n):
    """Ground truth from shortest paths for all vertex subsets of the rook graph."""
    N = m*n
    vertices = [(i,j) for i in range(m) for j in range(n)]
    distances = [[0 if u == v else 1 if (vertices[u][0] == vertices[v][0]
                                                   or vertices[u][1] == vertices[v][1])
                  else 2 for v in range(N)] for u in range(N)]
    forbidden = [[] for _ in range(N)]
    for a,b,c in combinations(range(N), 3):
        if (distances[a][b] + distances[b][c] == distances[a][c]
            or distances[a][c] + distances[c][b] == distances[a][b]
            or distances[b][a] + distances[a][c] == distances[b][c]):
            mask = (1<<a)|(1<<b)|(1<<c)
            forbidden[mask.bit_length()-1].append(mask)
    valid = bytearray(1<<N)
    valid[0] = 1
    general = Counter()
    maximal = Counter()
    for mask in range(1<<N):
        if mask:
            highest = mask.bit_length()-1
            valid[mask] = valid[mask ^ (1<<highest)] and all((mask&bad) != bad for bad in forbidden[highest])
        if valid[mask]:
            general[mask.bit_count()] += 1
    for mask in range(1<<N):
        if valid[mask] and not any(valid[mask | (1<<i)] for i in range(N) if not (mask & (1<<i))):
            maximal[mask.bit_count()] += 1
    return dict(general), dict(maximal)


@lru_cache(maxsize=None)
def associated_stirling(s,t):
    """Partitions of s labeled vertices into t blocks, each of size >= 2."""
    if s == 0 and t == 0:
        return 1
    if s < 2*t or t == 0:
        return 0
    return sum(comb(s-1, j-1)*associated_stirling(s-j, t-1)
               for j in range(2, s+1))


def falling(n,t):
    return factorial(n)//factorial(n-t)


def minimum_count(m,n):
    a = sum(falling(n,t)*associated_stirling(m,t)
            for t in range(1,m//2+1))
    if m < n:
        return a
    return factorial(m)+2*a


def spectrum(m,n):
    return set([m]) | set(range(n,m+n-1))


def check():
    direct_cases = [(2,2),(2,3),(2,4),(2,5),
                    (3,3),(3,4),(3,5),(4,4)]
    subsets = 0
    gp_total = 0
    maximal_total = 0
    for m,n in direct_cases:
        all_direct, maximal_direct = direct(m,n)
        all_formula, maximal_formula = predicted(m,n)
        if all_direct != all_formula or maximal_direct != maximal_formula:
            raise AssertionError((m,n,"graph/formula disagreement",all_direct,all_formula,maximal_direct,maximal_formula))
        subsets += 1<<(m*n)
        gp_total += sum(all_direct.values())
        maximal_total += sum(maximal_direct.values())
    pairs = 0
    for m in range(2,9):
        for n in range(m, min(m+6,13)):
            _, M = predicted(m,n)
            if set(M) != spectrum(m,n):
                raise AssertionError((m,n,"spectrum",M))
            if M[m] != minimum_count(m,n):
                raise AssertionError((m,n,"lower count",M[m],minimum_count(m,n)))
            if m==2 and n>=3 and M[n] != 2**n:
                raise AssertionError((m,n,"thin-board maximum",M[n]))
            if m>=3 and M[m+n-2] != m*n:
                raise AssertionError((m,n,"top count",M[m+n-2]))
            pairs += 1
    print("VERIFY_OK direct_cases=%d checked_subsets=%d general_position_sets=%d maximal_general_position_sets=%d symbolic_parameter_pairs=%d spectrum=PASS extremal_counts=PASS" %
          (len(direct_cases),subsets,gp_total,maximal_total,pairs))


if __name__ == "__main__":
    check()
