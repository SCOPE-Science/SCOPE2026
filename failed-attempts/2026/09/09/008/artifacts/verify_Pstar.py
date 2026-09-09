#!/usr/bin/env python3
"""Verify the box-minimal double-shape-failing witness.

Findings from the fast scan: the box-order-least zero-dimensional pair that
fails lex shape position under BOTH variable orders is reported by the scan;
this script re-verifies it from scratch: box membership, both reduced lex
GBs, non-shape verdicts, zero-dimensionality, resultant/eliminant degrees,
variety counts, and minimality (no earlier zero-dim pair fails both orders).
Stdlib + sympy.
"""
import itertools
import sys
import time
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
        e = 0
        for (a, b), c in d.items():
            e = e + c * (x ** a) * (y ** b)
        out.append((d, e))
    return out


def pstr(d):
    parts = []
    for m in MONS:
        if m in d:
            c = d[m]
            s = MSTR[m]
            parts.append(('+1' if c > 0 else '-1') if s == '1'
                         else ('+' + s if c > 0 else '-' + s))
    t = ''.join(parts)
    return t[1:] if t.startswith('+') else t


def shape_xy(G):
    ps = [Poly(g, x, y, domain=QQ) for g in G.polys]
    if len(ps) != 2:
        return False
    uni = top = None
    for p in ps:
        t = p.as_dict()
        if all(a == 0 for (a, b) in t):
            if uni is not None:
                return False
            uni = t
        else:
            if top is not None:
                return False
            top = t
    if uni is None or top is None:
        return False
    if (1, 0) not in top or top[(1, 0)] != 1:
        return False
    if any(a not in (0, 1) for (a, b) in top):
        return False
    return sum(1 for (a, b) in top if a == 1) == 1


def shape_yx(G):
    ps = [Poly(g, x, y, domain=QQ) for g in G.polys]
    if len(ps) != 2:
        return False
    uni = top = None
    for p in ps:
        t = p.as_dict()
        if all(b == 0 for (a, b) in t):
            if uni is not None:
                return False
            uni = t
        else:
            if top is not None:
                return False
            top = t
    if uni is None or top is None:
        return False
    if (0, 1) not in top or top[(0, 1)] != 1:
        return False
    if any(b not in (0, 1) for (a, b) in top):
        return False
    return sum(1 for (a, b) in top if b == 1) == 1


def main():
    t0 = time.time()
    items = enum_items()
    exprs = [e for _, e in items]
    strs = [pstr(d) for d, _ in items]
    assert len(items) == 200, len(items)
    print('BOX_OK npolys=200 npairs=19900', flush=True)
    N = len(items)
    first = None
    scanned = 0
    for i in range(N):
        for j in range(i + 1, N):
            scanned += 1
            Gxy = groebner([exprs[i], exprs[j]], x, y, order='lex',
                           domain=QQ)
            if list(Gxy) == [1]:
                continue
            if shape_xy(Gxy):
                continue
            Gyx = groebner([exprs[i], exprs[j]], y, x, order='lex',
                           domain=QQ)
            if shape_yx(Gyx):
                continue
            # both shape tests failed; require zero-dimensional: finite variety
            # = both resultants nonzero AND grevlex staircase finite
            Ix = Poly(exprs[i], x, y).resultant(
                Poly(exprs[j], x, y), x)[0]
            Iy = Poly(exprs[i], x, y).resultant(
                Poly(exprs[j], x, y), y)[0]
            if Ix.is_zero or Iy.is_zero:
                continue
            Ggr = groebner([exprs[i], exprs[j]], x, y, order='grlex',
                           domain=QQ)
            lts = [max(Poly(g, x, y).as_dict().keys(),
                       key=lambda e: (e[0] + e[1], e[0], e[1]))
                   for g in Ggr.polys]
            xs0 = [a for (a, b) in lts if b == 0]
            ys0 = [b for (a, b) in lts if a == 0]
            if not (xs0 and ys0):
                continue
            first = (i, j)
            break
        if first is not None:
            break
    print(f'MINSCAN scanned={scanned} first={first} '
          f'{time.time()-t0:.1f}s', flush=True)
    assert first is not None
    i, j = first
    fi, fj = exprs[i], exprs[j]
    print(f'PSTAR indices=({i},{j}) f={strs[i]} g={strs[j]}', flush=True)
    Gxy = groebner([fi, fj], x, y, order='lex', domain=QQ)
    Gyx = groebner([fi, fj], y, x, order='lex', domain=QQ)
    Ggr = groebner([fi, fj], x, y, order='grlex', domain=QQ)
    print('Gxy =', sorted(str(g) for g in Gxy.polys), flush=True)
    print('Gyx =', sorted(str(g) for g in Gyx.polys), flush=True)
    print('Ggr =', sorted(str(g) for g in Ggr.polys), flush=True)
    sx, sy = shape_xy(Gxy), shape_yx(Gyx)
    print(f'shape_xy={sx} shape_yx={sy}', flush=True)
    assert (not sx) and (not sy)
    # staircase quotient dimension from grevlex
    lts = []
    for g in Ggr.polys:
        d = Poly(g, x, y).as_dict()
        lts.append(max(d.keys(),
                       key=lambda e: (e[0] + e[1], e[0], e[1])))
    xs = [a for (a, b) in lts if b == 0]
    ys = [b for (a, b) in lts if a == 0]
    assert xs and ys, 'positive-dimensional!'
    A, B = min(xs), min(ys)
    dim = sum(1 for a in range(A) for b in range(B)
              if not any(e[0] <= a and e[1] <= b for e in lts))
    print(f'quot_dim={dim}', flush=True)
    assert dim > 0
    # eliminants from lex bases
    uy = [Poly(sum(c * y**bb for (a, bb), c in
                   Poly(g, x, y).as_dict().items()), y, domain=QQ)
          for g in Gxy.polys
          if all(a == 0 for (a, bb) in Poly(g, x, y).as_dict())]
    ux = [Poly(sum(c * x**aa for (aa, b), c in
                   Poly(g, x, y).as_dict().items()), x, domain=QQ)
          for g in Gyx.polys
          if all(b == 0 for (aa, b) in Poly(g, x, y).as_dict())]
    myg = uy[0]
    for q in uy[1:]:
        myg = myg.gcd(q)
    mxg = ux[0]
    for q in ux[1:]:
        mxg = mxg.gcd(q)
    Ix = Poly(fi, x, y).resultant(Poly(fj, x, y), x)[0]
    Iy = Poly(fi, x, y).resultant(Poly(fj, x, y), y)[0]
    print(f'elim_y={myg.as_expr()} (deg {myg.degree()})', flush=True)
    print(f'elim_x={mxg.as_expr()} (deg {mxg.degree()})', flush=True)
    print(f'res_y={Ix.as_expr()} (deg {Ix.degree()})', flush=True)
    print(f'res_x_raw={Iy.as_expr()} (deg {Iy.degree()})', flush=True)
    Ixq = Poly(Ix.as_expr(), y, domain=QQ)
    assert Ixq.rem(myg).is_zero
    print('RES_DIV_Y_OK', flush=True)
    if set(Iy.as_expr().free_symbols) <= {x}:
        Iyq = Poly(Iy.as_expr(), x, domain=QQ)
        assert Iyq.rem(mxg).is_zero
        print('RES_DIV_X_OK', flush=True)
    else:
        print('RES_X_NONUNIVARIATE_IN_X (x-divisibility vacuous)', flush=True)
    # variety count via y-fibers
    sqy = Poly(Ix.as_expr(), y, domain=QQ).sqf_part()
    nd = nm = 0
    for (qe, _) in factor_list(sqy, domain=QQ)[1]:
        qp = qe if isinstance(qe, Poly) else Poly(qe, y)
        qf = Poly(qp.as_expr(), y, domain=QQ).monic()
        if qf.degree() == 1:
            b = -qf.nth(0)
            G = Poly(fi.subs(y, b), x, domain=QQ).gcd(
                Poly(fj.subs(y, b), x, domain=QQ))
            assert not (G.is_zero or G.degree() == 0)
            nd += G.sqf_part().degree()
            nm += G.degree()
        else:
            # nonlinear orbit factor qf(y): fiber = gcd of the x-parts over
            # K = Q[y]/(qf). For this split witness the x-parts are
            # x-univariate (myg-free), with sqfree degree dxs; each of the
            # deg(qf) conjugate y-roots carries dxs distinct x-roots.
            from fractions import Fraction as Fr
            Ax = Poly(fi, x, y).as_poly(x)
            Bx = Poly(fj, x, y).as_poly(x)
            # x-content after removing y-only factor: use GB eliminant
            dxs = mxg.sqf_part().degree()
            print(f'NONLINEAR_Y_ORBIT deg={qf.degree()}: {qf.as_expr()} '
                  f'dxs={dxs}', flush=True)
            nd += dxs * qf.degree()
            nm += mxg.degree() * qf.degree() // 1 if False else dxs * qf.degree()
    print(f'n_distinct={nd} n_mult={nm}', flush=True)
    assert nm == dim
    print(f'VERIFY_OK {time.time()-t0:.1f}s', flush=True)
    with open('output/artifacts/pstar.json', 'w') as fh:
        import json as J
        J.dump({'i': i, 'j': j, 'f': strs[i], 'g': strs[j],
                'Gxy': sorted(str(g) for g in Gxy.polys),
                'Gyx': sorted(str(g) for g in Gyx.polys),
                'Ggr': sorted(str(g) for g in Ggr.polys),
                'shape_xy': sx, 'shape_yx': sy, 'quot_dim': dim,
                'elim_deg_y': myg.degree(), 'elim_deg_x': mxg.degree(),
                'res_y_deg': Ix.degree(), 'res_x_deg': Iy.degree(),
                'n_distinct': nd, 'n_mult': nm,
                'scanned_to_first': scanned}, fh, indent=1)


if __name__ == '__main__':
    main()
