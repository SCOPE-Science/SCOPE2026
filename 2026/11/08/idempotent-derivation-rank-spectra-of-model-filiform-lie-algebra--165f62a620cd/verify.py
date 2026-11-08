"""Finite-field verification of the idempotent-derivation rank spectrum.

Run: python verify.py
This script constructs the full linear space of derivations from the bracket
relations, then enumerates its idempotents. It does not use the proof's
parameterization of derivations.
"""
from itertools import product
from collections import Counter


class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
        self.char = 2 if q in (2, 4) else q

    def add(self, a, b):
        return a ^ b if self.char == 2 else (a + b) % self.char

    def neg(self, a):
        return a if self.char == 2 else (-a) % self.char

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        out = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    out ^= [1, 2, 3][i + j]  # x^2=x+1
        return out

    def inv(self, a):
        assert a
        return next(b for b in range(1, self.q) if self.mul(a, b) == 1)


def bracket(x, y, field):
    d = len(x)
    z = [0] * d
    for j in range(1, d - 1):
        z[j + 1] = field.sub(field.mul(x[0], y[j]), field.mul(y[0], x[j]))
    return z


def error(D, i, j, field):
    d = len(D)
    ei = [int(k == i) for k in range(d)]
    ej = [int(k == j) for k in range(d)]
    cb = bracket(ei, ej, field)
    lhs = [0] * d
    for r in range(d):
        for k in range(d):
            lhs[r] = field.add(lhs[r], field.mul(D[r][k], cb[k]))
    Di = [D[r][i] for r in range(d)]
    Dj = [D[r][j] for r in range(d)]
    rhs1 = bracket(Di, ej, field)
    rhs2 = bracket(ei, Dj, field)
    return [field.sub(lhs[k], field.add(rhs1[k], rhs2[k])) for k in range(d)]


def derivation_space_basis(n, field):
    d = n + 1
    columns = []
    for r in range(d):
        for c in range(d):
            E = [[0] * d for _ in range(d)]
            E[r][c] = 1
            v = []
            for i in range(d):
                for j in range(i + 1, d):
                    v += error(E, i, j, field)
            columns.append(v)
    M = [list(row) for row in zip(*columns)]
    pivots = []
    rank = 0
    for c in range(d * d):
        pivot = next((r for r in range(rank, len(M)) if M[r][c] != 0), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = field.inv(M[rank][c])
        M[rank] = [field.mul(inv, v) for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][c]:
                scale = M[r][c]
                M[r] = [field.sub(M[r][j], field.mul(scale, M[rank][j])) for j in range(d * d)]
        pivots.append(c)
        rank += 1
    free = [j for j in range(d * d) if j not in pivots]
    answer = []
    for f in free:
        v = [0] * (d * d)
        v[f] = 1
        for i, p in enumerate(pivots):
            v[p] = field.neg(M[i][f])
        answer.append(v)
    assert len(answer) == 2 * n + 1, (n, field.q, len(answer))
    return answer


def matrank(D, field):
    M = [row[:] for row in D]
    d = len(M)
    r = 0
    for c in range(d):
        p = next((i for i in range(r, d) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = field.inv(M[r][c])
        M[r] = [field.mul(inv, x) for x in M[r]]
        for i in range(r + 1, d):
            if M[i][c]:
                t = M[i][c]
                M[i] = [field.sub(M[i][j], field.mul(t, M[r][j])) for j in range(d)]
        r += 1
    return r


def idempotent(D, field):
    d = len(D)
    for i in range(d):
        for j in range(d):
            t = 0
            for k in range(d):
                t = field.add(t, field.mul(D[i][k], D[k][j]))
            if t != D[i][j]:
                return False
    return True


def predicted(n, q):
    out = Counter({0: 1, n: q ** n})
    if q in (2, 4):
        if n % 2 == 0:
            out[n // 2 + 1] += 2 * q ** n
        else:
            out[(n + 1) // 2] += q ** n
            out[(n + 3) // 2] += q ** (n - 1)
    return dict(sorted(out.items()))


def check(n, q):
    field = Field(q)
    basis = derivation_space_basis(n, field)
    d = n + 1
    obs = Counter()
    for coeff in product(range(q), repeat=len(basis)):
        Dflat = [0] * (d * d)
        for scalar, vec in zip(coeff, basis):
            if scalar:
                for j in range(d * d):
                    Dflat[j] = field.add(Dflat[j], field.mul(scalar, vec[j]))
        D = [Dflat[i * d : (i + 1) * d] for i in range(d)]
        if idempotent(D, field):
            obs[matrank(D, field)] += 1
    assert dict(sorted(obs.items())) == predicted(n, q), (n, q, obs, predicted(n, q))
    print(f"CHECK n={n} q={q}: {dict(sorted(obs.items()))}")


if __name__ == "__main__":
    for pair in [(3, 2), (4, 2), (5, 2), (3, 3), (4, 3), (3, 4), (3, 5)]:
        check(*pair)
    print("VERIFY_OK")
