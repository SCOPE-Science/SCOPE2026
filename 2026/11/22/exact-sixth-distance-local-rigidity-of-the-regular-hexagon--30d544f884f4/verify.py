"""Reproduce the exact regular-hexagon sixth-distance-energy Hessian.

Requires Python >=3.9 and SymPy >=1.10. Uses exact integer/rational
arithmetic only. Run: python verify.py
"""
from functools import lru_cache
from math import comb, factorial
import json
from pathlib import Path
import sympy as sp

VERTICES = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
N = len(VERTICES)
DIM = 2 * N
pa, pb, pc, pd = sp.symbols('a b c d')
x, y, u, v, z = sp.symbols('x y u v z')

@lru_cache(None)
def triangle_moment(p, q):
    """Polynomial integral of x**p*y**q on conv(0,(a,b),(c,d))."""
    expansion = 0
    for i in range(p + 1):
        for j in range(q + 1):
            s = i + j
            t = p + q - s
            coef = sp.Rational(comb(p, i)*comb(q, j)*factorial(s)*factorial(t),
                               factorial(p+q+2))
            expansion += coef*pa**i*pc**(p-i)*pb**j*pd**(q-j)
    return sp.expand((pa*pd-pb*pc)*expansion)

@lru_cache(None)
def triangle_jet(p, q, edge):
    ex = triangle_moment(p, q)
    values = (*VERTICES[edge], *VERTICES[(edge+1) % N])
    subs = dict(zip((pa, pb, pc, pd), values))
    variables = (pa, pb, pc, pd)
    return (ex.subs(subs),
            [sp.diff(ex, s).subs(subs) for s in variables],
            [[sp.diff(ex, s, t).subs(subs) for t in variables]
             for s in variables])

def polygon_moment_jet(p, q):
    value = sp.Integer(0)
    gradient = sp.zeros(DIM, 1)
    hessian = sp.zeros(DIM, DIM)
    for edge in range(N):
        val, grad, hess = triangle_jet(p, q, edge)
        value += val
        indexes = [2*edge, 2*edge+1, 2*((edge+1) % N),
                   2*((edge+1) % N)+1]
        for i in range(4):
            gradient[indexes[i]] += grad[i]
            for j in range(4):
                hessian[indexes[i], indexes[j]] += hess[i][j]
    return value, gradient, hessian

def main():
    pair_kernel = sp.expand(((x-u)**2+(x-u)*(y-v)+(y-v)**2)**3)
    polynomial_terms = sp.Poly(pair_kernel, x, y, u, v).terms()
    required = {(0, 0)}
    for powers, _ in polynomial_terms:
        required.add(tuple(powers[:2]))
        required.add(tuple(powers[2:]))
    moments = {pq: polygon_moment_jet(*pq) for pq in required}

    energy = sp.Integer(0)
    energy_gradient = sp.zeros(DIM, 1)
    energy_hessian = sp.zeros(DIM, DIM)
    for powers, coefficient in polynomial_terms:
        m, gm, hm = moments[tuple(powers[:2])]
        n, gn, hn = moments[tuple(powers[2:])]
        energy += coefficient*m*n
        energy_gradient += coefficient*(n*gm+m*gn)
        energy_hessian += coefficient*(n*hm+m*hn+gm*gn.T+gn*gm.T)

    area, area_gradient, area_hessian = moments[(0, 0)]
    assert area == 3
    assert energy == sp.Rational(5157, 280)
    assert energy_gradient == 5*energy/area*area_gradient

    # Exact Hessian of log(E / A**5) at the regular hexagon.
    H = (energy_hessian/energy
         - energy_gradient*energy_gradient.T/energy**2
         - 5*area_hessian/area
         + 5*area_gradient*area_gradient.T/area**2)
    assert H == H.T
    assert 25785*H == (25785*H).applyfunc(lambda t: sp.Integer(t))

    factors = [
        984987*z**2 - 6040566*z + 4139272,
        2954961*z**2 - 13920462*z + 4139272,
        4924935*z**2 - 5929404*z + 730904,
        24624675*z**2 - 61299540*z + 8316776,
    ]
    charpoly = z**4
    for factor in factors:
        charpoly *= factor/sp.LC(sp.Poly(factor, z))
        # Each factor is real-rooted as a factor of a symmetric matrix
        # characteristic polynomial; sum and product of roots are positive.
        coeffs = sp.Poly(factor, z).all_coeffs()
        assert coeffs[0] > 0 and coeffs[1] < 0 and coeffs[2] > 0
        assert coeffs[1]**2 > 4*coeffs[0]*coeffs[2]
    assert sp.expand(H.charpoly(z).as_expr()-charpoly) == 0
    assert H.rank() == 8
    assert len(H.nullspace()) == 4

    # Similarity tangent directions in the oblique (triangular-lattice) gauge.
    tx = sp.Matrix([1 if i % 2 == 0 else 0 for i in range(DIM)])
    ty = sp.Matrix([1 if i % 2 == 1 else 0 for i in range(DIM)])
    scaling = sp.Matrix([component for vertex in VERTICES for component in vertex])
    # B=[[-1,-2],[2,1]] is a nonzero infinitesimal Euclidean rotation
    # for the metric q(s,t)=s**2+s*t+t**2.
    rotation = sp.Matrix([component for a,b in VERTICES for component in (-a-2*b,2*a+b)])
    for direction in (tx,ty,scaling,rotation):
        assert H*direction == sp.zeros(DIM,1)
    assert sp.Matrix.hstack(tx,ty,scaling,rotation).rank() == 4

    # Note: 191*sqrt(3)/2835 is the physical Euclidean normalized energy.
    assert sp.simplify(energy/area**5*(sp.Rational(2,1)/sp.sqrt(3))**3) == 191*sp.sqrt(3)/2835
    data = {
        'coordinate_order': [f'{name}_{i}' for i in range(N) for name in ('u','v')],
        'metric': '(du)^2+(du)(dv)+(dv)^2',
        'regular_vertices': VERTICES,
        'coordinate_area': str(area),
        'coordinate_sixth_distance_energy': str(energy),
        'euclidean_normalized_energy': '191*sqrt(3)/2835',
        'hessian_denominator': 25785,
        'hessian_integer_numerators': [list(map(int,H.row(i)*25785)) for i in range(DIM)],
        'characteristic_quadratic_factors': [str(f) for f in factors],
        'zero_multiplicity': 4,
        'positive_eigenvalue_count': 8,
    }
    if __name__ == '__main__':
        Path('HESSIAN.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
        print('PASS: 28 exact polygon moments, area and energy, stationarity,')
        print('      Hessian, characteristic factors, 8 positive directions,')
        print('      and exactly 4 similarity directions in the kernel.')
    return data

if __name__ == '__main__':
    main()
