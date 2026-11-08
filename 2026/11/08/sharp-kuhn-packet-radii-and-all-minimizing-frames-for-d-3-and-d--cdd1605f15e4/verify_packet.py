"""Exact integer/rational checks for Euclidean Kuhn packets of FCC and BCC lattices.

Usage: python3 verify_packet.py
No third-party libraries or network access needed.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import Counter


def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))


def sub(u, v):
    return tuple(u[i] - v[i] for i in range(3))


def dot(u, v):
    return sum(u[i] * v[i] for i in range(3))


def norm2(v):
    return dot(v, v)


def det(u, v, w):
    return (u[0] * (v[1]*w[2]-v[2]*w[1])
            -u[1] * (v[0]*w[2]-v[2]*w[0])
            +u[2] * (v[0]*w[1]-v[1]*w[0]))


def center(*ps):
    return tuple(sum((F(p[j]) for p in ps), F()) / len(ps) for j in range(3))


def verify(kind):
    limit = 4 if kind == "FCC" else 5
    def in_lattice(v):
        if kind == "FCC":
            return sum(v) % 2 == 0
        return v[0] % 2 == v[1] % 2 == v[2] % 2

    short = sorted(v for v in product(range(-2,3), repeat=3)
                   if 0 < norm2(v) <= limit and in_lattice(v))
    assert len(short) == (18 if kind == "FCC" else 14)
    surviving = []
    for B in combinations(short, 3):
        if det(*B) == 0:
            continue
        subset_sums = [add(*(B[j] for j in J))
                       for size in (1, 2, 3)
                       for J in combinations(range(3), size)]
        if max(map(norm2, subset_sums)) <= limit:
            surviving.append(B)
    assert len(surviving) == (24 if kind == "FCC" else 8)
    counts = Counter()
    for B in surviving:
        grams = sorted(dot(B[i], B[j]) for i, j in combinations(range(3), 2))
        if kind == "FCC":
            assert sorted(map(norm2, B)) == [2, 2, 2]
            assert grams == [-1, -1, 0]
            assert abs(det(*B)) == 2
        else:
            assert sorted(map(norm2, B)) == [3, 3, 3]
            assert grams == [-1, -1, -1]
            assert abs(det(*B)) == 4
        for q in permutations(B):
            p0 = (0, 0, 0)
            p1 = q[0]
            p2 = add(q[0], q[1])
            p3 = add(*q)
            pts = (p0, p1, p2, p3)
            if kind == "BCC":
                c = center(*pts)
                assert all(norm2(sub(p, c)) == F(5,4) for p in pts)
                counts[F(5,4)] += 1
            else:
                diameter = [(pts[i], pts[j]) for i, j in combinations(range(4), 2)
                            if norm2(sub(pts[i], pts[j])) == 4]
                if diameter:
                    c = center(*diameter[0])
                    assert all(norm2(sub(p, c)) == 1 for p in pts)
                    counts[F(1)] += 1
                else:
                    assert all(norm2(sub(pts[i], pts[j])) == 2
                               for i, j in combinations(range(4), 2))
                    c = center(*pts)
                    assert all(norm2(sub(p, c)) == F(3,4) for p in pts)
                    counts[F(3,4)] += 1
    if kind == "FCC":
        assert counts == Counter({F(1): 96, F(3,4): 48})
        print("FCC_PASS 24 unordered optimal frames; 144 ordered frames; 96 radius^2=1 and 48 radius^2=3/4 packet simplices")
    else:
        assert counts == Counter({F(5,4): 48})
        print("BCC_PASS 8 unordered optimal frames; 48 ordered frames; all 48 doubled-coordinate packet simplices have radius^2=5/4")


if __name__ == "__main__":
    verify("FCC")
    verify("BCC")
