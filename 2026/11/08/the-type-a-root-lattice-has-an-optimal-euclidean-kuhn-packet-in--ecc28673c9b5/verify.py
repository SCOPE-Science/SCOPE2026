"""Exact finite consistency checks for root-lattice packet identities.

The universal proof is contained in RESULT.md; this checker is supplementary.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product


def eulerian(n):
    rows = [[1]]
    for m in range(2, n + 1):
        prev = rows[-1]
        rows.append([(m - k) * (prev[k-1] if k else 0) + (k+1) * (prev[k] if k < m-1 else 0) for k in range(m)])
    return rows[-1]


def verify_packet(n):
    N = n + 1
    total = 0
    counts = Counter()
    for perm in permutations(range(1, n + 1)):
        rank = {v: j for j, v in enumerate(perm)}
        mins = [0] + [(-1 if rank[j-1] < rank[j] else 0) for j in range(2, N)] + [-1]
        k = -sum(mins)
        assert k == 1 + sum(rank[j] < rank[j + 1] for j in range(1, n))
        counts[k] += 1
        c = [Fraction(m * N + k, N) for m in mins]
        r2 = Fraction(k * (N-k), N)
        vertex = [0] * N
        for step in range(n + 1):
            assert sum(vertex) == 0
            assert all(mins[j] <= vertex[j] <= mins[j]+1 for j in range(N))
            assert sum((Fraction(vertex[j]) - c[j])**2 for j in range(N)) == r2
            total += 1
            if step < n:
                i = perm[step]
                vertex[i-1] += 1
                vertex[i] -= 1
    expected = eulerian(n)
    assert [counts[k] for k in range(1, n+1)] == expected, (n,counts,expected)
    assert max(Fraction(k*(N-k),N) for k in counts) == Fraction((N*N)//4,N)
    return total, list(counts.items())


def verify_voronoi(n):
    N=n+1
    checked=0
    for x in product(range(-2,3), repeat=N-1):
        x = tuple(x) + (-sum(x),)
        if max(x)-min(x) > 1:
            continue
        for z in product(range(-2,3), repeat=N-1):
            z = tuple(z) + (-sum(z),)
            assert 2*sum(a*b for a,b in zip(x,z)) <= sum(a*a for a in z)
            checked+=1
    return checked

if __name__ == '__main__':
    tests=0
    for n in range(1,8):
        j, counts=verify_packet(n)
        tests+=j
        print(f'A_{n}: {j} vertex-sphere equalities; Eulerian k counts {sorted(counts)}')
    for n in range(1,4):
        c=verify_voronoi(n)
        tests+=c
        print(f'A_{n}: {c} finite Voronoi-inequality comparisons')
    print(f'PASS: {tests} exact finite checks')
