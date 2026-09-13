"""Finite-field characteristic-polynomial counts for cone extended Shi type B deletions.

Runs from the workspace dir (numpy available there).
cShi(B_l,k): cone in C^{l+1}; affine slice z=1 has hyperplanes
  x_i = m, x_i - x_j = m, x_i + x_j = m, m in S={-k+1..k}.
chi(D,p) = # complement points in F_p^{l+1} for good primes p.
"""
import numpy as np
import itertools, json, sys


def aff_count(l, S, p, skip=None):
    """# y in F_p^l avoiding all affine Shi hyperplanes except `skip`.

    skip: None, ('c', m0) coord x_1=m0, ('d', m0) diff x1-x2=m0,
          ('s', m0) sum x1+x2=m0. (0-based: coord i=0, pair (0,1).)
    """
    Smod = sorted({m % p for m in S})
    grid = np.indices((p,) * l).reshape(l, -1).T  # N x l
    N = grid.shape[0]
    forb = np.zeros(N, dtype=bool)

    def bad_vals(col, skip_m):
        if skip_m is None:
            return np.isin(col, Smod)
        r0 = skip_m % p
        rest = [v for v in Smod if v != r0]
        return np.isin(col, rest)

    for i in range(l):
        sm = None
        if skip is not None and skip[0] == 'c' and i == 0:
            sm = skip[1]
        forb |= bad_vals(grid[:, i], sm)
    for i in range(l):
        for j in range(i + 1, l):
            d = (grid[:, i] - grid[:, j]) % p
            s = (grid[:, i] + grid[:, j]) % p
            smd = skip[1] if (skip is not None and skip[0] == 'd' and i == 0 and j == 1) else None
            sms = skip[1] if (skip is not None and skip[0] == 's' and i == 0 and j == 1) else None
            forb |= bad_vals(d, smd)
            forb |= bad_vals(s, sms)
    return int((~forb).sum())


def weyl_B_count(l, p):
    """# y in F_p^l avoiding x_i=0, x_i-x_j=0, x_i+x_j=0."""
    grid = np.indices((p,) * l).reshape(l, -1).T
    N = grid.shape[0]
    forb = np.zeros(N, dtype=bool)
    for i in range(l):
        forb |= (grid[:, i] == 0)
    for i in range(l):
        for j in range(i + 1, l):
            forb |= ((grid[:, i] - grid[:, j]) % p == 0)
            forb |= ((grid[:, i] + grid[:, j]) % p == 0)
    return int((~forb).sum())


def chi_at_p(l, k, p, skip):
    S = list(range(-k + 1, k + 1))
    if skip == ('z',):
        n_aff = aff_count(l, S, p, None)
        c0 = weyl_B_count(l, p)
        return (p - 1) * n_aff + c0
    n_aff = aff_count(l, S, p, skip)
    return (p - 1) * n_aff


def interp_poly(pts):
    """Interpolate integer-coeff polynomial through (x,y) pts (overdetermined ok).

    Returns coeff list lows-to-high if exact fit on all pts, else None.
    Uses rational Gaussian elimination on first n+1 pts (n = degree guess),
    then verifies. Degree guess = len(pts)-1 down to ... we know degree = l+1;
    pass degree explicitly.
    """
    return None  # placeholder


def fit_chi(pts, deg):
    """Least-squares-free exact fit: solve Vandermonde on first deg+1 pts over
    QQ (via numpy rational-ish: use integer Bareiss), verify on rest."""
    import sympy as sp
    xs = [sp.Integer(x) for x, y in pts[:deg + 1]]
    ys = [sp.Integer(y) for x, y in pts[:deg + 1]]
    V = sp.Matrix([[x ** j for j in range(deg + 1)] for x in xs])
    rhs = sp.Matrix(ys)
    coeff = V.LUsolve(rhs)
    if not all(c.q == 1 for c in coeff):
        # still fine if verification passes; keep rationals
        pass
    ok = True
    for x, y in pts:
        if sum(coeff[j] * (x ** j) for j in range(deg + 1)) != y:
            ok = False
            break
    return list(coeff), ok


def int_roots(coeff):
    """Integer roots of monic-ish integer polynomial (coeff low to high)."""
    import sympy as sp
    t = sp.Symbol('t')
    p = sum(sp.Integer(c) * t ** j for j, c in enumerate(coeff))
    p = sp.expand(p)
    rts = []
    # rational root test on primitive part
    const = int(p.subs(t, 0))
    lead = int(sp.Poly(p, t).LC())
    if const == 0:
        rts.append(0)
        q, r = sp.div(p, t)
        return rts + int_roots(sp.Poly(q, t).all_coeffs()[::-1])
    divs = set()
    for d in range(1, abs(const) + 1):
        if const % d == 0:
            divs |= {d, -d}
    cand = set()
    for d in divs:
        if lead != 0 and (d * lead) != 0:
            # test d/e with e|lead; lead=1 expected
            cand.add(d)
    if lead != 1:
        for e in range(1, abs(lead) + 1):
            if lead % e == 0:
                for d in divs:
                    cand.add(sp.Rational(d, e))
                    cand.add(sp.Rational(d, -e))
    q = p
    for c in sorted(cand, key=lambda z: (abs(z), z)):
        while q.subs(t, c) == 0:
            rts.append(c)
            q, r = sp.div(q, t - c)
            if r != 0:
                break
    return rts, sp.expand(q)


if __name__ == '__main__':
    l = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    ks = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2]
    primes = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [7, 11, 13, 17, 19, 23, 29, 31]
    out = {}
    for k in ks:
        S = list(range(-k + 1, k + 1))
        cases = {'FULL': None}
        for m in S:
            cases[f'c_m{m}'] = ('c', m)
        for m in S:
            cases[f'd_m{m}'] = ('d', m)
        for m in S:
            cases[f's_m{m}'] = ('s', m)
        cases['z_del'] = ('z',)
        res = {}
        for name, skip in cases.items():
            pts = [(p, chi_at_p(l, k, p, skip)) for p in primes if p > 2 * k]
            coeff, ok = fit_chi(pts, l + 1)
            res[name] = {'pts': pts, 'coeff': [str(c) for c in coeff], 'fit_ok': ok}
            print(f'l={l} k={k} {name}: fit_ok={ok} coeff={coeff}', flush=True)
        out[f'l{l}_k{k}'] = res
    with open(f'raw_l{l}.json', 'w') as f:
        json.dump(out, f, indent=1)
