"""Finite diagnostic checks for a rank-four even lattice family.

Mathematical proof of the unbounded assertions is in RESULT.md. The
coordinate box below is diagnostic, not an exhaustive infinite search.
Standard-library Python 3 only.
"""
from itertools import product
from math import isqrt


def gram(t):
    return ((2, t, t, t), (t, -2, 4, 4), (t, 4, -2, 4), (t, 4, 4, -2))


def pairing(t, a, b):
    g = gram(t)
    return sum(a[i] * g[i][j] * b[j] for i in range(4) for j in range(4))


def predicted(t):
    e = [(0, int(i == 0), int(i == 1), int(i == 2)) for i in range(3)]
    others = [(t, -v[1], -v[2], -v[3]) for v in e]
    return e, others


def bounded_root_search(t, limit=6):
    observed = set()
    for y in product(range(-limit, limit + 1), repeat=3):
        S, T = sum(y), sum(z*z for z in y)
        square = (t*t - 8)*S*S + 12*T - 4
        if square < 0:
            continue
        d = isqrt(square)
        if d*d != square:
            continue
        for d_signed in {d, -d}:
            if (d_signed - t*S) % 2:
                continue
            v = ((d_signed - t*S)//2,) + y
            assert pairing(t, v, v) == -2
            observed.add(v)
    assert observed
    least = min(abs(pairing(t, (1,0,0,0), r)) for r in observed)
    e, other = predicted(t)
    minimal = {r for r in observed if pairing(t, (1,0,0,0), r) == t}
    assert least == t
    assert minimal == set(e + other)
    return len(observed)


def run():
    for t in (3, 15, 27, 39):
        h = (1,0,0,0)
        e, other = predicted(t)
        for i in range(3):
            a, b = e[i], other[i]
            assert pairing(t, a, a) == pairing(t, b, b) == -2
            assert pairing(t, h, a) == pairing(t, h, b) == t
            assert pairing(t, a, b) == t*t + 2
            for j in range(3):
                if i != j:
                    assert pairing(t, a, e[j]) == 4
                    assert pairing(t, b, other[j]) == 4
                    assert pairing(t, a, other[j]) == t*t - 4
        # All six generated vectors lie in <e1,e2,e3,t h>.
        # Since (t h-e1)+e1=t h, they generate this lattice,
        # with determinant t relative to the ordered lattice basis.
        assert tuple(e[0][i]+other[0][i] for i in range(4)) == (t,0,0,0)
        count = bounded_root_search(t)
        print(f"t={t}: {count} signed roots in bounded diagnostic search; 6 positive minimal roots")
    print("finite diagnostics passed; the infinite statements are proved separately")

if __name__ == '__main__':
    run()
