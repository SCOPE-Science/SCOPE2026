"""Exact cube quadratic-rank certificate and independent small-field U^3 checks."""
from collections import Counter
from itertools import combinations, permutations, product
from math import cos, pi, sqrt


def determinant(a):
    n = len(a)
    out = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i in range(n):
            term *= a[i][perm[i]]
        out += term
    return out


def certificate():
    # Each vertex u=(1,v1,v2,v3) contributes a signed rank-one form uu^T.
    vertices = [(1, (j >> 0) & 1, (j >> 1) & 1, (j >> 2) & 1) for j in range(8)]
    counts = Counter()
    for signs in product((-1, 1), repeat=8):
        a = [[sum(signs[v] * vertices[v][i] * vertices[v][j] for v in range(8))
              for j in range(4)] for i in range(4)]
        rank, pivot = 0, 0
        for k in range(1, 5):
            for ind in combinations(range(4), k):
                d = determinant([[a[i][j] for j in ind] for i in ind])
                if d:
                    rank, pivot = k, d
                    break
        counts[(rank, 0 if pivot == 0 else abs(pivot), (pivot > 0) - (pivot < 0))] += 1
    expected = {
        (0, 0, 0): 2,
        (1, 2, -1): 8, (1, 2, 1): 8,
        (2, 4, -1): 38, (2, 4, 1): 24, (2, 16, -1): 6,
        (3, 8, -1): 56, (3, 8, 1): 56,
        (4, 16, -1): 32, (4, 16, 1): 24, (4, 64, 1): 2,
    }
    assert counts == expected, (counts, expected)
    assert sum(counts.values()) == 256
    print('Exact integer principal-minor certificate: 256 / 256 patterns passed')
    print('Rank totals:', sorted(Counter({r: sum(v for (rr, d, s), v in counts.items() if rr == r) for r in range(5)}).items()))
    return counts


def formula(p, n):
    assert p % 2 and n >= 1
    q = p ** n
    chi2 = 1 if pow(2, (p - 1) // 2, p) == 1 else -1
    e = 1 if p % 4 == 1 else 1j
    nu = 1 if p % 4 == 1 or n % 2 == 0 else -1
    eta = round(((e * chi2) ** n).real) if nu == 1 else 0
    if nu == -1:
        return (2 + 20/q - 6/q**2) / 256
    return (2 + 16*eta/sqrt(q) + 68/q + 112*eta/q**1.5 + 58/q**2) / 256


def direct(p, n):
    points = list(product(range(p), repeat=n))
    phase = {x: cos(2*pi*sum(t*t for t in x)/p) for x in points}
    result = 0.0
    for x, h1, h2, h3 in product(points, repeat=4):
        prod = 1.0
        for a, b, c in product((0, 1), repeat=3):
            y = tuple((x[j] + a*h1[j] + b*h2[j] + c*h3[j]) % p for j in range(n))
            prod *= phase[y]
        result += prod
    return result / len(points)**4


if __name__ == '__main__':
    certificate()
    for p, n in [(3,1),(5,1),(7,1),(11,1),(13,1),(3,2),(5,2)]:
        lhs, rhs = direct(p, n), formula(p, n)
        assert abs(lhs - rhs) < 2e-10, (p, n, lhs, rhs)
        print(f'Brute cube p={p}, n={n}: {lhs:.12f} (matches formula)')
    print('PASS: exact rank table and seven direct complete-cube tests')
