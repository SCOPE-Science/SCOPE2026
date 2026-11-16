"""Independent finite census and exact identities for Lebedev 14-node quadratic sampling.

Run: python check_lebedev14.py  (NumPy and SymPy installed).
"""
import itertools
import numpy as np
import sympy as sp

pts = []
wts = []
for j in range(3):
    for s in (-1, 1):
        v = [0., 0., 0.]
        v[j] = float(s)
        pts.append(v)
        wts.append(1./15.)
for eps in itertools.product((-1, 1), repeat=3):
    pts.append([a / np.sqrt(3.) for a in eps])
    wts.append(3./40.)
pts = np.asarray(pts)
wts = np.asarray(wts)
assert len(pts) == 14 and np.allclose(np.sum(wts), 1)

# Independent real orthonormal spherical-harmonic basis for probability area measure.
def eval9(x):
    a, b, c = x
    return [1., np.sqrt(3.)*a, np.sqrt(3.)*b, np.sqrt(3.)*c,
            np.sqrt(15.)*a*b, np.sqrt(15.)*a*c, np.sqrt(15.)*b*c,
            (np.sqrt(15.)/2.)*(a*a-b*b),
            (np.sqrt(5.)/2.)*(3*c*c-1)]

E = np.sqrt(wts)[:, None]*np.asarray([eval9(x) for x in pts])
assert np.max(np.abs(E.T @ E-np.eye(9))) < 1e-12

best = -1.
winners = []
invertible = 0
for S in itertools.combinations(range(14), 9):
    lam = np.linalg.eigvalsh(E[list(S)].T @ E[list(S)])[0]
    invertible += lam > 1e-9
    if lam > best + 1e-9:
        best = lam
        winners = [S]
    elif abs(lam-best) <= 1e-9:
        winners.append(S)
assert len(winners) == 6
assert abs(best-0.2) < 1e-11
assert invertible == 1456

expected_winners = []
for j in range(3):
    for s in (-1, 1):
        erasures = {2*j + (0 if s == -1 else 1)}
        erasures.update(k for k in range(6,14) if pts[k,j] * s < 0)
        expected_winners.append(tuple(k for k in range(14) if k not in erasures))
assert set(winners) == set(expected_winners)

# Exact symbolic quadrature test for all coordinate monomials through degree four.
r = sp.sqrt(3)
exact_pts = []
exact_wts = []
for j in range(3):
    for sign in (-1, 1):
        v = [sp.Integer(0)]*3
        v[j] = sp.Integer(sign)
        exact_pts.append(tuple(v))
        exact_wts.append(sp.Rational(1,15))
for eps in itertools.product((-1, 1), repeat=3):
    exact_pts.append(tuple(sp.Integer(s)/r for s in eps))
    exact_wts.append(sp.Rational(3,40))
assert sum(exact_wts) == 1
for a in range(5):
    for b in range(5-a):
        for c in range(5-a-b):
            got = sp.simplify(sum(w * (v[0]**a)*(v[1]**b)*(v[2]**c)
                                  for v,w in zip(exact_pts,exact_wts)))
            if (a%2) or (b%2) or (c%2):
                want = sp.Integer(0)
            else:
                # E[x^(2i)y^(2j)z^(2k)] = ((2i-1)!! ...)/((2n+1)!!).
                def oddfac(n):
                    return sp.factorial2(2*n-1) if n else sp.Integer(1)
                i,j,k=a//2,b//2,c//2
                want=sp.Rational(oddfac(i)*oddfac(j)*oddfac(k),oddfac(i+j+k+1))
            assert sp.simplify(got-want) == 0, (a,b,c,got,want)

K=lambda t:(15*t*t+6*t-3)/2
B=sp.Matrix([[sp.sqrt(exact_wts[i]*exact_wts[j])*K(sum(exact_pts[i][h]*exact_pts[j][h] for h in range(3)))
               for j in range(14)] for i in range(14)])
assert all(sp.simplify(e) == 0 for e in (B*B-B))
T = tuple(k for k in range(14) if k not in expected_winners[0])
Q = B.extract(T,T)
chi = sp.factor(Q.charpoly('z').as_expr())
z=sp.Symbol('z')
want = (z-sp.Rational(4,5))**2 * (z-sp.Rational(1,2)) * ((z-sp.Rational(3,5))**2 - (r-1)**2/sp.Integer(50))
assert sp.simplify(chi-want) == 0, (chi,sp.factor(want))
assert sp.simplify((sp.Rational(4,5)-sp.Rational(3,5))*(sp.Rational(4,5)-sp.Rational(27,40))
                   - ((1+r)/(10*sp.sqrt(2)))**2) == (1-2*r)/200

print('LEBEDEV14_VERIFY_OK Parseval=PASS monomials_to_degree4=PASS')
print('LEBEDEV14_VERIFY_OK all_9_subsets=2002 invertible=1456 maximizers=6 sharp_lower_bound=1/5')
print('LEBEDEV14_VERIFY_OK exact_removed_gram_polynomial=PASS pair_obstruction=PASS')
