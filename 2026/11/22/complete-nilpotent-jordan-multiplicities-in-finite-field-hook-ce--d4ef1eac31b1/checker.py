"""Direct finite-field brute-force check for nilpotent hook-centralizer Jordan profiles.

Requires only Python 3 standard library. Use: python checker.py
"""
from itertools import product
from collections import Counter


class Field:
    def __init__(self, p, polynomial=None):
        self.p = p
        self.polynomial = polynomial or [0, 1]
        self.d = len(self.polynomial) - 1
        self.q = p ** self.d
        assert self.polynomial[-1] == 1
        self.add_table = [[self._add(a, b) for b in range(self.q)] for a in range(self.q)]
        self.mul_table = [[self._mul(a, b) for b in range(self.q)] for a in range(self.q)]

    def _digits(self, x):
        return [(x // (self.p ** i)) % self.p for i in range(self.d)]

    def _encode(self, a):
        return sum(x * self.p ** i for i, x in enumerate(a))

    def _add(self, x, y):
        a, b = self._digits(x), self._digits(y)
        return self._encode([(a[i] + b[i]) % self.p for i in range(self.d)])

    def _mul(self, x, y):
        a, b = self._digits(x), self._digits(y)
        f = [0] * (2 * self.d - 1)
        for i in range(self.d):
            for j in range(self.d):
                f[i + j] += a[i] * b[j]
        for k in range(2 * self.d - 2, self.d - 1, -1):
            c = f[k] % self.p
            for i in range(self.d):
                f[k - self.d + i] -= c * self.polynomial[i]
        return self._encode([x % self.p for x in f[:self.d]])

    def add(self, a, b):
        return self.add_table[a][b]

    def mul(self, a, b):
        return self.mul_table[a][b]

    def neg(self, a):
        return self._encode([(-x) % self.p for x in self._digits(a)])

    def inverse(self, a):
        assert a != 0
        return next(i for i in range(1, self.q) if self.mul(a, i) == 1)


def rank(M, F):
    A = [list(row) for row in M]
    rows, cols = len(A), len(A[0])
    k = 0
    for j in range(cols):
        pivot = next((i for i in range(k, rows) if A[i][j] != 0), None)
        if pivot is None:
            continue
        A[k], A[pivot] = A[pivot], A[k]
        inv = F.inverse(A[k][j])
        for c in range(j, cols):
            A[k][c] = F.mul(A[k][c], inv)
        for i in range(k + 1, rows):
            if A[i][j]:
                v = A[i][j]
                for c in range(j, cols):
                    A[i][c] = F.add(A[i][c], F.neg(F.mul(v, A[k][c])))
        k += 1
        if k == rows:
            break
    return k


def multiply(A, B, F):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:
                        C[i][j] = F.add(C[i][j], F.mul(A[i][k], B[k][j]))
    return C


def make_matrix(f, a, b, n, F):
    X = [[0] * (n + 1) for _ in range(n + 1)]
    # K[t]/t^n in basis 1,t,...,t^(n-1), with J:t^i->t^(i+1).
    for j in range(n):
        for d, coef in enumerate(f):
            if j + d < n:
                X[j + d][j] = coef
    X[n - 1][n] = a
    X[n][0] = b
    return X


def observed_profile(X, F):
    n = len(X)
    ranks = [n]
    power = X
    for k in range(1, n + 2):
        ranks.append(rank(power, F))
        if ranks[-1] == 0:
            break
        power = multiply(power, X, F)
    assert ranks[-1] == 0
    return tuple(ranks)


def formula_profile(f, a, b, n, F):
    s = next((i for i, x in enumerate(f) if x), n)
    if s <= n - 2:
        r1 = n - s
    elif s == n - 1:
        r1 = 2 if a and b else 1
    else:
        r1 = int(bool(a)) + int(bool(b))
    if 2 * s < n - 1:
        r2 = n - 2 * s
    elif 2 * s == n - 1:
        r2 = int(F.add(F.mul(f[s], f[s]), F.mul(a, b)) != 0)
    else:
        r2 = int(bool(a) and bool(b))
    ranks = [n + 1, r1, r2]
    for k in range(3, n + 2):
        ranks.append(max(n - k * s, 0))
        if ranks[-1] == 0:
            break
    while len(ranks) > 2 and ranks[-2] == 0:
        ranks.pop()
    return tuple(ranks)


def partition(profile):
    r = list(profile) + [0]
    parts = []
    for k in range(1, len(r) - 1):
        cnt = r[k - 1] - 2 * r[k] + r[k + 1]
        assert cnt >= 0
        parts.extend([k] * cnt)
    return tuple(sorted(parts, reverse=True))


def theorem_census(n, q):
    counts = Counter()
    def register(s, r1, r2, count):
        ranks = [n + 1, r1, r2]
        for k in range(3, n + 2):
            ranks.append(max(n - k * s, 0))
            if ranks[-1] == 0:
                break
        counts[partition(ranks)] += count
    for s in range(1, n - 1):
        fs = (q - 1) * (q ** (n - s - 1))
        if 2 * s < n - 1:
            register(s, n - s, n - 2 * s, q*q*fs)
        elif 2 * s == n - 1:
            register(s, n - s, 1, fs*(q*q-q+1))
            register(s, n - s, 0, fs*(q-1))
        else:
            register(s, n - s, 1, fs*(q-1)**2)
            register(s, n - s, 0, fs*(2*q-1))
    counts[(1,)*(n+1)] += 1
    counts[(2,) + (1,)*(n-1)] += (q-1)*(2*q+1)
    counts[(3,) + (1,)*(n-2)] += q*(q-1)**2
    assert sum(counts.values()) == q**(n+1)
    return counts


def run_one(n, F):
    n_cases = 0
    c = Counter()
    for coeff in product(range(F.q), repeat=n-1):
        f = (0,) + coeff
        for a in range(F.q):
            for b in range(F.q):
                X = make_matrix(f, a, b, n, F)
                measured = observed_profile(X, F)
                predicted = formula_profile(f, a, b, n, F)
                if measured != predicted:
                    raise AssertionError((n, F.q, f, a, b, measured, predicted))
                c[partition(measured)] += 1
                n_cases += 1
    assert c == theorem_census(n, F.q), (n, F.q, c, theorem_census(n, F.q))
    print(f'PASS q={F.q:>2} n={n} matrices={n_cases:>7} distinct_Jordan_types={len(c):>2}')
    return n_cases


def main():
    cases = [
        (Field(2), [3, 4, 5, 6, 7]),
        (Field(3), [3, 4, 5, 6]),
        (Field(5), [3, 4, 5]),
        (Field(7), [3, 4]),
        (Field(2, [1, 1, 1]), [3, 4, 5]),
        (Field(3, [1, 0, 1]), [3, 4]),
    ]
    total = 0
    for F, sizes in cases:
        for n in sizes:
            total += run_one(n, F)
    print(f'ALL PASS: {total} matrices, {sum(len(x[1]) for x in cases)} field/size configurations.')


if __name__ == '__main__':
    main()
