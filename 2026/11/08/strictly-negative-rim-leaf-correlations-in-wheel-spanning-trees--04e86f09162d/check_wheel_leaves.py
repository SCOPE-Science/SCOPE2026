"""Exact reproducibility checks for rim-leaf covariances of uniform wheel spanning trees.
No random sampling or external dependencies are required.
Run with: python3 check_wheel_leaves.py
"""
from fractions import Fraction
from itertools import combinations


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def formulas(m):
    assert m >= 3
    den = lucas(2*m) - 2
    single = 3*fibonacci(2*m - 2)
    joint = {}
    for d in range(1, m//2 + 1):
        if d == 1:
            joint[d] = 4*fibonacci(2*m - 4)
        else:
            joint[d] = 9*fibonacci(2*d - 2)*fibonacci(2*(m-d-1))
    return den, single, joint


def enumeration(m):
    # Hub vertex m; rim vertices 0,...,m-1
    edges = [(i, (i+1)%m) for i in range(m)] + [(i, m) for i in range(m)]
    n = m + 1
    total, leaf_one = 0, 0
    leaves_pair = {d: 0 for d in range(1, m//2 + 1)}
    for chosen in combinations(range(len(edges)), n - 1):
        parent = list(range(n))
        deg = [0]*n
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        ok = True
        for j in chosen:
            a,b = edges[j]
            ra, rb = find(a), find(b)
            if ra == rb:
                ok = False
                break
            parent[ra] = rb
            deg[a] += 1
            deg[b] += 1
        if not ok: continue
        # With n-1 edges and no cycle, this is a spanning tree.
        total += 1
        if deg[0] == 1:
            leaf_one += 1
            for d in leaves_pair:
                if deg[d] == 1:
                    leaves_pair[d] += 1
    return total, leaf_one, leaves_pair


def main():
    checks = 0
    for m in range(3, 9):
        expected = formulas(m)
        actual = enumeration(m)
        assert actual == expected, (m, actual, expected)
        checks += 2 + len(expected[2])
    for m in range(3, 101):
        z, p, q = formulas(m)
        for d,numer in q.items():
            assert numer*z < p*p, (m,d)
            checks += 1
        if m >= 4:
            assert 9*fibonacci(2*m-6) < 4*fibonacci(2*m-4)
            checks += 1
        if m >= 6:
            assert all(q[d] < q[d+1] for d in range(2,m//2))
            checks += 1
    print('PASS: %d exact assertions; brute spanning-tree enumeration m=3,...,8; all-size-claim instances m=3,...,100.'%checks)
    for m in range(3, 9):
        z,p,q=formulas(m)
        print(m,z,Fraction(p,z),{d:Fraction(q[d]*z-p*p,z*z) for d in q})

if __name__ == '__main__':
    main()
