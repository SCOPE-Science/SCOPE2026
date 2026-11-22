#!/usr/bin/env python3
"""Exact exhaustive ramification classification of binary (4,3) filling curves.

Requires Python 3 and SymPy. No third-party data files are required.
The four projective charts are tested over the algebraic closure, not over
just a finite collection of extension fields.
"""
import itertools
import sympy as sp

x, y = sp.symbols('x y')
MON = [(i, j) for i in range(5) for j in range(4)]
PTS = [(1, 0), (0, 1), (1, 1)]


def equation(v, ax=0, ay=0):
    return sum(x ** (i if ax == 0 else 4-i)
               * y ** (j if ay == 0 else 3-j)
               for k, (i, j) in enumerate(MON) if (v >> k) & 1)


def filling_basis():
    rows = []
    for (u0, u1), (v0, v1) in itertools.product(PTS, repeat=2):
        row = sum(((u0**(4-i) * u1**i * v0**(3-j) * v1**j) & 1) << k
                  for k, (i, j) in enumerate(MON))
        rows.append(row)
    pivot = {}
    for row in rows:
        u = row
        for pos, p in sorted(pivot.items()):
            if (u >> pos) & 1:
                u ^= p
        if u:
            pivot[(u & -u).bit_length() - 1] = u
    basis = []
    for j in range(20):
        if j in pivot:
            continue
        v = 1 << j
        for pos, p in sorted(pivot.items(), reverse=True):
            if (p & v).bit_count() % 2:
                v ^= 1 << pos
        assert all((v & row).bit_count() % 2 == 0 for row in rows)
        basis.append(v)
    assert len(pivot) == 9 and len(basis) == 11
    return basis, rows


def geometrically_smooth(v):
    for ax, ay in itertools.product((0, 1), repeat=2):
        f = equation(v, ax, ay)
        G = sp.groebner((f, sp.diff(f, x), sp.diff(f, y)), x, y,
                        modulus=2)
        if len(G.polys) != 1 or G.polys[0].as_expr() != 1:
            return False
    return True


def all_filling_smooth():
    basis, rows = filling_basis()
    smooth = set()
    for m in range(1, 2**len(basis)):
        v = 0
        for k, b in enumerate(basis):
            if (m >> k) & 1:
                v ^= b
        assert all((v & r).bit_count() % 2 == 0 for r in rows)
        if geometrically_smooth(v):
            smooth.add(v)
    assert len(smooth) == 66
    return smooth


MATS = [(a, b, c, d) for a, b, c, d in itertools.product((0, 1), repeat=4)
        if (a*d + b*c) % 2 == 1]
assert len(MATS) == 6
IDENT = (1, 0, 0, 1)
X0, X1, Y0, Y1 = sp.symbols('X0 X1 Y0 Y1')


def coordinate_action(mask, mx, my):
    a, b, c, d = mx
    e, f, g, h = my
    expr = sum((a*X0+b*X1)**(4-i) * (c*X0+d*X1)**i
               * (e*Y0+f*Y1)**(3-j) * (g*Y0+h*Y1)**j
               for k, (i, j) in enumerate(MON) if (mask >> k) & 1)
    pp = sp.Poly(expr, X0, X1, Y0, Y1, modulus=2)
    return sum((int(pp.coeff_monomial(X0**(4-i)*X1**i
                                      *Y0**(3-j)*Y1**j)) & 1) << k
               for k, (i, j) in enumerate(MON))


def representative_orbits(curves):
    remaining = set(curves)
    result = []
    while remaining:
        v = min(remaining)
        orbit = {coordinate_action(v, m, n)
                 for m, n in itertools.product(MATS, repeat=2)}
        assert orbit <= curves and orbit <= remaining
        remaining -= orbit
        result.append((v, orbit))
    assert [(v, len(orb)) for v, orb in result] == [
        (396246, 6), (399606, 18), (404886, 36), (420790, 6)]
    return result


def cubic_in_y(mask):
    return [sp.Poly(sum(x**i for k, (i, j0) in enumerate(MON)
                        if j0 == j and (mask >> k) & 1), x, modulus=2)
            for j in range(4)]


def branch_data(mask):
    a0, a1, a2, a3 = cubic_in_y(mask)
    D = a3*a0 + a2*a1
    D = sp.Poly(D, x, modulus=2)
    T = a2*a2 + a3*a1
    T = sp.Poly(T, x, modulus=2)
    assert D.degree() == 8 and D.nth(0) == 1
    assert D.eval(1) % 2 == 1
    assert sp.gcd(D, D.diff()).degree() == 0
    assert sp.gcd(D, a3).degree() == 0
    factors = sp.factor_list(D, modulus=2)[1]
    degrees = sorted([fac.degree() for fac, exponent in factors for _ in range(exponent)])
    for factor, exponent in factors:
        assert exponent == 1 and factor.is_irreducible
    gd = sp.gcd(D, T)
    assert gd.degree() in (0, 8)
    if gd.degree() == 8:
        assert gd.monic() == D.monic()
    deck = [m for m in MATS if coordinate_action(mask, IDENT, m) == mask]
    return D, degrees, gd.degree(), len(deck)


def main():
    curves = all_filling_smooth()
    orbits = representative_orbits(curves)
    expected = {
        396246: ([8], 8, 3),
        399606: ([8], 0, 1),
        404886: ([8], 0, 1),
        420790: ([2, 6], 8, 3),
    }
    tame_count = wild_count = 0
    for v, orbit in orbits:
        D, degs, triple_gcd, n_deck = branch_data(v)
        assert (degs, triple_gcd, n_deck) == expected[v]
        if triple_gcd == 8:
            tame_count += len(orbit)
        else:
            wild_count += len(orbit)
        print('representative',v,'orbit',len(orbit),'branch',D.as_expr(),
              'closed_point_degrees',degs,'triple_gcd_degree',triple_gcd,
              'fiberwise_deck_order',n_deck)
    assert tame_count == 12 and wild_count == 54
    print('FILLING43_RAMIFICATION_VERIFIED', 'equations=2048', 'smooth=66',
          'orbits=4', 'cyclic_tame=12', 'S3_wild=54',
          'branch_cycle_profiles=(8)x3,(2+6)x1')


if __name__ == '__main__':
    main()
