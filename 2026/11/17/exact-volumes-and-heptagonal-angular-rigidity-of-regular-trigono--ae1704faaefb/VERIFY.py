"""Standalone checks for regular trigonometric cyclic four-polytopes.

Run with: python VERIFY.py  (Python 3.9+, standard library only).
This script supplies exact finite algebraic coefficient checks and independent
numerical determinant tests; the universal statements use the accompanying proof.
"""
import cmath
import itertools
import math
from fractions import Fraction as Q


def det4(matrix):
    total = 0.0
    for perm in itertools.permutations(range(4)):
        sg = -1 if sum(perm[i] > perm[j] for i in range(4)
                       for j in range(i + 1, 4)) % 2 else 1
        term = sg
        for row in range(4):
            term *= matrix[row][perm[row]]
        total += term
    return total


def vertices(n):
    return [tuple(q / math.sqrt(2) for q in
                  (math.cos(2 * math.pi * j / n), math.sin(2 * math.pi * j / n),
                   math.cos(4 * math.pi * j / n), math.sin(4 * math.pi * j / n)))
            for j in range(n)]


def test_volume(n):
    vv = vertices(n)
    h = 2 * math.pi / n
    det_total = 0.0
    for i in range(n):
        for k in range(2, n - 1):
            ids = [i % n, (i + 1) % n, (i + k) % n, (i + k + 1) % n]
            dd = det4([vv[j] for j in ids])
            exact = 2 * math.sin(h / 2)**2 * (1 - math.cos(k * h)) * (math.cos(h) - math.cos(k * h)) * (1 + math.cos(h) + math.cos(k * h))
            assert abs(dd - exact) < 1e-10, (n, i, k, dd, exact)
            assert dd > 0, (n, i, k)
            det_total += dd
    via_facets = det_total / 48
    closed = n * n * math.cos(h) * math.sin(h)**2 / 48
    assert abs(via_facets - closed) < 2e-11, (n, via_facets, closed)
    return closed


def exact_hessian_coefficients():
    # The 4x4 complex determinant has rows (z^j, z^-j, z^(2j), z^(-2j)).
    # The second derivative of the positive real determinant has factor 1/16;
    # ordered edge-pair cone decomposition adds 1/48. Entries are in Z[zeta_7]/768.
    n = 7
    weights = (1, -1, 2, -2)
    permutations = []
    for p in itertools.permutations(range(4)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        permutations.append((p, sign))
    H = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for separation in range(2, n - 1):
            ids = (i, (i + 1) % n, (i + separation) % n,
                   (i + separation + 1) % n)
            for a in range(4):
                for b in range(a, 4):
                    order = [0] * 4
                    if a == b:
                        order[a] = 2
                    else:
                        order[a] = order[b] = 1
                    coeff = [0] * n
                    for perm, sign in permutations:
                        exponent = sum(weights[perm[col]] * ids[col] for col in range(4)) % n
                        term = sign
                        for col in range(4):
                            term *= weights[perm[col]] ** order[col]
                        coeff[exponent] += term
                    for e in range(n):
                        H[ids[a]][ids[b]][e] += coeff[e]
                        if a != b:
                            H[ids[b]][ids[a]][e] += coeff[e]
    assert all(H[i][j] == H[j][i] for i in range(n) for j in range(n))
    assert all(H[i][j] == H[0][(j-i) % n] for i in range(n) for j in range(n))
    spectra = []
    for k in range(4):
        coeff = [0] * n
        for j in range(n):
            for e in range(n):
                coeff[(e + k*j) % n] += H[0][j][e]
        assert all(coeff[e] == coeff[-e] for e in range(1, 4))
        # zeta^j + zeta^-j = 2 T_j(u), u=cos(2pi/7).
        # u^3 = (-4u^2+4u+1)/8.
        a = Q(coeff[0] - 2*coeff[2] + coeff[3], 768)
        b = Q(2*coeff[1] - 2*coeff[3], 768)
        c = Q(4*coeff[2] - 4*coeff[3], 768)
        spectra.append((a,b,c))
    expected = [
        (Q(0), Q(0), Q(0)),
        (Q(-7,64), Q(-7,24), Q(7,48)),
        (Q(175,384), Q(-175,192), Q(-35,24)),
        (Q(7,24), Q(-259,192), Q(-119,96)),
    ]
    assert spectra == expected, (spectra, expected)
    u = math.cos(2*math.pi/7)
    assert u > 0.6
    vals = [float(a + b*u + c*u*u) for a,b,c in spectra]
    assert abs(vals[0]) < 1e-14 and all(x < 0 for x in vals[1:]), vals
    # Independent central-difference Hessian of the geometric determinant formula
    # checks the exact coefficient convention, not merely cyclotomic arithmetic.
    def volume_angles(angles):
        vv = [tuple(q / math.sqrt(2) for q in
                    (math.cos(t), math.sin(t), math.cos(2*t), math.sin(2*t)))
              for t in angles]
        return sum(det4([vv[p] for p in
                         (i, (i+1)%7, (i+k)%7, (i+k+1)%7)])
                   for i in range(7) for k in range(2, 6)) / 48
    theta = [2*math.pi*j/7 for j in range(7)]
    base = volume_angles(theta)
    delta = 1e-3
    def mixed(a,b):
        if a==b:
            plus=theta.copy(); minus=theta.copy()
            plus[a]+=delta;minus[a]-=delta
            return (volume_angles(plus)-2*base+volume_angles(minus))/delta**2
        out=[]
        for sign1,sign2 in ((1,1),(1,-1),(-1,1),(-1,-1)):
            arr=theta.copy();arr[a]+=sign1*delta;arr[b]+=sign2*delta
            out.append(volume_angles(arr))
        return (out[0]-out[1]-out[2]+out[3])/(4*delta**2)
    for j in range(7):
        z=cmath.exp(2j*math.pi/7)
        exact=sum(H[0][j][e]*(z**e) for e in range(7)).real/768
        assert abs(exact-mixed(0,j)) < 3e-6, (j,exact,mixed(0,j))
    return vals

if __name__ == '__main__':
    ns = (5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 32)
    vals = [test_volume(n) for n in ns]
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    hessian = exact_hessian_coefficients()
    print(f"PASS: {len(ns)} complete ordered-facet determinant sweeps (n={ns}), exact heptagonal Hessian coefficients and symmetry, seven numerical Hessian entry comparisons.")
    print(f"P7 volume = {test_volume(7):.15f}; Fourier Hessian eigenvalues = {hessian}")
