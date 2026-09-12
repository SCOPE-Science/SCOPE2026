"""Finite-level verification that the S-unit cup [2] cup [3] is nonzero.

Model: K = Q(zeta_3, cbrt(2), cbrt(3)) has Gal(K/Q) =: G0 ~= (C3^2) rtimes C2,
with the C2 (complex conjugation) acting on V = C3^2 by inversion.
Kummer classes kappa(2), kappa(3) in H^1(G_S, mu_3) factor through G0
(the cube roots lie in Q_S since x^3-2, x^3-3 ramify only at {2,3}).
Their cup in H^2(G_S, mu_3^{otimes 2}) is the inflation of the cup on G0,
and its restriction to V is the standard cup e1 cup e2 in H^2(C3^2, F3).

This script checks at cochain level (normalized bar resolution, F3):
 (i)  phi_2, phi_3 are 1-cocycles on G0 with values in M1 = mu_3,
 (ii) their cup is a 2-cocycle with values in M2 = mu_3^{otimes 2},
 (iii) its restriction to V is NOT a coboundary (hence nonzero in H^2(V)),
 (iv)  it is NOT a coboundary on G0 either (hence nonzero in H^2(G0)).
Nonvanishing mod 3 implies nonvanishing of the Z/9 diagonal cup b cup a
(reduction map: a zero Z/9 class would reduce to zero mod 3).

Pure Python, no dependencies.
"""
import json
import os
import random

MOD = 3

# ---- V = C3^2 (additive notation) ----
V = [(i, j) for i in range(3) for j in range(3)]
ZERO_V = (0, 0)


def addV(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def negV(a):
    return ((-a[0]) % 3, (-a[1]) % 3)


# ---- G0 = V rtimes C2, tau v tau = v^{-1} ----
G = [(v, e) for v in V for e in (0, 1)]
ID = (ZERO_V, 0)


def mul(g, h):
    a, e = g
    b, f = h
    b2 = b if e == 0 else negV(b)
    return (addV(a, b2), (e + f) % 2)


# group sanity (identity + associativity on random triples)
for g in G:
    assert mul(g, ID) == g and mul(ID, g) == g
random.seed(20260912)
for _ in range(300):
    a, b, c = random.choice(G), random.choice(G), random.choice(G)
    assert mul(mul(a, b), c) == mul(a, mul(b, c))


def act1(g, m):
    """Action on M1 = mu_3 (additive F3): V trivial, tau acts by -1."""
    return m if g[1] == 0 else (-m) % 3


def phi(k, g):
    """Kummer 1-cocycle for the k-th radicand.

    phi(v, e) = v[k] (projection), with phi(tau) = 0: the real cube roots
    of 2, 3 are fixed by complex conjugation. Check of case (a,1)(b,1):
    LHS phi(a-b,0) = a[k]-b[k]; RHS phi(a,1)+tau.phi(b,1) = a[k]-b[k]. OK.
    """
    return g[0][k] % 3


# (i) 1-cocycle check: phi(gh) == phi(g) + g.phi(h)
for k in (0, 1):
    for g in G:
        for h in G:
            assert phi(k, mul(g, h)) == (phi(k, g) + act1(g, phi(k, h))) % 3


def cup(g, h):
    """Cup phi_2 cup phi_3: (g,h) |-> phi_2(g) * (g . phi_3(h)) in M2."""
    return (phi(0, g) * act1(g, phi(1, h))) % 3


# (ii) 2-cocycle check (M2 has trivial G0-action mod 3 since chi^2 = 1)
for g in G:
    for h in G:
        for kk in G:
            assert (cup(h, kk) - cup(mul(g, h), kk)
                    + cup(g, mul(h, kk)) - cup(g, h)) % 3 == 0


def cupV(a, b):
    """Restriction to V: e1 cup e2 with trivial action."""
    return (a[0] * b[1]) % 3


# restriction consistency
for a in V:
    for b in V:
        assert cup((a, 0), (b, 0)) == cupV(a, b)


def coboundary_columns(elts, mul_fn):
    """Columns = d(delta_x) for each basis 1-cochain delta_x, trivial action."""
    idx = {g: i for i, g in enumerate(elts)}
    n1 = len(elts)
    pairs = [(g, h) for g in elts for h in elts]
    cols = []
    for x in elts:
        k = idx[x]
        col = []
        for (g, h) in pairs:
            val = (1 if idx[h] == k else 0) - (1 if idx[mul_fn(g, h)] == k else 0) \
                + (1 if idx[g] == k else 0)
            col.append(val % 3)
        cols.append(col)
    return cols


def in_span_mod3(cols, target):
    """Decide whether target is in the span of cols over F3."""
    nrows = len(target)
    ncols = len(cols)
    M = [[cols[c][r] % 3 for c in range(ncols)] + [target[r] % 3]
         for r in range(nrows)]
    piv = 0
    for c in range(ncols):
        pivr = -1
        for r in range(piv, nrows):
            if M[r][c] % 3 != 0:
                pivr = r
                break
        if pivr == -1:
            continue
        M[piv], M[pivr] = M[pivr], M[piv]
        inv = 1 if M[piv][c] == 1 else 2
        M[piv] = [(v * inv) % 3 for v in M[piv]]
        for r in range(nrows):
            if r != piv and M[r][c] % 3 != 0:
                f = M[r][c]
                M[r] = [(M[r][j] - f * M[piv][j]) % 3 for j in range(ncols + 1)]
        piv += 1
    for r in range(nrows):
        if all(M[r][c] == 0 for c in range(ncols)) and M[r][ncols] % 3 != 0:
            return False
    return True


# solver self-tests
test_cols = coboundary_columns(V, lambda a, b: addV(a, b))
zero_t = [0] * 81
assert in_span_mod3(test_cols, zero_t) is True
assert in_span_mod3(test_cols, test_cols[0]) is True  # a coboundary is a coboundary
e00 = [0] * 81
e00[0] = 1  # generic cochain need not be in span; just exercises the solver
_ = in_span_mod3(test_cols, e00)

# (iii) restriction nonzero in H^2(V, F3)?
target_V = [cupV(a, b) for a in V for b in V]
cols_V = coboundary_columns(V, lambda a, b: addV(a, b))
res_is_coboundary = in_span_mod3(cols_V, target_V)

# (iv) cup nonzero in H^2(G0, M2)?
target_G = [cup(g, h) for g in G for h in G]
cols_G = coboundary_columns(G, mul)
cup_is_coboundary = in_span_mod3(cols_G, target_G)

result = {
    "group_order_G0": len(G),
    "phi_are_1_cocycles": True,
    "cup_is_2_cocycle": True,
    "restriction_equals_cupV_on_V": True,
    "restriction_is_coboundary_on_V": res_is_coboundary,
    "restriction_nonzero_in_H2_V": (not res_is_coboundary),
    "cup_is_coboundary_on_G0": cup_is_coboundary,
    "cup_nonzero_in_H2_G0": (not cup_is_coboundary),
    "conclusion": ("mod-3 Kummer cup is nonzero at finite level G0. "
                   "No global claim is made: passage to H^2(G_{Q,S}) needs "
                   "inflation-injectivity / wild-symbol analysis (see DRAFT.md)."),
}
print(json.dumps(result, indent=2))
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "cup_verification.json")
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print("wrote", out_path)
assert res_is_coboundary is False and cup_is_coboundary is False
print("ASSERTIONS PASSED: cup class is nonzero at finite level.")
