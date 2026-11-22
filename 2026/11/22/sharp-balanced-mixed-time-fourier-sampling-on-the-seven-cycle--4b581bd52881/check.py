#!/usr/bin/env python3
"""Independent exact-arithmetic audit of a seven-point mixed Fourier design.

No external dependencies.  All matrix entries are represented in Z[zeta_7],
not by floating-point approximations.  Run: python check.py
"""
from itertools import combinations, permutations

N = 7
ZERO = (0,) * N
REPS = [
    ((0, 1, 2), (0, 1, 2), 147, (112, -350, -350)),
    ((0, 1, 2), (0, 1, 3), 294, (-938, 0, 0)),
    ((0, 1, 2), (0, 1, 4), 147, (-938, 0, 350)),
    ((0, 1, 2), (0, 2, 4), 147, (-238, 350, 0)),
    ((0, 1, 3), (0, 1, 2), 294, (-938, 0, 0)),
    ((0, 1, 3), (0, 1, 3), 98, (-63, 0, 0)),
    ((0, 1, 3), (0, 1, 5), 98, (-63, 0, 0)),
]


def mon(k):
    return tuple(int(i == k % N) for i in range(N))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k*x for x in a)


def mul(a, b):
    result = [0]*N
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                result[(i+j) % N] += x*y
    return tuple(result)


def summands(xs):
    out = ZERO
    for x in xs:
        out = add(out, x)
    return out


def determinant(M):
    out = ZERO
    for p in permutations(range(3)):
        parity = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        term = mul(mul(M[0][p[0]], M[1][p[1]]), M[2][p[2]])
        out = sub(out, term) if parity & 1 else add(out, term)
    return out


def to_u(c):
    assert all(c[i] == c[-i % N] for i in range(1, 4))
    # u=zeta+zeta^-1; u^2=2+zeta^2+zeta^-2;
    # zeta^3+zeta^-3=1-u-u^2.
    return (c[0]-2*c[2]+c[3], c[1]-c[3], c[2]-c[3])


def gram(t, c):
    return [[summands(mon((tj-ti)*k) for k in c) for tj in t] for ti in t]


def shifted(G):
    return [[sub(scale(G[i][j], 5), scale(mon(0), 7)) if i == j
             else scale(G[i][j], 5) for j in range(3)] for i in range(3)]


def invariants(t, c):
    G = gram(t, c)
    M = shifted(G)
    s2 = summands(sub(mul(G[i][i], G[j][j]), mul(G[i][j], G[j][i]))
                   for i in range(3) for j in range(i+1, 3))
    minor2 = sub(mul(M[0][0], M[1][1]), mul(M[0][1], M[1][0]))
    return tuple(map(to_u, (determinant(M), determinant(G), s2, minor2)))


def orbit(t, c):
    return {
        (tuple(sorted((a*x+b) % N for x in t)),
         tuple(sorted((pow(a, -1, N)*y+d) % N for y in c)))
        for a in range(1, N) for b in range(N) for d in range(N)
    }


def progression_product(t, c):
    # Detect the unique center of each 3-term progression, if any.
    steps = []
    for triple in (t, c):
        choices = [(triple[1]-triple[0]) % N] if False else []
        for mid in triple:
            ends = [v for v in triple if v != mid]
            if (ends[0]+ends[1]-2*mid) % N == 0:
                choices = [(ends[0]-mid) % N]
        if len(choices) != 1:
            return False
        steps.append(choices[0])
    return (steps[0]*steps[1]) % N in (2, N-2)


def main():
    pairs = {(t,c) for t in combinations(range(N),3) for c in combinations(range(N),3)}
    assert len(pairs) == 1225
    covered = set()
    winner_orbit = set()
    for t,c,n,expected_det in REPS:
        oc = orbit(t,c)
        assert not covered.intersection(oc), (t,c)
        assert len(oc) == n
        covered.update(oc)
        if (t,c) == ((0,1,2),(0,2,4)):
            winner_orbit = oc
        det, gram_det, s2, minor2 = invariants(t,c)
        assert det == expected_det, (t,c,det)
        assert gram_det in ((21,-7,-7),(7,0,0),(0,0,7),
                            (14,7,0),(14,0,0)), (t,c,gram_det)
        assert all(invariants(tt,cc)[0] == det for tt,cc in oc), (t,c)
        print('orbit',t,c,'size',n,'det(5G-7I)',det,'detG',gram_det)
    assert covered == pairs
    assert len(winner_orbit) == 147
    assert {pair for pair in pairs if progression_product(*pair)} == winner_orbit
    assert invariants((0,1,2),(0,2,4)) == (
        (-238,350,0),(14,7,0),(22,3,0),(64,25,-25))
    # Exact sign certificate: 6/5 < u < 5/4. u solves u^3+u^2-2u-1=0.
    # All losing determinants are negative throughout this rational interval.
    from fractions import Fraction
    lo, hi = Fraction(6,5), Fraction(5,4)
    assert 112-350*lo-350*lo*lo < 0
    assert -938+350*hi*hi < 0
    assert -938 < 0 and -63 < 0
    # Winning matrix M=5G-7I has Sylvester minors 8,64+25u-25u^2,
    # -238+350u, each positive throughout the interval.
    assert 64+25*hi-25*hi*hi > 0
    assert -238+350*lo > 0
    print('PASS: 1,225 configurations; 7 affine orbits; 147 exact optimizers')


if __name__ == '__main__':
    main()
