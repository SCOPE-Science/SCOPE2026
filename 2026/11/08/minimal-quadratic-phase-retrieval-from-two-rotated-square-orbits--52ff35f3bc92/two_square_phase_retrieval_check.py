"""Independent numerical checks for two rotated square-orbit polynomial magnitudes.

Run with: python two_square_phase_retrieval_check.py
Uses only NumPy and Python standard library; all scientific definitions are local.
"""
import itertools
import math
import numpy as np


def basis():
    E = []
    for j in range(3):
        h = np.zeros((3, 3), complex)
        h[j, j] = 1
        E.append(h)
    for j, k in [(0, 1), (1, 2), (0, 2)]:
        h = np.zeros((3, 3), complex)
        h[j, k] = h[k, j] = 1 / math.sqrt(2)
        E.append(h)
        h = np.zeros((3, 3), complex)
        h[j, k] = 1j / math.sqrt(2)
        h[k, j] = -1j / math.sqrt(2)
        E.append(h)
    return E


BASIS = basis()


def sample_matrix(r1, r2, alpha):
    zs = [r * np.exp(1j * (theta + k * math.pi / 2))
          for r, theta in [(r1, 0), (r2, alpha)] for k in range(4)]
    A = np.zeros((8, 9))
    for l, z in enumerate(zs):
        v = np.array([1, z, z * z])
        for i, H in enumerate(BASIS):
            A[l, i] = (v.conj() @ H @ v).real
    return A, zs


def predicted_values(r1, r2, alpha):
    u, v = r1 * r1, r2 * r2
    D = 2 * np.array([[1, u, u*u], [1, v, v*v]], float)
    C = 2 * np.array([[r1, r1**3], [r2, r2**3]], float)
    O = 2 * math.sqrt(2) * np.array([[u, 0],
                          [v*math.cos(2*alpha), -v*math.sin(2*alpha)]], float)
    return np.sort(np.concatenate((np.linalg.svd(D, compute_uv=False),
                                  np.tile(np.linalg.svd(C, compute_uv=False), 2),
                                  np.linalg.svd(O, compute_uv=False))))


def determinant_formula(r1, r2, alpha):
    u, v = r1*r1, r2*r2
    nk2 = (u*v)**2 + (u+v)**2 + 1
    return (2**18) * (u*v)**4 * (u-v)**6 * nk2 * math.sin(2*alpha)**2


def as_signal(y, zs):
    return np.array([sum(y[j] * z**j for j in range(3)) for z in zs], complex)


def assertion(condition, msg):
    global tests
    tests += 1
    if not condition:
        raise AssertionError(msg)


tests = 0
for r1, r2, alpha in itertools.product([.22, .4, .7, 1.1, 1.6],
                                        [.31, .58, .9, 1.4, 2.1],
                                        [.06, .17, math.pi/8, math.pi/4, .91, 1.32]):
    if abs(r1-r2) < 1e-12:
        continue
    A, zs = sample_matrix(r1, r2, alpha)
    actual = np.sort(np.linalg.svd(A, compute_uv=False))
    expected = predicted_values(r1, r2, alpha)
    assertion(np.allclose(actual, expected, rtol=1e-11, atol=5e-12),
              'block singular spectrum')
    formula = determinant_formula(r1, r2, alpha)
    direct = np.linalg.det(A @ A.T)
    assertion(np.isclose(formula, direct, rtol=4e-10, atol=1e-16), 'determinant')
    u, v = r1*r1, r2*r2
    K = np.diag([u*v, -(u+v), 1]).astype(complex)
    kvec = np.array([np.trace(H @ K).real for H in BASIS])
    assertion(np.linalg.norm(A @ kvec) <= 2e-12 * max(1,np.linalg.norm(A)),
              'explicit kernel')
    assertion(actual[0] > 1e-9, 'nonresonant lifting full row rank')
    # Perturb intensities from truly different signals; their lifted difference
    # cannot lie in the full-rank kernel.
    x = np.array([1.1+.2j, .3-.4j, -.6+.1j])
    y = np.array([-.5+.4j, 1.1+.7j, .5-1j])
    intensity_gap = np.linalg.norm(np.abs(as_signal(x, zs))**2 - np.abs(as_signal(y, zs))**2)
    assertion(intensity_gap > 1e-9, 'noncoincident intensities')

for r1, r2 in [(0.4, 1.2), (0.7, .7), (0, 1.2)]:
    for alpha in [0, math.pi/2, math.pi, 3*math.pi/2]:
        A, zs = sample_matrix(r1, r2, alpha)
        assertion(np.linalg.matrix_rank(A, tol=1e-9) < 8, 'resonant degeneracy')
        if r1*r2>0:
            a, b = np.array([1, 0, 1j]), np.array([1, 0, -1j])
            assertion(np.allclose(np.abs(as_signal(a, zs))**2,
                                     np.abs(as_signal(b, zs))**2, atol=1e-10),
                      'resonant ambiguity pair')

for r in [.2, .7, 1.3]:
    A, zs = sample_matrix(r,r,math.pi/4)
    a, b = np.array([r,0,0]), np.array([0,1,0])
    assertion(np.allclose(np.abs(as_signal(a, zs))**2,
                             np.abs(as_signal(b, zs))**2, atol=1e-11),
              'equal radii ambiguity pair')

for r in [.2, .8, 1.3]:
    A, zs = sample_matrix(0,r,math.pi/4)
    a, b = np.array([0,r,0]), np.array([0,0,1])
    assertion(np.allclose(np.abs(as_signal(a, zs))**2,
                             np.abs(as_signal(b, zs))**2, atol=1e-11),
              'zero radius ambiguity pair')

for r1, r2, alpha in [(0.4,0.9,math.pi/4), (0.1,1.6,math.pi/5),
                      (0.7,0.7,math.pi/4), (0,1.2,math.pi/4)]:
    A, zs = sample_matrix(r1, r2, alpha)
    assertion(np.linalg.matrix_rank(A, tol=1e-10) == (8 if r1*r2>0 and r1!=r2 else
                                                      5 if r1==r2 else 5),
              'rank at degenerate radii')

for r1, r2 in [(0.35,1.1), (.8,1.6)]:
    objective = []
    for angle in np.linspace(.01, math.pi/2-.01, 101):
        A, _ = sample_matrix(r1,r2,angle)
        objective.append(np.linalg.det(A @ A.T))
    A, _ = sample_matrix(r1,r2,math.pi/4)
    assertion(max(objective) <= (1+1e-12)*np.linalg.det(A@A.T),
              'quarter-turn-difference determinant optimum')

print('TWO_ROTATED_SQUARES_CHECKS_PASS', tests)
