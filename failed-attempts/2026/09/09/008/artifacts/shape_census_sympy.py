#!/usr/bin/env python3
"""Complete lex shape-position stratification over the sparse box U (v2).

U = unordered pairs {f,g} of DISTINCT polynomials in Q[x,y], each of total
degree exactly 2 with 2-3 nonzero terms and coefficients in {+1,-1}.

Engine: sympy exact Groebner/resultant/factorization; stdlib Fraction
arithmetic for fiber gcd over Q[t]/(q) on nonlinear root orbits.

Outputs: stratification.csv, summary.json, both_fail_bases.json
"""
import csv
import itertools
import json
import time
from fractions import Fraction

from sympy import QQ, Poly, factor_list, groebner, symbols

x, y = symbols('x y')

MONS = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0)]
MSTR = {(2, 0): 'x^2', (1, 1): 'xy', (0, 2): 'y^2', (1, 0): 'x',
        (0, 1): 'y', (0, 0): '1'}
QUADS = {(2, 0), (1, 1), (0, 2)}


def enum_items():
    polys = []
    for k in (2, 3):
        for supp in itertools.combinations(range(6), k):
            if not any(MONS[m] in QUADS for m in supp):
                continue
            for signs in itertools.product((1, -1), repeat=k):
                d = {}
                for mi, s in zip(supp, signs):
                    d[MONS[mi]] = s
                polys.append(d)
    polys.sort(key=lambda d: (tuple(sorted(d.keys())),
                              tuple(d[m] for m in sorted(d.keys()))))
    out = []
    for d in polys:
        expr = 0
        for (a, b), c in d.items():
            expr = expr + c * (x ** a) * (y ** b)
        out.append((d, expr))
    return out


def pstr(d):
    parts = []
    for m in MONS:
        if m in d:
            c = d[m]
            s = MSTR[m]
            if s == '1':
                parts.append('+1' if c > 0 else '-1')
            else:
                parts.append('+' + s if c > 0 else '-' + s)
    t = ''.join(parts)
    return t[1:] if t.startswith('+') else t


def shape_of(G, top):
    """Structural shape test on a reduced lex GB.

    top == x means lex order x>y: shape is {x-h(y), m(y)}.
    top == y means lex order y>x: shape is {y-h(x), m(x)}.
    """
    ps = [Poly(g, x, y, domain=QQ) for g in G.polys]
    if len(ps) != 2:
        return False
    uni = topc = None
    for p in ps:
        terms = p.as_dict()
        is_uni = (all(a == 0 for (a, b) in terms) if top == x
                  else all(b == 0 for (a, b) in terms))
        if is_uni:
            if uni is not None:
                return False
            uni = p
        else:
            if topc is not None:
                return False
            topc = p
    if uni is None or topc is None:
        return False
    terms = topc.as_dict()
    if top == x:
        if (1, 0) not in terms or terms[(1, 0)] != 1:
            return False
        if any(a not in (0, 1) for (a, b) in terms):
            return False
        if sum(1 for (a, b) in terms if a == 1) != 1:
            return False
    else:
        if (0, 1) not in terms or terms[(0, 1)] != 1:
            return False
        if any(b not in (0, 1) for (a, b) in terms):
            return False
        if sum(1 for (a, b) in terms if b == 1) != 1:
            return False
    return True


def staircase_dim(G):
    """dim_Q Q[x,y]/I from grevlex LT staircase; None if infinite."""
    lts = []
    for g in G.polys:
        d = Poly(g, x, y).as_dict()
        lts.append(max(d.keys(), key=lambda e: (e[0] + e[1], e[0], e[1])))
    xs = [a for (a, b) in lts if b == 0]
    ys = [b for (a, b) in lts if a == 0]
    if not xs or not ys:
        return None
    A, B = min(xs), min(ys)
    n = 0
    for a in range(A):
        for b in range(B):
            if not any(e[0] <= a and e[1] <= b for e in lts):
                n += 1
    return n


# ---------- stdlib Q[t]/(q) extension-field gcd ----------
def unorm(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def uis0(p):
    return all(c == 0 for c in p)


def umul(a, b):
    if uis0(a) or uis0(b):
        return [Fraction(0)]
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i + j] += ca * cb
    return unorm(r)


def umodrem(a, b):
    a = unorm(list(a))
    b = unorm(list(b))
    if uis0(b):
        raise ZeroDivisionError
    r = list(a)
    db = len(b) - 1
    cb = b[-1]
    while len(r) - 1 >= db and not uis0(r):
        dd = len(r) - 1 - db
        q = r[-1] / cb
        for i in range(len(b)):
            r[dd + i] -= q * b[i]
        r = unorm(r)
    return r


def uquo_rem(a, b):
    a = unorm(list(a))
    b = unorm(list(b))
    r = list(a)
    db = len(b) - 1
    cb = b[-1]
    q = [Fraction(0)] * max(len(r) - db, 0)
    while len(r) - 1 >= db and not uis0(r):
        dd = len(r) - 1 - db
        t = r[-1] / cb
        q[dd] = t
        for i in range(len(b)):
            r[dd + i] -= t * b[i]
        r = unorm(r)
    return unorm(q), unorm(r)


def kadd(a, b, q):
    n = max(len(a), len(b))
    return umodrem([(a[i] if i < len(a) else Fraction(0)) +
                    (b[i] if i < len(b) else Fraction(0))
                    for i in range(n)], q)


def ksub(a, b, q):
    n = max(len(a), len(b))
    return umodrem([(a[i] if i < len(a) else Fraction(0)) -
                    (b[i] if i < len(b) else Fraction(0))
                    for i in range(n)], q)


def kmul(a, b, q):
    return umodrem(umul(a, b), q)


def kinv(a, q):
    r0, r1 = unorm(list(q)), unorm(list(a))
    s0, s1 = [Fraction(0)], [Fraction(1)]
    while not uis0(r1):
        qq, rr = uquo_rem(r0, r1)
        r0, r1 = r1, rr
        prod = umul(qq, s1)
        n = max(len(s0), len(prod))
        s0, s1 = s1, unorm([(s0[i] if i < len(s0) else Fraction(0)) -
                            (prod[i] if i < len(prod) else Fraction(0))
                            for i in range(n)])
    c = r0[0]
    return unorm([v / c for v in umodrem(s0, q)])


def kx_norm(P, q):
    d = -1
    for i, c in enumerate(P):
        if not uis0(unorm(c)):
            d = i
    if d == -1:
        return [[Fraction(0)]]
    return [umodrem(list(c), q) for c in P[:d + 1]]


def kx_is0(P, q):
    return all(uis0(unorm(c)) for c in P)


def kx_modrem(A, B, q):
    A = kx_norm(A, q)
    B = kx_norm(B, q)
    R = list(A)
    db = len(B) - 1
    inv = kinv(B[db], q)
    while len(R) - 1 >= db and not kx_is0(R, q):
        dd = len(R) - 1 - db
        coeff = kmul(R[len(R) - 1], inv, q)
        for i in range(len(B)):
            R[dd + i] = ksub(R[dd + i], kmul(coeff, B[i], q), q)
        R = kx_norm(R, q)
    return R


def kx_monic(A, q):
    A = kx_norm(A, q)
    if kx_is0(A, q):
        return A
    inv = kinv(A[-1], q)
    return kx_norm([kmul(c, inv, q) for c in A], q)


def kx_gcd(A, B, q):
    A = kx_norm(A, q)
    B = kx_norm(B, q)
    while not kx_is0(B, q):
        A, B = B, kx_modrem(A, B, q)
    return kx_monic(A, q)


def kx_deriv(A):
    if len(A) <= 1:
        return [[Fraction(0)]]
    return [unorm([v * i for v in A[i]]) for i in range(1, len(A))]


def kx_divmod(A, B, q):
    A = kx_norm(A, q)
    B = kx_norm(B, q)
    R = list(A)
    db = len(B) - 1
    inv = kinv(B[db], q)
    Q = [[Fraction(0)]] * max(len(R) - db, 0)
    while len(R) - 1 >= db and not kx_is0(R, q):
        dd = len(R) - 1 - db
        coeff = kmul(R[len(R) - 1], inv, q)
        Q[dd] = coeff
        for i in range(len(B)):
            R[dd + i] = ksub(R[dd + i], kmul(coeff, B[i], q), q)
        R = kx_norm(R, q)
    return kx_norm(Q, q), R


def kx_sqdeg(G, q):
    G = kx_monic(kx_norm(G, q), q)
    if len(G) - 1 <= 0:
        return 0
    D = kx_deriv(G)
    if kx_is0(D, q):
        return 0
    H = kx_gcd(G, D, q)
    if len(H) - 1 <= 0:
        return len(G) - 1
    Q, R = kx_divmod(G, H, q)
    assert kx_is0(R, q)
    return len(Q) - 1


def fiber_above_orbit(fd, gd, qfac, elim_sym, fib_sym):
    """Contribution of one nonlinear Q-orbit factor qfac(elim_sym).

    fd, gd: dicts (a,b)->int of f, g. Returns (distinct, mult) with orbit
    multiplicity folded in.
    """
    qpoly = qfac if isinstance(qfac, Poly) else Poly(qfac, elim_sym)
    qq = [Fraction(c) for c in reversed(qpoly.all_coeffs())]
    dq = len(qq) - 1
    if fib_sym == x:
        proj = lambda e: e[0]
        pw = lambda e: e[1]
    else:
        proj = lambda e: e[1]
        pw = lambda e: e[0]
    dx = 0
    for e in list(fd) + list(gd):
        dx = max(dx, proj(e))
    A = [[Fraction(0)]] * (dx + 1)
    B = [[Fraction(0)]] * (dx + 1)
    for e, c in fd.items():
        t = [Fraction(0)] * pw(e) + [Fraction(c)]
        A[proj(e)] = kadd(A[proj(e)], umodrem(t, qq), qq)
    for e, c in gd.items():
        t = [Fraction(0)] * pw(e) + [Fraction(c)]
        B[proj(e)] = kadd(B[proj(e)], umodrem(t, qq), qq)
    G = kx_gcd(A, B, qq)
    if kx_is0(G, qq) or len(G) - 1 <= 0:
        return 0, 0
    return dq * kx_sqdeg(G, qq), dq * (len(G) - 1)


def fiber_counts(fi, fj, fd, gd, Ix, Iy):
    """Exact affine variety counts via both fiber directions.

    Returns (nd_y, nm_y, nd_x) with nd_y == nd_x expected; nm_y is the
    y-fiber multiplicity sum.
    """
    sqy = Poly(Ix.as_expr(), y, domain=QQ).sqf_part()
    # Iy may genuinely involve y (positive-dimensional direction shares a
    # y-only factor); then build the x-fiber check only when univariate in x.
    sqx = None
    if set(Iy.as_expr().free_symbols) <= {x}:
        sqx_raw = Poly(Iy.as_expr(), x, domain=QQ)
        sqx = sqx_raw.sqf_part()
    fy = factor_list(sqy, domain=QQ)[1]
    fx = factor_list(sqx, domain=QQ)[1] if sqx is not None else []
    nd_y = nm_y = 0
    # NB: resultants keep their own generator; re-express factors in the
    # intended elimination variable via as_expr().
    for (qexpr, _) in fy:
        qpoly = qexpr if isinstance(qexpr, Poly) else Poly(qexpr, y)
        qfac = Poly(qpoly.as_expr(), y, domain=QQ).monic()
        if qfac.degree() == 1:
            b = -qfac.nth(0)
            A = Poly(fi.subs(y, b), x, domain=QQ)
            Bc = Poly(fj.subs(y, b), x, domain=QQ)
            G = A.gcd(Bc)
            if G.is_zero or G.degree() == 0:
                continue
            nd_y += G.sqf_part().degree()
            nm_y += G.degree()
        else:
            dd, mm = fiber_above_orbit(fd, gd, qfac, y, x)
            nd_y += dd
            nm_y += mm
    nd_x = 0
    x_fiber_ok = sqx is not None
    for (qexpr, _) in fx:
        qpoly = qexpr if isinstance(qexpr, Poly) else Poly(qexpr, x)
        qe = qpoly.as_expr()
        assert set(qe.free_symbols) <= {x}, f'x-fiber factor {qe}'
        qfac = Poly(qe, x, domain=QQ).monic()
        if qfac.degree() == 1:
            a = -qfac.nth(0)
            A = Poly(fi.subs(x, a), y, domain=QQ)
            Bc = Poly(fj.subs(x, a), y, domain=QQ)
            G = A.gcd(Bc)
            if not (G.is_zero or G.degree() == 0):
                nd_x += G.sqf_part().degree()
        else:
            dd, _ = fiber_above_orbit(fd, gd, qfac, x, y)
            nd_x += dd
    return nd_y, nm_y, nd_x, x_fiber_ok


def main():
    t0 = time.time()
    items = enum_items()
    dicts = [d for d, _ in items]
    exprs = [e for _, e in items]
    strs = [pstr(d) for d in dicts]
    npairs = len(items) * (len(items) - 1) // 2
    print(f'polys={len(items)} pairs={npairs}', flush=True)
    rows = []
    Pstar = None
    both_fail_extra = {}
    counts = {'ZD': 0, 'POS': 0, 'INC': 0, 'shape_xy': 0, 'shape_yx': 0,
              'either': 0, 'both': 0, 'both_fail': 0, 'res_div_fail': 0,
              'zd_cert_mismatch': 0, 'fiber_mismatch': 0,
              'mult_mismatch': 0}
    n = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            n += 1
            fi, fj = exprs[i], exprs[j]
            Gxy = groebner([fi, fj], x, y, order='lex', domain=QQ)
            if list(Gxy) == [1]:
                counts['INC'] += 1
                rows.append((i, j, 'INC', 1, -1, -1, 0, 0, -1, -1,
                             -1, -1, -1, -1, -1, 0, 1))
                continue
            Gyx = groebner([fi, fj], y, x, order='lex', domain=QQ)
            Ggr = groebner([fi, fj], x, y, order='grlex', domain=QQ)
            sx = shape_of(Gxy, x)
            sy = shape_of(Gyx, y)
            Ix = Poly(fi, x, y).resultant(Poly(fj, x, y), x)[0]
            Iy = Poly(fi, x, y).resultant(Poly(fj, x, y), y)[0]
            stair = staircase_dim(Ggr)
            zd_res = not (Ix.is_zero or Iy.is_zero)
            zd_stair = stair is not None
            if zd_res != zd_stair:
                counts['zd_cert_mismatch'] += 1
            if not (zd_res and zd_stair):
                counts['POS'] += 1
                rows.append((i, j, 'POS', len(Gxy.polys), len(Gyx.polys),
                             len(Ggr.polys), int(sx), int(sy), -1, -1,
                             -1 if Ix.is_zero else Ix.degree(),
                             -1 if Iy.is_zero else Iy.degree(),
                             -1, -1, -1, 0, 1))
                continue
            counts['ZD'] += 1
            unis_y = [Poly(sum(c * y**b for (a, b), c in
                               Poly(g, x, y).as_dict().items()), y,
                           domain=QQ)
                      for g in Gxy.polys
                      if all(a == 0 for (a, b) in
                             Poly(g, x, y).as_dict())]
            unis_x = [Poly(sum(c * x**a for (a, b), c in
                               Poly(g, x, y).as_dict().items()), x,
                           domain=QQ)
                      for g in Gyx.polys
                      if all(b == 0 for (a, b) in
                             Poly(g, x, y).as_dict())]
            assert unis_y and unis_x, f'missing eliminant at {i},{j}'
            myg = unis_y[0]
            for qq_ in unis_y[1:]:
                myg = myg.gcd(qq_)
            mxg = unis_x[0]
            for qq_ in unis_x[1:]:
                mxg = mxg.gcd(qq_)
            edy, edx = myg.degree(), mxg.degree()
            divok = 1
            if not Ix.rem(myg).is_zero:
                divok = 0
                counts['res_div_fail'] += 1
            if not Iy.rem(mxg).is_zero:
                divok = 0
                counts['res_div_fail'] += 1
            nd_y, nm_y, nd_x, xfok = fiber_counts(fi, fj, dicts[i], dicts[j],
                                                        Ix, Iy)
            if xfok and nd_y != nd_x:
                counts['fiber_mismatch'] += 1
            if nm_y != stair:
                counts['mult_mismatch'] += 1
            if sx:
                counts['shape_xy'] += 1
            if sy:
                counts['shape_yx'] += 1
            if sx or sy:
                counts['either'] += 1
            if sx and sy:
                counts['both'] += 1
            bf = (not sx) and (not sy)
            if bf:
                counts['both_fail'] += 1
                if Pstar is None:
                    Pstar = {'i': i, 'j': j, 'f': strs[i], 'g': strs[j],
                             'Gxy': sorted(str(e) for e in Gxy.polys),
                             'Gyx': sorted(str(e) for e in Gyx.polys),
                             'Ggr': sorted(str(e) for e in Ggr.polys),
                             'elim_deg_y': edy, 'elim_deg_x': edx,
                             'res_y_deg': Ix.degree(),
                             'res_x_deg': Iy.degree(),
                             'n_distinct': nd_y, 'quot_dim': stair}
                if len(both_fail_extra) < 80:
                    both_fail_extra[f'{i},{j}'] = {
                        'f': strs[i], 'g': strs[j],
                        'Gxy': sorted(str(e) for e in Gxy.polys),
                        'Gyx': sorted(str(e) for e in Gyx.polys)}
            rows.append((i, j, 'ZD', len(Gxy.polys), len(Gyx.polys),
                         len(Ggr.polys), int(sx), int(sy), edy, edx,
                         Ix.degree(), Iy.degree(), stair, nd_y, nm_y,
                         int(bf), divok))
            if n % 2000 == 0:
                print(f'  {n}/{npairs} {time.time()-t0:.0f}s ZD='
                      f'{counts["ZD"]} BF={counts["both_fail"]}', flush=True)
    with open('output/artifacts/stratification.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['i', 'j', 'status', 'n_lex_xy', 'n_lex_yx', 'n_grevlex',
                    'shape_xy', 'shape_yx', 'elim_deg_y', 'elim_deg_x',
                    'res_y_deg', 'res_x_deg', 'quot_dim', 'n_distinct',
                    'n_mult', 'both_fail', 'res_div_ok'])
        w.writerows(rows)
    summary = {'n_polys': len(items), 'n_pairs': npairs, 'counts': counts,
               'Pstar': Pstar, 'seconds': round(time.time() - t0, 1)}
    with open('output/artifacts/summary.json', 'w') as fh:
        json.dump(summary, fh, indent=1)
    with open('output/artifacts/both_fail_bases.json', 'w') as fh:
        json.dump(both_fail_extra, fh, indent=1)
    print(json.dumps(summary, indent=1)[:3000], flush=True)
    print(f'done {time.time()-t0:.0f}s both_fail_stored='
          f'{len(both_fail_extra)}', flush=True)


if __name__ == '__main__':
    main()
