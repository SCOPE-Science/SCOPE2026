"""Exact checks for planar area shells of cycle cosmological polytopes.
Only the standard coordinate model and a published two-face criterion are used.
All planar areas are computed through exact squared distances.
"""
from collections import Counter
from itertools import combinations
from fractions import Fraction


def vertices(n):
    out = []
    for i in range(n):
        j = (i + 1) % n
        for kind, entries in enumerate((
            ((i, 1), (j, 1), (n + i, -1)),
            ((i, 1), (j, -1), (n + i, 1)),
            ((i, -1), (j, 1), (n + i, 1)),
        )):
            v = [0] * (2 * n)
            for k, a in entries:
                v[k] = a
            out.append((i, kind, tuple(v)))
    return out


def d2(a, b):
    return sum((x - y)**2 for x, y in zip(a, b))


def four_area_squared(a, b, c):
    # Heron's identity: 16 Area^2 = 4 A B - (A+B-C)^2
    A, B, C = d2(a, b), d2(b, c), d2(a, c)
    num = 4 * A * B - (A+B-C)**2
    assert num > 0 and num % 4 == 0
    return num // 4


def face_triangles(n):
    # A triple spans a triangular 2-face exactly when:
    # (i) no cluster contributes all 3 vertices;
    # (ii) any doubled cluster contributes the pair of labelled ends (1,2);
    # (iii) for n=3, neither of the two full oriented cycle selections occurs.
    # This is the cycle specialization of the face criterion of Kuehne--Monin.
    vv = vertices(n)
    for tri in combinations(vv, 3):
        clusters = [x[0] for x in tri]
        kinds = [x[1] for x in tri]
        if len(set(clusters)) == 1:
            continue
        if len(set(clusters)) == 2:
            doubled = next(i for i in set(clusters) if clusters.count(i) == 2)
            if {x[1] for x in tri if x[0] == doubled} != {1, 2}:
                continue
        if n == 3 and len(set(clusters)) == 3:
            ordered = [next(x[1] for x in tri if x[0] == i) for i in range(n)]
            if ordered == [1] * n or ordered == [2] * n:
                continue
        yield tri


def formula(n):
    if n == 3:
        return Counter({12: 4, 16: 12, 28: 27})
    t0 = n * (n-4) * (n-5) // 6
    t1 = n * (n-4)
    return Counter({
        15: 8*n,
        20: 15*t1,
        23: 14*n,
        27: 27*t0,
        28: 6*n,
        32: 3*n*(n-3) + 12*t1,
        39: 5*n,
    })


def quadrilateral_area(n, i):
    # The four corners are p_(i-1), q_(i-1) or r_(i-1)
    # and p_i, q_i or r_i with common midpoint x_i.
    vv = vertices(n)
    left = (i-1) % n
    right = i
    P = next(v for e,k,v in vv if e == left and k == 0)
    Q = next(v for e,k,v in vv if e == left and k == 2)
    R = next(v for e,k,v in vv if e == right and k == 0)
    S = next(v for e,k,v in vv if e == right and k == 1)
    # P + Q = R + S = 2 x_i; their diagonals are perpendicular.
    assert tuple(a + b for a,b in zip(P,Q)) == tuple(a + b for a,b in zip(R,S))
    da = tuple(a-b for a,b in zip(P,Q))
    db = tuple(a-b for a,b in zip(R,S))
    assert sum(a*b for a,b in zip(da,db)) == 0
    assert sum(a*a for a in da) == 8 and sum(b*b for b in db) == 8
    return 4


def main():
    for n in range(3, 13):
        hist = Counter(four_area_squared(*(x[2] for x in tr)) for tr in face_triangles(n))
        predicted = formula(n)
        assert hist == predicted, (n, hist, predicted)
        assert sum(hist.values()) == 27 * (n*(n-1)*(n-2)//6) + 3*n*(n-1) - (2 if n == 3 else 0)
        assert all(quadrilateral_area(n,i) == 4 for i in range(n))
        if n >= 4:
            equilateral_count = 27*n*(n-4)*(n-5)//6
            assert hist.get(27,0) == equilateral_count
        print(f"n={n} triangles={sum(hist.values())} squares={n} shells={dict(sorted(hist.items()))}")
    print('COSMO_CYCLE_FACE_AREA_EXACT_PASS n=3..12')

if __name__ == '__main__':
    main()
