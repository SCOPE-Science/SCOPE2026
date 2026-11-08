#!/usr/bin/env python3
"""Exact four-patch occupancy-chain computations (SymPy required)."""
import itertools
import sympy as sp

c = sp.symbols('c', positive=True)
PATH = [(0, 1), (1, 2), (2, 3)]
SQUARE = PATH + [(0, 3)]
TRIANGLE_TAIL = PATH + [(0, 2)]


def transient_matrix(edges, parameter):
    """Positive matrix -Q, states 1..15; empty state is absorbing."""
    M = sp.zeros(15)
    adjacency = [{j for i, j in edges if i == v} |
                 {i for i, j in edges if j == v} for v in range(4)]
    for mask in range(1, 16):
        row = mask - 1
        M[row, row] = mask.bit_count()
        for v in range(4):
            if mask & (1 << v):
                nxt = mask & ~(1 << v)
                if nxt:
                    M[row, nxt - 1] -= 1
            else:
                k = sum(bool(mask & (1 << u)) for u in adjacency[v])
                M[row, row] += k * parameter
                M[row, (mask | (1 << v)) - 1] -= k * parameter
    return M


def symbolic_orbit_solution(edges):
    graph = {tuple(sorted(e)) for e in edges}
    automorphisms = [p for p in itertools.permutations(range(4))
                     if {tuple(sorted((p[i], p[j]))) for i, j in graph} == graph]
    orbits, seen = [], set()
    for state in range(1, 16):
        if state in seen:
            continue
        orbit = sorted({sum(1 << p[i] for i in range(4) if state & (1 << i))
                        for p in automorphisms})
        seen.update(orbit)
        orbits.append(orbit)
    orbit_id = {s: k for k, orbit in enumerate(orbits) for s in orbit}
    full = transient_matrix(edges, c)
    reduced = sp.zeros(len(orbits))
    for row, orbit in enumerate(orbits):
        s = orbit[0] - 1
        for target in range(1, 16):
            reduced[row, orbit_id[target]] += full[s, target - 1]
    t = reduced.inv(method='DM') * sp.ones(len(orbits), 1)
    lifted = sp.Matrix([t[orbit_id[s]] for s in range(1, 16)])
    assert all(sp.cancel(v) == 0 for v in full * lifted - sp.ones(15, 1))
    return sp.factor(t[orbit_id[15]]), len(orbits), lifted


def main():
    square, n_square, lift_square = symbolic_orbit_solution(SQUARE)
    tail, n_tail, lift_tail = symbolic_orbit_solution(TRIANGLE_TAIL)
    assert (n_square, n_tail) == (5, 11)
    expected_square = ((8*c**4 + 24*c**3 + 42*c**2 + 61*c + 25)
                       / (4 * (5*c+3)))
    h = (162*c**7+806*c**6+1857*c**5+2618*c**4+2412*c**3
         +1416*c**2+480*c+72)
    expected_tail = (324*c**10+2556*c**9+9919*c**8+25760*c**7
                     +48131*c**6+65654*c**5+65563*c**4+46968*c**3
                     +22806*c**2+6696*c+900)/(6*h)
    assert sp.cancel(square - expected_square) == 0
    assert sp.cancel(tail - expected_tail) == 0

    P = (648*c**9+3504*c**8+8486*c**7+10624*c**6+4144*c**5
         -7529*c**4-13801*c**3-10608*c**2-4176*c-684)
    expected_difference = c**2*P/(12*(5*c+3)*h)
    assert sp.cancel(square-tail-expected_difference) == 0
    assert sp.Poly(P,c).all_coeffs() == [648,3504,8486,10624,4144,
                                        -7529,-13801,-10608,-4176,-684]
    signs = [sp.sign(v) for v in sp.Poly(P,c).all_coeffs()]
    assert sum(a != b for a,b in zip(signs, signs[1:])) == 1
    assert P.subs(c,0) < 0
    root = sp.polys.polytools.intervals(P, eps=sp.Rational(1,10**11), sqf=True)
    positive = [interval for interval in root if interval[0] > 0]
    assert len(positive) == 1
    lo,hi = positive[0]
    assert lo > sp.Rational(1079524,10**6) and hi < sp.Rational(1079525,10**6)

    assert sp.limit((square-tail)/c**2,c,0,dir='+') == -sp.Rational(19,72)
    assert sp.limit((square-tail)/c**3,c,sp.oo) == sp.Rational(1,15)
    assert square.subs(c,0) == tail.subs(c,0) == sp.Rational(25,12)
    for x in [sp.Rational(1,10), sp.Rational(1,2),sp.Integer(1),
              sp.Rational(6,5),sp.Integer(2),sp.Integer(5)]:
        for graph, expected in [(SQUARE, square), (TRIANGLE_TAIL, tail)]:
            mat = transient_matrix(graph, x)
            independent = mat.inv(method='DM')*sp.ones(15,1)
            assert independent[14] == expected.subs(c,x)
            assert mat*independent == sp.ones(15,1)
        assert sp.sign((square-tail).subs(c,x)) == (-1 if x<sp.Rational(1079524,10**6) else 1)

    z=sp.Symbol('lambda')
    def spectral_polynomial(edges):
        adj=sp.zeros(4)
        for a,b in edges: adj[a,b]=adj[b,a]=1
        return sp.expand((z*sp.eye(4)-adj).det())
    assert spectral_polynomial(SQUARE) == z**4-4*z**2
    assert sp.expand(spectral_polynomial(TRIANGLE_TAIL) - (z+1)*(z**3-z**2-3*z+1)) == 0
    assert (z**3-z**2-3*z+1).subs(z,2)<0
    print('PASS: 5/11 orbit reductions, full symbolic backward equations, exact formulas,')
    print('unique positive sign transition, full 15-state independent rational checks,')
    print('small/large rate limits, and spectral characteristic identities.')
    print('threshold bracket:', lo, hi)

if __name__ == '__main__':
    main()
