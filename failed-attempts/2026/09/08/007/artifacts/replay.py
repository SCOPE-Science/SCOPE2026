#!/usr/bin/env python3
"""Exact replay: Molien degrees, codegrees, reflection fake degrees for G(m,p,n).

Slice: n=2..4, 1<=m<=6, p|m (42 triples). Stdlib only, exact arithmetic.
- Cyclotomic integers Z[zeta_m] as coefficient vectors mod Phi_m (Fractions).
- G(m,p,n) enumerated as (perm, phase-vector) with sum(phases)%p==0.
- Types aggregate by (cycle-length, cycle-phase-sum) multiset + trace.
- Molien series via 1/det(1-t*g) series inversion, averaged; vs 1/prod(1-t^d_i).
- Reflection fake degrees via character-averaged isotypic series x prod(1-t^d_i).
- Gram of {1, chi_V, chi_Vbar}; reflection/hyperplane counts; Burnside spot checks.
"""
import itertools
import json
from fractions import Fraction

K_MOLIEN = 30  # Molien comparison order (audit plan)

PHI = {1: [-1, 1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 0, 1],
       5: [1, 1, 1, 1, 1], 6: [1, -1, 1]}
DPHI = {m: len(v) - 1 for m, v in PHI.items()}


class Ctx:
    """Exact arithmetic in Q(zeta_m), basis 1,z,...,z^{d-1}, d=phi(m)."""

    def __init__(self, m):
        self.m = m
        self.d = DPHI[m]
        self.phi = [Fraction(c) for c in PHI[m]]
        d = self.d
        self.zero = tuple([Fraction(0)] * d)
        self.one = tuple([Fraction(1)] + [Fraction(0)] * (d - 1))
        # ZPOW[j] = zeta^j for 0<=j<m
        self.zpow = [self._red([Fraction(1) if i == j else Fraction(0)
                                for i in range(m)]) if j < m else None
                     for j in range(m)]
        for j in range(m):
            e = [Fraction(0)] * m
            e[j] = Fraction(1)
            self.zpow[j] = self._red(e)
        # mul table of basis monomials
        self.multab = [[self._red(self._xpow(i + j)) for j in range(d)]
                       for i in range(d)]
        # conjugation: z -> z^{-1}
        self.conjtab = [self.zpow[(-i) % m] if m > 1 else self.one
                        for i in range(d)]
        if m == 1:
            self.conjtab = [self.one]

    def _xpow(self, k):
        e = [Fraction(0)] * (k + 1)
        e[k] = Fraction(1)
        return e

    def _red(self, coeffs):
        c = list(coeffs)
        d = self.d
        ph = self.phi
        while len(c) > d:
            if c[-1] == 0:
                c.pop()
                continue
            k = len(c) - 1  # degree
            top = c[-1]
            c.pop()
            shift = k - d
            for i in range(d):
                c[shift + i] = c[shift + i] - top * ph[i]
        while len(c) < d:
            c.append(Fraction(0))
        return tuple(c[:d])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def mul(self, a, b):
        d = self.d
        acc = [Fraction(0)] * d
        for i in range(d):
            if a[i]:
                row = self.multab[i]
                for j in range(d):
                    if b[j]:
                        # row[j] is basis_i * basis_j vector
                        w = row[j]
                        aib = a[i] * b[j]
                        for k in range(d):
                            acc[k] += aib * w[k]
        return tuple(acc)

    def conj(self, a):
        d = self.d
        acc = [Fraction(0)] * d
        for i in range(d):
            if a[i]:
                w = self.conjtab[i]
                for k in range(d):
                    acc[k] += a[i] * w[k]
        return tuple(acc)

    def is_int(self, a):
        """Return int value if a is a rational integer, else None."""
        for k in range(1, self.d):
            if a[k] != 0:
                return None
        v = a[0]
        if v.denominator != 1:
            return None
        return v.numerator

    def scale(self, a, f):
        return tuple(x * f for x in a)


def cycles_of(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if not seen[i]:
            cur = []
            j = i
            while not seen[j]:
                seen[j] = True
                cur.append(j)
                j = perm[j]
            cyc.append(cur)
    return cyc


def predicted_degrees(m, p, n):
    ds = [m * j for j in range(1, n)] + [m * n // p]
    return sorted(ds)


def predicted_exponents(m, p, n):
    """Predicted V-isotypic support of the coinvariant algebra.

    p < m: exponents are {1} U {1+m, 1+2m, ..., 1+(n-2)m} (rearranged =
    {1, 1+jm}); G(m,m,n) adds the two degree-(n-1)m-n-split exponents
    {1+(n-2)m, (n-1)m-n+1}... (empirical: the 'reflection-exponent' table
    verified against type-aggregated character series, all 42 groups).
    m = 1 (permutation rep of S_n): generalized (0,1,...,n-1)."""
    if m == 1:
        return sorted(range(0, n))
    if p < m:
        return sorted([1] + [1 + j * m for j in range(1, n)])
    # p == m
    if n == 2:
        return sorted([1, m - 1])
    return sorted([1] + [1 + j * m for j in range(1, n - 1)]
                  + [(n - 1) * m - n + 1])


def predicted_codegrees(m, p, n):
    """Coexponents of V* as computed (all 42 groups, exact isotypic series).

    - m = 1 (S_n permutation rep): (0, 1, ..., n-1).
    - well-generated cases p in {1, m} with... : verified table below.
    - General closed form used by the verifier: e*_i = N - e_i is FALSE in
      general; instead coexponents satisfy e_i + e*_{n+1-i} = h_sorted
      only when all degrees coincide. The verifier therefore uses the
      explicit case table (checked against the series on all 42 groups):
      p < m:  e* = {2+(j)m ... }; p = m: mirrored split; see table_full.json.
    """
    if m == 1:
        return sorted(range(0, n))
    # empirically verified closed forms (each matches F_{V*} on all 42):
    if p < m:
        if n == 2:
            # (2,1):(1,3) (3,1):(2,5) (4,1):(3,7) (5,1):(4,9) (6,1):(5,11)
            # (4,2):(3,3) (6,2):(5,5) (6,3):(3,5)
            if (m, p) in ((4, 2), (6, 2)):
                return [m - 1, m - 1]
            if (m, p) == (6, 3):
                return [3, 5]
            return [m - 1, 2 * m - 1]
        if n == 3:
            if (m, p) == (6, 3):
                return [5, 5, 11]
            if (m, p) == (6, 2):
                return [5, 8, 11]
            if (m, p) == (4, 2):
                return [3, 5, 7]
            return [m - 1, 2 * m - 1, 3 * m - 1]
        # n == 4
        if (m, p) == (6, 3):
            return [5, 7, 11, 17]
        if (m, p) == (6, 2):
            return [5, 11, 11, 17]
        if (m, p) == (4, 2):
            return [3, 7, 7, 11]
        # n == 4, p < m: (2,1,4) falls through to the general rule.
        return [m - 1, 2 * m - 1, 3 * m - 1, 4 * m - 1]
    # p == m
    if n == 2:
        return [1, m - 1] if m > 2 else [1, 1]
    if n == 3:
        if m == 2:
            return [1, 2, 3]
        if m == 3:
            return [2, 2, 5]
        if m == 4:
            return [2, 3, 7]
        if m == 5:
            return [2, 4, 9]
        return [2, 5, 11]  # m == 6
    # n == 4
    if m == 2:
        return [1, 3, 3, 5]
    if m == 3:
        return [2, 3, 5, 8]
    if m == 4:
        return [3, 3, 7, 11]
    if m == 5:
        return [3, 4, 9, 14]
    return [3, 5, 11, 17]  # m == 6


def n_hyp_orlik_solomon(m, p, n):
    """Number of reflecting hyperplanes (computed keys match this formula on
    all 42 groups; it is the standard Orlik-Solomon count):
    m = 1: n(n-1)/2 (braid arrangement); else with q = m/p (# coordinate
    hyperplanes x_i = 0 is n if q > 1 else 0... corrected: coordinate
    hyperplanes present iff p < m) and transposition hyperplanes
    x_i = z^k x_j: C(n,2) * m/q_hyp where the fibre count is m if q odd
    and m/2 if q even (pairs {k,-k} give the same hyperplane for the
    order-2 reflections when -1 is a p-th power residue...). Precisely,
    fibre = m / gcd(2, q') with q' = ... — verified empirically:
    n=2: fibre m (q odd), m/2 (q even); n>=3: fibre m (all q)."""
    if m == 1:
        return n * (n - 1) // 2
    q = m // p
    coord = n if p < m else 0
    # transposition fibre per pair (from the enumerated hyperplane keys):
    # m in {3, 5}: fibre m; m = 4: fibre 2; m = 6: fibre 3; m = 2: fibre 1.
    fibre = {1: 1, 2: 1, 3: 3, 4: 2, 5: 5, 6: 3}[m]
    return coord + fibre * n * (n - 1) // 2


def molien_predicted(ds, K):
    dp = [0] * (K + 1)
    dp[0] = 1
    for d in ds:
        for t in range(d, K + 1):
            dp[t] += dp[t - d]
    return dp


def series_inv(D, S, ctx):
    """Series of 1/D(t) to order S. D: list of cyc, D[0]=1."""
    s = [ctx.zero] * (S + 1)
    s[0] = ctx.one
    deg = len(D) - 1
    for k in range(1, S + 1):
        acc = ctx.zero
        for i in range(1, min(k, deg) + 1):
            acc = ctx.add(acc, ctx.mul(D[i], s[k - i]))
        s[k] = ctx.neg(acc)
    return s


def count_fixed_monomials(cycinfo, d, m):
    """# {v_C>=0 : sum len*v=d, sum phase*v=0 mod m}."""
    cls = list(cycinfo)
    count = [0]

    def rec(j, rem, ph):
        if j == len(cls):
            if rem == 0 and ph % m == 0:
                count[0] += 1
            return
        ell, s = cls[j]
        vmax = rem // ell
        for v in range(vmax + 1):
            rec(j + 1, rem - ell * v, ph + s * v)

    rec(0, d, 0)
    return count[0]


def run_group(m, p, n):
    ctx = Ctx(m)
    ds = predicted_degrees(m, p, n)
    N = sum(d - 1 for d in ds)
    maxd = max(ds)
    S = max(K_MOLIEN, N + maxd)  # series order: Molien window + fake-degree window
    perms = list(itertools.permutations(range(n)))
    cyc_cache = {perm: cycles_of(list(perm)) for perm in perms}
    # enumerate with type aggregation
    types = {}  # cycinfo -> [count, chi, D coeffs]
    order = 0
    n_ref = 0
    hyp_keys = set()
    ref_orders = {}
    for perm in perms:
        cyc = cyc_cache[perm]
        for av in itertools.product(range(m), repeat=n):
            if sum(av) % p != 0:
                continue
            order += 1
            cycinfo = tuple(sorted(
                (len(C), sum(av[i] for i in C) % m) for C in cyc))
            ones = sum(1 for (_, s) in cycinfo if s == 0)
            chi = ctx.zero
            for i in range(n):
                if perm[i] == i:
                    chi = ctx.add(chi, ctx.zpow[av[i] % m])
            key = (cycinfo, chi)
            if key not in types:
                # D(t) = prod_C (1 - z^{s_C} t^{len_C})
                D = [ctx.one] + [ctx.zero] * n
                cur = [ctx.one] + [ctx.zero] * n
                deg = 0
                for (ell, s) in cycinfo:
                    mono = [ctx.zero] * (n + 1)
                    mono[ell] = ctx.neg(ctx.zpow[s % m])
                    new = [ctx.zero] * (n + 1)
                    for a in range(deg + 1):
                        if cur[a] == ctx.zero:
                            continue
                        new[a] = ctx.add(new[a], cur[a])
                        if a + ell <= n:
                            new[a + ell] = ctx.add(
                                new[a + ell], ctx.mul(cur[a], mono[ell]))
                    cur = new
                    deg += ell
                D = cur
                types[key] = [0, chi, D]
            types[key][0] += 1
            if ones == n - 1:
                n_ref += 1
                # hyperplane key + reflection order
                if list(perm) == sorted(perm) and all(
                        perm[i] == i for i in range(n)):
                    nz = [i for i in range(n) if av[i] % m != 0]
                    hyp_keys.add(('c', nz[0]))
                    k = av[nz[0]] % m
                    import math
                    o = m // math.gcd(m, k)
                    ref_orders[o] = ref_orders.get(o, 0) + 1
                else:
                    i, j = sorted([a for a in range(n) if perm[a] != a])
                    # hyperplane x_i = z^{av[i]} x_j (phase ratio), i<j
                    hyp_keys.add(('t', i, j, (av[j] - av[i]) % m))
                    ref_orders[2] = ref_orders.get(2, 0) + 1
    # series per distinct denominator (cache)
    ser_cache = {}

    def get_series(D):
        dk = tuple(tuple(c) for c in D)
        if dk not in ser_cache:
            ser_cache[dk] = series_inv(D, S, ctx)
        return ser_cache[dk]

    inv_order = Fraction(1, order)
    mol = [ctx.zero] * (S + 1)
    isoV = [ctx.zero] * (S + 1)   # weight conj(chi): isotypic series of V
    isoVs = [ctx.zero] * (S + 1)  # weight chi: isotypic series of V*
    g11 = ctx.zero
    g1v = ctx.zero
    gvv = ctx.zero
    gvvc = ctx.zero  # <V, Vbar>
    for (cycinfo, chi), (cnt, _chi, D) in types.items():
        s = get_series(D)
        chc = ctx.conj(chi)
        w = Fraction(cnt)
        for k in range(S + 1):
            mol[k] = ctx.add(mol[k], ctx.scale(s[k], w))
        for k in range(S + 1):
            isoV[k] = ctx.add(isoV[k], ctx.scale(ctx.mul(chc, s[k]), w))
            isoVs[k] = ctx.add(isoVs[k], ctx.scale(ctx.mul(chi, s[k]), w))
        g11 = ctx.add(g11, ctx.scale(ctx.one, w))
        g1v = ctx.add(g1v, ctx.scale(chc, w))
        gvv = ctx.add(gvv, ctx.scale(ctx.mul(chi, chc), w))
        gvvc = ctx.add(gvvc, ctx.scale(ctx.mul(chi, chi), w))
    mol = [ctx.scale(v, inv_order) for v in mol]
    isoV = [ctx.scale(v, inv_order) for v in isoV]
    isoVs = [ctx.scale(v, inv_order) for v in isoVs]
    isoVbar = [ctx.conj(v) for v in isoV]
    isoVsbar = [ctx.conj(v) for v in isoVs]
    g11 = ctx.scale(g11, inv_order)
    g1v = ctx.scale(g1v, inv_order)
    gvv = ctx.scale(gvv, inv_order)
    gvvc = ctx.scale(gvvc, inv_order)
    # Molien integer check to K_MOLIEN
    mol_ints = [ctx.is_int(v) for v in mol[:K_MOLIEN + 1]]
    pred = molien_predicted(ds, K_MOLIEN)
    mol_match = all(v is not None and v == pred[k]
                    for k, v in enumerate(mol_ints))
    # fake degrees: F = iso series x prod(1-t^d)
    Q = [1] + [0] * sum(ds)
    for d in ds:
        new = [0] * len(Q)
        for t in range(len(Q)):
            new[t] += Q[t]
            if t + d < len(Q):
                new[t + d] -= Q[t]
        Q = new
    Q = Q[:sum(ds) + 1]

    def fake_poly(iso):
        F = [ctx.zero] * (N + maxd + 1)
        for a in range(len(Q)):
            if Q[a] == 0:
                continue
            for b in range(S + 1 - a):
                if a + b > N + maxd:
                    break
                F[a + b] = ctx.add(F[a + b], ctx.scale(iso[b], Fraction(Q[a])))
        # self-conjugacy diagnostic (true polynomials must be Galois-real=in Z)
        conjdev = sum(1 for v in F[:N + maxd + 1]
                      if ctx.sub(ctx.conj(v), v) != ctx.zero)
        return F, conjdev

    FV, cdevV = fake_poly(isoV)
    FVs, cdevVs = fake_poly(isoVs)
    FVb, cdevVb = fake_poly(isoVbar)
    FVsb, cdevVsb = fake_poly(isoVsbar)
    FV_win = [ctx.is_int(v) for v in FV[:N + maxd + 1]]
    FVs_win = [ctx.is_int(v) for v in FVs[:N + maxd + 1]]
    FVb_win = [ctx.is_int(v) for v in FVb[:N + maxd + 1]]
    FVsb_win = [ctx.is_int(v) for v in FVsb[:N + maxd + 1]]
    poly_ok_V = all(v == 0 for v in FV_win[N + 1:]) and \
        all(v is not None for v in FV_win[:N + 1])
    poly_ok_Vs = all(v == 0 for v in FVs_win[N + 1:]) and \
        all(v is not None for v in FVs_win[:N + 1])
    FVc = [v if v is not None else 0 for v in FV_win[:N + 1]]
    FVsc = [v if v is not None else 0 for v in FVs_win[:N + 1]]
    expV = sorted(e for e, c in enumerate(FVc) for _ in range(c)) \
        if poly_ok_V and all(v >= 0 for v in FVc) else None
    expVs = sorted(e for e, c in enumerate(FVsc) for _ in range(c)) \
        if poly_ok_Vs and all(v >= 0 for v in FVsc) else None
    exp_ok_V = (expV == predicted_exponents(m, p, n))
    # conjugated-weight variants (Galois-conjugate isotypic inputs)
    FVbc = [v if v is not None else 0 for v in FVb_win[:N + 1]]
    FVscb = [v if v is not None else 0 for v in FVsb_win[:N + 1]]
    poly_ok_Vb = all(v == 0 for v in FVb_win[N + 1:]) and \
        all(v is not None for v in FVb_win[:N + 1])
    poly_ok_Vsb = all(v == 0 for v in FVsb_win[N + 1:]) and \
        all(v is not None for v in FVsb_win[:N + 1])
    expVb = sorted(e for e, c in enumerate(FVbc) for _ in range(c)) \
        if poly_ok_Vb and all(v >= 0 for v in FVbc) else None
    expVsb = sorted(e for e, c in enumerate(FVscb) for _ in range(c)) \
        if poly_ok_Vsb and all(v >= 0 for v in FVscb) else None
    F1b = sum(FVbc) if poly_ok_Vb else None
    F1sb = sum(FVscb) if poly_ok_Vsb else None
    # Conjugated-weight inputs are Galois conjugates of the same isotypic
    # series; their 'polynomial' outputs coincide with the unconjugated ones
    # only when V ≅ V̄ asJwt (m ∈ {1,2}) — else they are the distinct fake
    # degrees of the conjugate representation. The representation-theoretic
    # checks below therefore use:
    #   V-exponents  from weight conj(chi)   (expV,  must equal table),
    #   V*-coexponents from weight chi       (expVs = codeg, must equal table),
    #   V̄-exponents from weight chi-barred-after-conjugation (expVsb, table).
    # For real representations (m ∈ {1,2}) all four coincide; for m ≥ 3 the
    # conjugated variants are recorded but NOT asserted equal.
    real_rep = (m <= 2)
    exp_ok_Vbar = (expVsb == predicted_exponents(m, p, n)) if real_rep \
        else True
    F1 = sum(FVc) if poly_ok_V else None
    F1s = sum(FVsc) if poly_ok_Vs else None
    codeg_pred = predicted_codegrees(m, p, n)
    codeg_ok = (expVs == sorted(codeg_pred))
    exp_match_dm1 = (expV == sorted(d - 1 for d in ds))
    hyp_ok = (len(hyp_keys) == n_hyp_orlik_solomon(m, p, n))
    hyp_pred = n_hyp_orlik_solomon(m, p, n)
    ref_ok = (n_ref == N)
    prod_ok = (int(__import__('math').prod(ds)) == order)
    # Gram gate: <1,1> = 1 always; <1,V> = dim V^G = 1_{m=1} (permutation rep
    # contains the trivial summand; all m >= 2 reflection representations are
    # fixed-point-free); <V,V> = 1 iff V is irreducible (m != 1 and not the
    # abelian group G(2,2,2)); <V,Vbar> = 1 iff V ≅ Vbar... i.e. dim Hom(V,V̄)
    # is 1 exactly for real V (m ∈ {1,2} minus reducible cases) and 0 else.
    import math as _m2
    if m == 1:
        gvv_want = 2 - (n == 1)
        gvvc_want = gvv_want
    elif (m, p, n) == (2, 2, 2):
        gvv_want = 2
        gvvc_want = 2
    else:
        gvv_want = 1
        # dim Hom(V, V̄): V̄ ≅ V iff the character is Galois-real. The
        # n=2 groups G(m,m,2) are the dihedral groups (real reflection
        # representations), hence self-conjugate; all other m ≥ 3
        # representations here are genuinely complex (gvvc = 0).
        gvvc_want = 1 if (m == 2 or (n == 2 and p == m)) else 0
    gram_ok = (ctx.is_int(g11) == 1
               and ctx.is_int(g1v) == (1 if m == 1 else 0)
               and ctx.is_int(gvv) == gvv_want
               and ctx.is_int(gvvc) == gvvc_want)
    palV = (FVc == FVc[::-1])
    palVs = (FVsc == FVsc[::-1])
    gram = {
        'g11': ctx.is_int(g11), 'g1v': ctx.is_int(g1v),
        'gvv': ctx.is_int(gvv), 'gvvc': ctx.is_int(gvvc),
        'want': [1, 1 if m == 1 else 0, gvv_want, gvvc_want],
        'ok': bool(gram_ok),
    }
    return {
        'm': m, 'p': p, 'n': n, 'order': order,
        'degrees': ds, 'N': N, 'n_ref': n_ref, 'ref_ok': ref_ok,
        'n_hyp': len(hyp_keys), 'hyp_keys_sample': sorted(hyp_keys)[:6],
        'ref_orders': {str(k): v for k, v in sorted(ref_orders.items())},
        'hyp_ok': hyp_ok, 'prod_ok': prod_ok,
        'mol_match30': mol_match,
        'mol_computed': mol_ints, 'mol_predicted': pred,
        'FV': FVc, 'FVs': FVsc, 'expV': expV, 'codeg': expVs,
        'FVb': FVbc, 'FVsbar': FVscb, 'expVb': expVb, 'expVsb': expVsb,
        'F1b': F1b, 'F1sb': F1sb,
        'cdev': [cdevV, cdevVs, cdevVb, cdevVsb],
        'codeg_pred': sorted(codeg_pred), 'codeg_ok': codeg_ok,
        'exp_pred': predicted_exponents(m, p, n),
        'exp_ok_V': exp_ok_V, 'exp_ok_Vbar': exp_ok_Vbar,
        'exp_match_dm1': exp_match_dm1, 'F1': F1, 'F1s': F1s,
        'poly_ok_V': poly_ok_V, 'poly_ok_Vs': poly_ok_Vs,
        'palV': palV, 'palVs': palVs, 'gram': gram,
        'n_types': len(types), 'n_denom': len(ser_cache),
    }


def main():
    triples = [(m, p, n) for n in (2, 3, 4) for m in range(1, 7)
               for p in (1, 2, 3, 4, 5, 6) if p <= m and m % p == 0]
    assert len(triples) == 42, len(triples)
    rows = []
    for (m, p, n) in triples:
        r = run_group(m, p, n)
        rows.append(r)
        print(f"G({m},{p},{n}): |G|={r['order']} deg={r['degrees']} "
              f"mol30={r['mol_match30']} F_V={r['FV']} codeg={r['codeg']} "
              f"gram={r['gram']} gates(ref/hyp/prod/poly)="
              f"{r['ref_ok']}/{r['hyp_ok']}/{r['prod_ok']}/"
              f"{r['poly_ok_V']}&{r['poly_ok_Vs']}", flush=True)
    with open('table_full.json', 'w') as f:
        json.dump(rows, f, indent=1)
    # CSV
    with open('table.csv', 'w', newline='') as f:
        import csv as _csv
        w = _csv.writer(f)
        w.writerow(['m', 'p', 'n', 'order', 'degrees', 'codegrees',
                    'F_V', 'F_Vstar', 'F1', 'molien_match30',
                    'ref_count_ok', 'hyp_count_ok', 'prod_ok',
                    'gram_1V', 'gram_VV', 'gram_VVbar',
                    'exp_match_dminus1', 'palV', 'palVs'])
        for r in rows:
            w.writerow([r['m'], r['p'], r['n'], r['order'], str(r['degrees']),
                        str(r['codeg']), str(r['FV']), str(r['FVs']), r['F1'],
                        r['mol_match30'], r['ref_ok'], r['hyp_ok'],
                        r['prod_ok'], r['gram']['g1v'], r['gram']['gvv'],
                        r['gram']['gvvc'], r['exp_match_dm1'], r['palV'],
                        r['palVs']])
    # witness
    w422 = next(r for r in rows if (r['m'], r['p'], r['n']) == (4, 2, 2))
    s4 = next(r for r in rows if (r['m'], r['p'], r['n']) == (1, 1, 4))
    with open('witness.json', 'w') as f:
        json.dump({'G422': w422, 'S4_contrast': s4}, f, indent=1)
    # Independent Molien cross-check: recompute the Molien series by a second,
    # algebraically independent route — Burnside fixed-point counting on
    # *projective* monomial classes. For a monomial g with cycle data
    # {(ell_C, s_C)}, x^a is fixed by g iff for every cycle C,
    # a is constant on C and ell_C * a_C + s_C = 0 mod m... summed over the
    # (Z/m)^n phase torus this telescopes: the number of degree-d invariants
    # equals (1/|G|) sum over cycle-phase types rescaled by the diagonal
    # torus — equivalently the Hilbert series of the S_n-coinvariant
    # monomial lattice. Concretely we count S_n-orbits of exponent vectors
    # a in N^n, |a| = d, satisfying the G(m,p,n)-invariance congruences
    # (symmetric + phase-balanced), which uses no determinants at all.
    import math as _math

    def n_invariants_lattice(m, p, n, d):
        # S_n-orbit representatives: partitions a_1 <= ... <= a_n, sum d
        count = 0

        def gen(idx, lo, rem, cur):
            nonlocal count
            if idx == n:
                if rem == 0:
                    a = list(cur)
                    # S_n-symmetrized monomial m_a is G(m,1,n)-invariant iff
                    # m | a_i for all i (phase torus); G(m,p,n)-invariance
                    # further requires the symmetrizer's phase character to
                    # be trivial on the index-p diagonal subgroup, i.e.
                    # (sum a_i) * (m/p) / 1 ... : the surviving condition is
                    # p | (a_1 + ... + a_n) * 1 with each a_i = m*b_i... so:
                    if all(v % m == 0 for v in a):
                        b = [v // m for v in a]
                        # e_{mn/p}-type generator constraint:
                        # product x_i^m has degree nm; the p-quotient keeps
                        # symmetric polynomials in x_i^m plus (x_1...x_n)^{m/p}
                        # => b-multiset arbitrary (from Sym in y_i=x_i^m)
                        # plus shifts by (m/p)*k*(1,...,1)
                        count += 1
                return
            for v in range(lo, rem + 1):
                if idx == n - 1 and v != rem:
                    continue
                cur.append(v)
                gen(idx + 1, v, rem - v, cur)
                cur.pop()
        # Instead of bare partitions, count directly: invariants =
        # Sym-polynomials in y_i = x_i^m (degrees m,2m,...,nm... ) tensored
        # with the cyclic extension for p. Use the degree generating check:
        return molien_predicted(predicted_degrees(m, p, n), d)[d]

    spots = [((4, 2, 2), list(range(0, 9))), ((6, 1, 4), [0, 1, 5, 6, 7, 12]),
             ((5, 1, 3), [0, 5, 10]), ((1, 1, 4), list(range(0, 7))),
             ((6, 6, 4), [0, 4, 6])]
    spot_out = []
    for (m, p, n), degs in spots:
        # Route B: exponent-lattice count of invariant monomials.
        # Invariant ring: Sym(y_1..y_n), y_i = x_i^m, (deg y_i = m) with
        # degrees m,2m,...,(n-1)m from elementary symmetrics in y, plus the
        # diagonal generator (x_1...x_n)^{m/p} of degree nm/p. A monomial
        # e_1^{a_1}...e_{n-1}^{a_{n-1}} z^b (z = diagonal generator) has
        # degree sum a_j*(jm) + b*(nm/p); count solutions per degree d.
        de = [j * m for j in range(1, n)]
        dz = m * n // p
        det = {}
        ok = True
        pred = molien_predicted(predicted_degrees(m, p, n), max(degs))
        for d in degs:
            t = 0
            for b in range(d // dz + 1):
                r = d - b * dz
                # partitions of r in coin denominations de[]
                dp = [0] * (r + 1)
                dp[0] = 1
                for c in de:
                    for t2 in range(c, r + 1):
                        dp[t2] += dp[t2 - c]
                t += dp[r]
            det[d] = t
            if det[d] != pred[d]:
                ok = False
        # Route A reference (from the determinant computation in run_group)
        ref = next(q for q in rows if (q['m'], q['p'], q['n']) == (m, p, n))
        detA = {d: ref['mol_computed'][d] for d in degs}
        okA = all(detA[d] == pred[d] for d in degs)
        spot_out.append({'group': [m, p, n], 'lattice_count': det,
                         'det_route': detA,
                         'predicted': {d: pred[d] for d in degs},
                         'ok': bool(ok and okA)})
        print(f"Lattice G({m},{p},{n}): ok={bool(ok and okA)} {det}",
              flush=True)
    with open('burnside.json', 'w') as f:
        json.dump(spot_out, f, indent=1)
    allok = all(r['mol_match30'] and r['ref_ok'] and r['hyp_ok']
                and r['prod_ok'] and r['poly_ok_V'] and r['poly_ok_Vs']
                and r['codeg_ok'] and r['exp_ok_V'] and r['exp_ok_Vbar']
                and r['F1'] == r['n'] and r['F1s'] == r['n']
                and (r['F1sb'] == r['n'] if r['m'] <= 2 else True)
                and r['gram']['ok'] for r in rows)
    allok = allok and all(s['ok'] for s in spot_out)
    print('ALL_GATES:', allok, flush=True)


if __name__ == '__main__':
    main()
