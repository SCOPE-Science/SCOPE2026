from collections import Counter
from math import comb

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for rest in partitions(n - x, x):
            yield (x,) + rest

def labels(parts):
    out = []
    for i, a in enumerate(parts):
        out += [i] * a
    return out

def direct_J(parts):
    lab = labels(parts)
    n = len(lab)
    c = Counter()
    for mask in range(1 << n):
        W = [v for v in range(n) if (mask >> v) & 1]
        ext = 0
        for u in range(n):
            if (mask >> u) & 1:
                continue
            if any(lab[u] != lab[v] for v in W):
                ext += 1
        c[(len(W), ext)] += 1
    return c

def formula_J(parts):
    n = sum(parts)
    c = Counter()
    c[(0, 0)] = 1
    for s in range(1, n + 1):
        one_part = 0
        for a in parts:
            if s <= a:
                q = comb(a, s)
                c[(s, n - a)] += q
                one_part += q
        cross = comb(n, s) - one_part
        if cross:
            c[(s, n - s)] += cross
    return c

def direct_D(parts):
    lab = labels(parts)
    n = len(lab)
    coeff = [0] * (n + 1)
    for mask in range(1 << n):
        if mask == 0:
            continue
        dominated = True
        for u in range(n):
            if (mask >> u) & 1:
                continue
            if not any(((mask >> v) & 1) and lab[u] != lab[v] for v in range(n)):
                dominated = False
                break
        if dominated:
            coeff[mask.bit_count()] += 1
    return tuple(coeff)

def formula_D(parts):
    n = sum(parts)
    r = len(parts)
    coeff = [comb(n, k) for k in range(n + 1)]
    for a in parts:
        for k in range(a + 1):
            coeff[k] -= comb(a, k)
        coeff[a] += 1
    coeff[0] += r - 1
    return tuple(coeff)

def reconstruct_from_J(c):
    n = max(s for s, _ in c)
    p = []
    for t in range(1, n):
        q = c.get((1, n - t), 0)
        assert q % t == 0
        p += [t] * (q // t)
    return tuple(sorted(p))

def poly_sub(a, b):
    n = max(len(a), len(b))
    return [ (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n) ]

def A(t):
    # (1+x)^t - x^t - 1
    a = [comb(t, k) for k in range(t + 1)]
    a[0] -= 1
    a[t] -= 1
    return a

def reconstruct_from_D(coeff):
    n = len(coeff) - 1
    oneplus = [comb(n, k) for k in range(n + 1)]
    q = poly_sub(oneplus, list(coeff))  # Q=(1+x)^n-D
    # Q = 1 + sum_{t>=2} m_t A_t
    work = q[:]
    p = []
    while True:
        d = max((i for i, v in enumerate(work) if i > 0 and v != 0), default=None)
        if d is None:
            break
        t = d + 1
        assert work[d] % t == 0, (coeff, work, d)
        m = work[d] // t
        assert m > 0
        p += [t] * m
        at = A(t)
        for i, v in enumerate(at):
            work[i] -= m * v
    assert work[0] == 1 and all(v == 0 for v in work[1:]), work
    used = sum(p)
    p += [1] * (n - used)
    return tuple(sorted(p))

types = subsets = 0
J_sigs = {}
D_sigs = {}
for n in range(2, 11):
    for p in partitions(n):
        if len(p) < 2:
            continue
        j0 = direct_J(p)
        j1 = formula_J(p)
        assert j0 == j1, ("J", p)
        d0 = direct_D(p)
        d1 = formula_D(p)
        assert d0 == d1, ("D", p, d0, d1)
        assert reconstruct_from_J(j0) == p, ("J-inverse", p)
        assert reconstruct_from_D(d0) == p, ("D-inverse", p, reconstruct_from_D(d0))
        js = tuple(sorted(j0.items()))
        ds = d0
        assert js not in J_sigs or J_sigs[js] == p
        assert ds not in D_sigs or D_sigs[ds] == p
        J_sigs[js] = p
        D_sigs[ds] = p
        types += 1
        subsets += 1 << n

formula_types = 0
D_formula_sigs = {}
for n in range(2, 31):
    for p in partitions(n):
        if len(p) < 2:
            continue
        d = formula_D(p)
        assert reconstruct_from_D(d) == p, ("large-D-inverse", p)
        assert d not in D_formula_sigs or D_formula_sigs[d] == p
        D_formula_sigs[d] = p
        formula_types += 1

print("VERIFY_OK")
print("definition_level_types =", types)
print("vertex_subsets_checked_per_polynomial =", subsets)
print("ordinary_D_formula_and_inverse_types_through_30 =", formula_types)
print("J_collisions_checked = 0")
print("D_collisions_checked = 0")
