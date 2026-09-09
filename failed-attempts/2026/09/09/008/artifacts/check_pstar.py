#!/usr/bin/env python3
"""Final clean certificate for the box-minimal double-shape-failing witness.

Uses correct sympy APIs throughout (sympy.resultant function form so the
x-side resultant is a polynomial in x). Regenerates box U from definition,
audits every predecessor pair before P*, and certifies P* = (0,60).
Writes pstar_cert.json; prints VERIFY_OK on success.
"""
import itertools
import json
import time

from sympy import QQ, Poly, factor_list, groebner, resultant, solve, symbols

x, y = symbols('x y')
MONS = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0)]
MSTR = {(2, 0): 'x^2', (1, 1): 'xy', (0, 2): 'y^2',
        (1, 0): 'x', (0, 1): 'y', (0, 0): '1'}
QUADS = {(2, 0), (1, 1), (0, 2)}


def enum_items():
    polys = []
    for k in (2, 3):
        for supp in itertools.combinations(range(6), k):
            if not any(MONS[m] in QUADS for m in supp):
                continue
            for signs in itertools.product((1, -1), repeat=k):
                d = {MONS[mi]: s for mi, s in zip(supp, signs)}
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
    t = ''
    for m in MONS:
        if m in d:
            c, s = d[m], MSTR[m]
            t += ('+1' if c > 0 else '-1') if s == '1' \
                else ('+' + s if c > 0 else '-' + s)
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


def zd_status(fi, fj):
    Ix = resultant(fi, fj, x)
    Iy = resultant(fi, fj, y)
    if Ix == 0 or Iy == 0:
        return False, Ix, Iy, None
    Ggr = groebner([fi, fj], x, y, order='grlex', domain=QQ)
    lts = [max(Poly(g, x, y).as_dict().keys(),
               key=lambda e: (e[0] + e[1], e[0], e[1]))
           for g in Ggr.polys]
    xs = [a for (a, b) in lts if b == 0]
    ys = [b for (a, b) in lts if a == 0]
    if not (xs and ys):
        return False, Ix, Iy, None
    A, B = min(xs), min(ys)
    dim = sum(1 for a in range(A) for b in range(B)
              if not any(e[0] <= a and e[1] <= b for e in lts))
    return True, Ix, Iy, dim


def main():
    t0 = time.time()
    items = enum_items()
    assert len(items) == 200, len(items)
    npairs = len(items) * (len(items) - 1) // 2
    assert npairs == 19900, npairs
    print(f'BOX_OK npolys=200 npairs=19900', flush=True)
    exprs = [e for _, e in items]
    strs = [pstr(d) for d, _ in items]
    assert strs[0] == '-y^2-y-1' and strs[60] == '-x^2-x-1'

    # Prefix audit: every pair before (0,60) in (i,j) lex order.
    prefix = []
    for j in range(1, 60):
        Gxy = groebner([exprs[0], exprs[j]], x, y, order='lex', domain=QQ)
        if list(Gxy) == [1]:
            prefix.append([0, j, strs[j], 'INC', 0, 0])
            continue
        zd, Ix, Iy, dim = zd_status(exprs[0], exprs[j])
        if not zd:
            prefix.append([0, j, strs[j], 'POS', 0, 0])
            continue
        sx = shape_xy(Gxy)
        Gyx = groebner([exprs[0], exprs[j]], y, x, order='lex', domain=QQ)
        sy = shape_yx(Gyx)
        assert sx or sy, f'earlier double-fail at (0,{j})!'
        prefix.append([0, j, strs[j], 'ZD', int(sx), int(sy)])
    print(f'PREFIX_OK 59 pairs, no earlier zero-dim double-shape-fail',
          flush=True)

    # P* certificate.
    i, j = 0, 60
    fi, fj = exprs[i], exprs[j]
    Gxy = groebner([fi, fj], x, y, order='lex', domain=QQ)
    Gyx = groebner([fi, fj], y, x, order='lex', domain=QQ)
    Ggr = groebner([fi, fj], x, y, order='grlex', domain=QQ)
    sx, sy = shape_xy(Gxy), shape_yx(Gyx)
    assert (not sx) and (not sy)
    sxy = sorted(str(g) for g in Gxy.polys)
    syx = sorted(str(g) for g in Gyx.polys)
    sgr = sorted(str(g) for g in Ggr.polys)
    assert sxy == ["Poly(x**2 + x + 1, x, y, domain='QQ')",
                   "Poly(y**2 + y + 1, x, y, domain='QQ')"], sxy
    assert syx == ["Poly(x**2 + x + 1, y, x, domain='QQ')",
                   "Poly(y**2 + y + 1, y, x, domain='QQ')"], syx
    print('GXY_OK', sxy, flush=True)
    print('GYX_OK', syx, flush=True)

    zd, Ix, Iy, dim = zd_status(fi, fj)
    assert zd and dim == 4
    assert Poly(Ix, y, domain=QQ).degree() == 4
    assert Poly(Iy, x, domain=QQ).degree() == 4
    print(f'ZD_OK quot_dim=4 res_x_deg=4 res_y_deg=4', flush=True)

    my = Poly(y**2 + y + 1, y, domain=QQ)
    mx = Poly(x**2 + x + 1, x, domain=QQ)
    assert Poly(Ix, y, domain=QQ).rem(my).is_zero
    assert Poly(Iy, x, domain=QQ).rem(mx).is_zero
    print('ELIM_OK elim_y=y^2+y+1 elim_x=x^2+x+1 both divide resultants',
          flush=True)
    assert factor_list(Poly(Ix, y, domain=QQ), domain=QQ)[1] == [
        (Poly(y**2 + y + 1, y, domain=QQ), 2)]
    assert factor_list(Poly(Iy, x, domain=QQ), domain=QQ)[1] == [
        (Poly(x**2 + x + 1, x, domain=QQ), 2)]

    ys = solve(fi, y)
    xs = solve(fj, x)
    assert len(ys) == 2 and len(xs) == 2
    pts = [(a, b) for a in xs for b in ys]
    assert len(pts) == 4
    for (a, b) in pts:
        assert (fi.subs({x: a, y: b})).simplify() == 0
        assert (fj.subs({x: a, y: b})).simplify() == 0
    print('VARIETY_OK n_distinct=4 n_mult=4 (2x2 grid of prim. cube roots)',
          flush=True)

    cert = {'box': {'n_polys': 200, 'n_pairs': 19900},
            'Pstar': {'i': 0, 'j': 60, 'f': strs[0], 'g': strs[60],
                      'Gxy': sxy, 'Gyx': syx, 'Ggr': sgr,
                      'shape_xy': False, 'shape_yx': False,
                      'quot_dim': 4,
                      'elim_y': 'y^2+y+1', 'elim_deg_y': 2,
                      'elim_x': 'x^2+x+1', 'elim_deg_x': 2,
                      'res_x_deg': 4, 'res_y_deg': 4,
                      'res_x_factors': [['y^2+y+1', 2]],
                      'res_y_factors': [['x^2+x+1', 2]],
                      'n_distinct': 4, 'n_mult': 4,
                      'scanned_to_first': 60},
            'prefix_audit': prefix,
            'seconds': round(time.time() - t0, 1)}
    with open('output/artifacts/pstar_cert.json', 'w') as fh:
        json.dump(cert, fh, indent=1)
    print(f"VERIFY_OK {time.time()-t0:.1f}s", flush=True)


if __name__ == '__main__':
    main()
