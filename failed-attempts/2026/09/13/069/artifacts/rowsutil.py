# Side-effect-free exact helpers (no top-level execution on import).
from fractions import Fraction
import pulp


def le_lin(p, q):
    return ((q - p, 0) if q > p else (q - p + 6, 1))


def rows(M, A, F, wm, wn, e, extra=()):
    R = []

    def add(terms, rhs, sense):
        d = {}
        for i, c in terms:
            d[i] = d.get(i, 0) + c
        R.append((d, rhs, sense))
    for i in range(1, 6):
        for j in range(1, 6):
            s = i + j
            if s < 6:
                add([(s, 1), (i, -1), (j, -1)], 0, '<=')
            elif s > 6:
                add([(s - 6, 1), (i, -1), (j, -1)], 1, '<=')
    for p in M:
        for q in range(1, 6):
            if q == p:
                continue
            d, off = le_lin(p, q)
            add([(q, 1), (p, -1), (d, -1)], -1 - off, '<=')
    for a in A:
        for j in range(1, 6):
            if j == a:
                continue
            d, off = le_lin(j, a)
            add([(a, 1), (j, -1), (d, -1)], -1 - off, '<=')
    for q, p in wm.items():
        d, off = le_lin(q, p)
        add([(p, 1), (q, -1), (d, -1)], off, '>=')
    for j, a in wn.items():
        d, off = le_lin(a, j)
        add([(j, 1), (a, -1), (d, -1)], off, '>=')
    for i in range(1, 6):
        if i == F:
            continue
        add([(F, 6), (i, -6)], i - F, '>=')
    for (i, lo, hi) in extra:
        if lo is not None:
            add([(i, 1)], lo, '>=')
        if hi is not None:
            add([(i, 1)], hi, '<=')
    o = {i: ((e - 1) * 6 if i == F else 0) - e for i in range(1, 6)}
    oc = (e - 1) * (F - 5)
    return o, oc, R


def J(d):
    return {int(k): v for k, v in d.items()}


def check_bound(o, oc, R, U, V, need):
    A1 = [r for r in R if r[2] == '<=']
    A2 = [r for r in R if r[2] == '>=']
    U = [(j, Fraction(v)) for j, v in U]
    V = [(j, Fraction(v)) for j, v in V]
    assert all(v >= 0 for _, v in U + V), "negativity"
    assert all(0 <= j < len(A1) for j, _ in U)
    assert all(0 <= j < len(A2) for j, _ in V)
    for i in range(1, 6):
        s = sum(v * (-A1[j][0].get(i, 0)) for j, v in U) + \
            sum(v * (A2[j][0].get(i, 0)) for j, v in V)
        assert s <= o[i], "dual infeasible at k%d" % i
    b = sum(v * (-A1[j][1]) for j, v in U) + \
        sum(v * (A2[j][1]) for j, v in V) + oc
    assert b >= need, "weak bound %s < %s" % (b, need)
    return b


def check_infeas(R, cert):
    A1 = [r for r in R if r[2] == '<=']
    A2 = [r for r in R if r[2] == '>=']
    Y = [(j, Fraction(v)) for j, v in cert["Y"]]
    Z = [(j, Fraction(v)) for j, v in cert["Z"]]
    assert all(v >= 0 for _, v in Y + Z), "negativity"
    for i in range(1, 6):
        s = sum(v * (-A1[j][0].get(i, 0)) for j, v in Y) + \
            sum(v * (A2[j][0].get(i, 0)) for j, v in Z)
        assert s == 0, "balance k%d=%s" % (i, s)
    v = sum(v * (-A1[j][1]) for j, v in Y) + \
        sum(v * (A2[j][1]) for j, v in Z)
    assert v > 0, "nonpositive ray value"
    return v
