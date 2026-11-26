#!/usr/bin/env python3
"""Exact finite checks of the parabola-pair energy and character census."""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, p, relation):
        """The coefficient vector gives the relation X**d = relation(X)."""
        d = len(relation)
        self.q = q = p**d
        digits = [tuple(x // p**i % p for i in range(d)) for x in range(q)]
        code = {a: i for i, a in enumerate(digits)}
        self.add = add = [[code[tuple((u + v) % p for u, v in zip(a, b))]
                           for b in digits] for a in digits]
        self.neg = neg = [row.index(0) for row in add]
        self.sub = [[row[z] for z in neg] for row in add]

        def multiply(a, b):
            z = [0] * (2*d - 1)
            for i, u in enumerate(a):
                for j, v in enumerate(b):
                    z[i+j] += u*v
            for i in range(2*d-2, d-1, -1):
                for j, c in enumerate(relation):
                    z[i-d+j] += z[i]*c
            return code[tuple(v % p for v in z[:d])]

        self.mul = mul = [[multiply(a, b) for b in digits] for a in digits]
        assert all(len(set(row)) == q for row in mul[1:])
        self.square = [row[x] for x, row in enumerate(mul)]
        self.chi = [0] + [-1]*(q-1)
        for x in self.square[1:]:
            self.chi[x] = 1
        assert self.chi.count(1) == (q-1)//2


def energy(F, points, weights):
    """Sum squared ordered two-sum multiplicities with integer weights."""
    n = F.q
    bins = [0]*(n*n)
    for (x, y), a in zip(points, weights):
        X, Y = F.add[x], F.add[y]
        for (u, v), b in zip(points, weights):
            bins[n*X[u] + Y[v]] += a*b
    return sum(v*v for v in bins)


SMALL = {3: (1, 1), 5: (1, 3), 7: (-1, 1), 9: (0, 2),
         11: (-1, 3), 13: (-1, 2)}
TRANSITION = {17: (2, 2), 19: (4, 4), 23: (6, 6),
              25: (4, 8), 27: (6, 6), 29: (4, 4)}


def check(p, relation):
    F = Field(p, relation)
    q, chi, mul, sub = F.q, F.chi, F.mul, F.sub
    opposite = F.neg[1]
    P = list(enumerate(F.square))
    first = [sub[mul[2][x]][1] for x in range(q)]
    second = [mul[x][sub[2][x]] for x in range(q)]
    signs = {x: (chi[first[x]], chi[second[x]]) for x in range(2,q)}
    D = {}
    base = 22*q*q - 54*q + 33
    for x, (a, b) in signs.items():
        S = P + [(u, mul[x][v]) for u, v in P[1:]]
        assert len(set(S)) == 2*q-1
        E = energy(F, S, [1]*len(S))
        assert energy(F, S, [2]+[1]*(len(S)-1)) == 22*q*q-6*q
        D[x], rem = divmod(E-base, 4*(q-1))
        assert rem == 0 and D[x] == -a-b+(x == opposite), (q, x, E)

    counts = Counter(pair for pair in signs.values() if 0 not in pair)
    T = sum(chi[mul[u][v]] for u, v in zip(first, second))
    R = 1+chi[opposite]+chi[3 % p]
    for s, t in product((-1, 1), repeat=2):
        if p == 3:
            numerator = q-3-(1+chi[opposite])*(s+t+s*t)
        else:
            numerator = q-4-(s+t)*R+s*t*(T-1)
        assert 4*counts[s,t] == numerator, (q, s, t)

    if q in TRANSITION:
        regular = Counter(pair for x, pair in signs.items() if x != opposite)
        assert (regular[1,1], regular[-1,-1]) == TRANSITION[q], q
    assert (min(D.values()), max(D.values())) == SMALL.get(
        q, (-2, 3 if q % 3 == 2 else 2)), q
    if q >= 17:
        minimizers = {x for x, d in D.items() if d == min(D.values())}
        maximizers = {x for x, d in D.items() if d == max(D.values())}
        assert minimizers == {x for x in signs if x != opposite and signs[x] == (1,1)}
        assert maximizers == ({opposite} if q % 3 == 2 else
                              {x for x in signs if x != opposite and signs[x] == (-1,-1)})
    return q-2


if __name__ == '__main__':
    primes = [(p, (0,)) for p in (3,5,7,11,13,17,19,23,29,31)]
    extensions = [(3,(2,0)), (5,(3,0)), (3,(2,1,0)), (7,(6,0))]
    total = 0
    for p, relation in primes + extensions:
        n = check(p, relation)
        total += n
        print('field', n+2, 'parameters', n)
    print('DIRECT_ENERGY_CHECK_OK', total)
