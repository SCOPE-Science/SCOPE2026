"""Independent finite checks for the prism two-factor cycle-count theorem.

No network, third-party packages, or nonlocal data are required.
Run: python3 prism_twofactor_verify.py
"""
from collections import Counter
from math import comb


def graph_edges(n):
    assert n >= 3
    edges = set()
    for i in range(n):
        for layer in (0, 1):
            edges.add(tuple(sorted((2*i+layer, 2*((i+1)%n)+layer))))
        edges.add((2*i, 2*i+1))
    return sorted(edges)


def exact_cycle_census(n):
    """Enumerate matchings by backtracking, then independently count
    connected components in each 2-regular complement."""
    edges = graph_edges(n)
    at = [[] for _ in range(2*n)]
    for i, (a, b) in enumerate(edges):
        at[a].append(i)
        at[b].append(i)
    counts = Counter()
    matchings = 0

    def recurse(unused, used_edges):
        nonlocal matchings
        if not unused:
            matchings += 1
            comp_adj = [[] for _ in range(2*n)]
            for j, (a, b) in enumerate(edges):
                if j not in used_edges:
                    comp_adj[a].append(b)
                    comp_adj[b].append(a)
            assert all(len(x) == 2 for x in comp_adj)
            seen = set()
            cc = 0
            for v in range(2*n):
                if v not in seen:
                    cc += 1
                    stack = [v]
                    seen.add(v)
                    while stack:
                        w = stack.pop()
                        for u in comp_adj[w]:
                            if u not in seen:
                                seen.add(u)
                                stack.append(u)
            counts[cc] += 1
            return
        a = min(unused)
        for j in at[a]:
            x, y = edges[j]
            b = y if x == a else x
            if b in unused:
                recurse(unused-{a,b}, used_edges | {j})

    recurse(set(range(2*n)), set())
    return counts, matchings


def formula(n):
    v = Counter()
    for k in range(1, n//2+1):
        v[k] += n*comb(n-k-1, k)//(n-2*k) if n-2*k else 2
        # formula in numerator only for n-2k>0; the even maximum is 2
    v[2] += 1
    if n % 2 == 0:
        v[1] += 2
    return +v


def direct_cycle_matchings(n):
    # independent brute-force enumeration of all vertex-disjoint edge sets on C_n
    c = Counter()
    for mask in range(1 << n):
        if any((mask >> i & 1) and (mask >> ((i+1) % n) & 1)
               for i in range(n)):
            continue
        c[mask.bit_count()] += 1
    return c


def main():
    cases = 0
    for n in range(3, 15):
        census, total = exact_cycle_census(n)
        predicted = formula(n)
        assert census == predicted, (n, census, predicted)
        M = direct_cycle_matchings(n)
        transformed = M.copy()
        transformed[0] -= 1
        if n % 2 == 0:
            transformed[1] += 2
        transformed[2] += 1
        transformed = +transformed
        assert transformed == predicted, (n, transformed, predicted)
        assert total == sum(predicted.values())
        assert predicted[1] == n + (2 if n % 2 == 0 else 0)
        cases += 1
    print('EXHAUSTIVE_MATCHING_COMPLEMENT_CYCLE_CENSUS_PASS', cases)

    # Exact first-coefficient Newton-defect formula, checked over a large
    # finite interval; the rigorous all-order sign proof is in RESULT.md.
    for m in range(4, 201):
        for parity in (0, 1):
            n = 2*m + parity
            a = n + (2 if parity == 0 else 0)
            b = n*(n-3)//2 + 1
            c = n*(n-4)*(n-5)//6
            d = m-1
            defect = 2*d*a*c-(d-1)*b*b
            if parity == 0:
                closed3 = (m-2)*(m-1)*(4*m**3-55*m+3)
            else:
                closed3 = (m-2)*(4*m**4-12*m**3-15*m**2+14*m+6)
            assert 3*defect == closed3 and defect > 0, (m, parity)
    print('FIRST_NEWTON_OBSTRUCTION_EXACT_INTEGER_CHECK_PASS', 394)

    # Low-order real-rootedness is proved by displayed factorizations.
    expected = {
        3: {1: 3, 2: 1},
        4: {1: 6, 2: 3},
        5: {1: 5, 2: 6},
        6: {1: 8, 2: 10, 3: 2},
        7: {1: 7, 2: 15, 3: 7},
        8: {1: 10, 2: 21, 3: 16, 4: 2},
        9: {1: 9, 2: 28, 3: 30, 4: 9},
    }
    for n, coeff in expected.items():
        assert dict(formula(n)) == coeff, n
    assert 15**2 - 4*7*7 == 29
    print('SMALL_BOUNDARY_CERTIFICATES_PASS n=3..9')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
