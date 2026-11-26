"""Independent finite checks for the fast-period directed-dispersal expansion.

Requires Python 3, NumPy, SciPy and SymPy. The general assertion is
proved analytically in RESULT.md; these tests verify selected instances.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

passed = 0


def check(condition, description):
    global passed
    if not condition:
        raise AssertionError(description)
    passed += 1


# A genuinely directed three-site cycle and three distinct seasons.
L_exact = sp.Matrix([[-1, 0, 1], [1, -1, 0], [0, 1, -1]])
seasons_exact = [sp.Matrix([2, -1, -1]),
                 sp.Matrix([-1, 2, -1]),
                 sp.Matrix([-1, -1, 2])]
p_exact = sp.ones(3, 1) / 3
q_exact = sp.ones(3, 1)
check(L_exact * p_exact == sp.zeros(3, 1), 'right Perron vector')
check(q_exact.T * L_exact == sp.zeros(1, 3), 'left Perron vector')
check(q_exact.dot(p_exact) == 1, 'Perron normalization')
check(sum(seasons_exact, sp.zeros(3, 1)) == sp.zeros(3, 1), 'zero average growth')

x = sp.Symbol('x', real=True)
starts = [sp.zeros(3, 1)]
for r in seasons_exact:
    starts.append(starts[-1] + r / 3)
primitive_mean = sum(((starts[j] + starts[j + 1]) / 6
                      for j in range(3)), sp.zeros(3, 1))
check(primitive_mean == sp.Matrix([sp.Rational(1, 3), 0, -sp.Rational(1, 3)]),
      'centering the temporal primitive')
M_exact = sp.zeros(3, 3)
for j, r in enumerate(seasons_exact):
    lo, hi = sp.Rational(j, 3), sp.Rational(j + 1, 3)
    H = starts[j] + (x - lo) * r - primitive_mean
    for a in range(3):
        for b in range(3):
            M_exact[a, b] += sp.integrate(H[a] * H[b], (x, lo, hi))
check(M_exact == sp.Matrix([[sp.Rational(1, 27), -sp.Rational(1, 54), -sp.Rational(1, 54)],
                            [-sp.Rational(1, 54), sp.Rational(1, 27), -sp.Rational(1, 54)],
                            [-sp.Rational(1, 54), -sp.Rational(1, 54), sp.Rational(1, 27)]]),
      'exact temporal covariance matrix')
C_exact = -sum((q_exact[a] * L_exact[a, b] * p_exact[b] * M_exact[a, b]
               for a in range(3) for b in range(3)), sp.Integer(0))
check(C_exact == sp.Rational(1, 18), 'exact directed-cycle curvature')
energy = sum((q_exact[a] * L_exact[a, b] * p_exact[b] *
              (M_exact[a, a] + M_exact[b, b] - 2 * M_exact[a, b]) / 2
              for a in range(3) for b in range(3) if a != b), sp.Integer(0))
check(energy == C_exact, 'exact Dirichlet-energy identity')

# Compare the analytic coefficient to the actual monodromy growth rate.
L_np = np.array(L_exact.tolist(), dtype=float)
R_np = np.array([list(r) for r in seasons_exact], dtype=float)
def floquet_rate(T, migration, season_rates, weights):
    product = np.eye(migration.shape[0])
    for row, w in zip(season_rates, weights):
        product = expm(T * w * (migration + np.diag(row))) @ product
    eigenvalues = np.linalg.eigvals(product)
    return math.log(max(abs(eigenvalues))) / T

for T in [0.2, 0.1, 0.05, 0.025]:
    observed = floquet_rate(T, L_np, R_np, np.ones(3) / 3)
    check(observed > 0, f'positive time-heterogeneity shift at T={T}')
    check(abs(observed / T**2 - 1 / 18) < 0.02 * T + 0.00001,
          f'quadratic coefficient at T={T}')

# Unequal seasons and a nonreversible migration generator with six edges.
L = np.array([[-1.2, 0.3, 1.5], [1.0, -0.5, 0.1], [0.2, 0.2, -1.6]])
R = np.array([[1.5, -2.5, 0.1], [0.1, 1.0, -1.0],
              [1.3, -1.0, 0.0], [-0.3, 1.4, 0.5]])
w = np.array([0.10, 0.25, 0.30, 0.35])
check(np.allclose(np.sum(L, axis=0), 0), 'column-conservative dispersal')
check(not np.allclose(L, L.T), 'nonreversible dispersal')
check(np.allclose(w.sum(), 1), 'full period')
means = w @ R
A0 = L + np.diag(means)
evals, evecs = np.linalg.eig(A0)
ind = np.argmax(evals.real)
lam0 = evals[ind].real
p = evecs[:, ind].real
if np.all(p < 0): p = -p
p /= p.sum()
evals_l, evecs_l = np.linalg.eig(A0.T)
ind_l = np.argmin(abs(evals_l - lam0))
q = evecs_l[:, ind_l].real
if np.all(q < 0): q = -q
q /= q @ p
check(np.all(p > 0) and np.all(q > 0), 'strictly positive Perron vectors')
check(abs(q @ p - 1) < 1e-12, 'left-right normalization')
check(np.max(abs(A0 @ p - lam0*p)) < 1e-12, 'Perron right equation')
check(np.max(abs(q @ A0 - lam0*q)) < 1e-12, 'Perron left equation')

D = R - means
pre = np.zeros(3)
starts = []
Hmean = np.zeros(3)
for duration, slope in zip(w, D):
    starts.append(pre.copy())
    Hmean += duration*pre + 0.5*duration**2*slope
    pre += duration*slope
check(np.max(abs(pre)) < 1e-12, 'periodic primitive closes')
M = np.zeros((3, 3))
for duration, slope, st in zip(w, D, starts):
    h = st - Hmean
    M += (duration*np.outer(h, h) +
          0.5*duration**2*(np.outer(h, slope)+np.outer(slope, h)) +
          duration**3*np.outer(slope, slope)/3)
Q = A0-lam0*np.eye(3)
C1 = -sum(q[i]*Q[i,j]*p[j]*M[i,j] for i in range(3) for j in range(3))
C2 = sum(q[i]*L[i,j]*p[j]*(M[i,i]+M[j,j]-2*M[i,j])/2
         for i in range(3) for j in range(3) if i != j)
check(abs(C1-C2) < 1e-13, 'two independent coefficient representations')
check(abs(C1-0.0103703081676231) < 1e-11, 'unequal-season reference coefficient')
check(C1 > 0, 'strict positive curvature')
for T in (0.08, 0.04, 0.02):
    observed = floquet_rate(T, L, R, w)
    check(observed > lam0, 'strict increase from averaged growth')
    check(abs((observed-lam0)/T**2-C1) < 0.003*T,
          f'quadratic error bound for T={T}')

# A common seasonal forcing is exactly immaterial for every period.
scalar_offsets = np.array([1.2, -1.0, 0.4, -0.2])
Rcommon = means[None, :] + scalar_offsets[:, None]
common_average = w @ scalar_offsets
constant_rate = max(np.linalg.eigvals(A0).real) + common_average
for T in (0.02, 0.2, 1.5):
    observed = floquet_rate(T, L, Rcommon, w)
    check(abs(observed - constant_rate) < 2e-11, 'exact scalar-forcing invariance')

print(f'PASS: {passed} assertions; three-season exact C={C_exact}; four-season C={C1:.15f}')
