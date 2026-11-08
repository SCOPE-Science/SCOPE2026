"""Numerical spot checks for the stated two-circle quadratic intensity theorem.
Finite checks only: the accompanying proof establishes all quantified claims.
"""
import numpy as np


def vector(radius, angle):
    return np.array([1, radius * np.exp(-1j * angle), radius**2 * np.exp(-2j * angle)], dtype=complex)


def sample(H, radius, angle):
    w = vector(radius, angle)
    return float(np.real(np.vdot(w, H @ w)))


def basis():
    out = []
    for j in range(3):
        H = np.zeros((3, 3), dtype=complex)
        H[j, j] = 1
        out.append(H)
    for j, k in [(0, 1), (0, 2), (1, 2)]:
        H = np.zeros((3, 3), dtype=complex)
        H[j, k] = H[k, j] = 1
        out.append(H)
        H = np.zeros((3, 3), dtype=complex)
        H[j, k], H[k, j] = 1j, -1j
        out.append(H)
    return out


def matrix(rows):
    Hs = basis()
    return np.array([[sample(H, radius, angle) for H in Hs] for radius, angle in rows])


def kernel(r, s):
    return np.diag([r*r*s*s, -r*r-s*s, 1]).astype(complex)


def check(r, s, q):
    grid = [(rho, 2*np.pi*m/5) for rho in (r, s) for m in range(5)]
    A = matrix(grid)
    _, sing, vt = np.linalg.svd(A)
    assert (sing[:8] > 1e-9).all() and sing[-1] < 2e-12, sing
    K = kernel(r, s)
    assert np.max(np.abs([sample(K, rho, ang) for rho, ang in grid])) < 3e-12
    D = np.array([r*r*s*s, -(r*r+s*s), 1] + [0]*6, dtype=float)
    assert abs(np.vdot(vt[-1], D)) / np.linalg.norm(D) > 1 - 1e-11
    for u in [r/2, (r+s)/2, 2*s]:
        if min(abs(u-r),abs(u-s)) < 1e-12:
            continue
        B = matrix(grid + [(u, 0.37)])
        assert np.linalg.matrix_rank(B, tol=1e-9) == 9
        assert abs(sample(K, u, 0.37)-(u*u-r*r)*(u*u-s*s)) < 1e-11
    P = np.outer(q, q.conj())
    cap = (abs(q[1])**2 / (r*r+s*s)
           - abs(q[0])**2/(r*r*s*s) - abs(q[2])**2)
    for t in (0.0, max(cap, 0.0) * 0.5, max(cap, 0.0)):
        H = P + t*K
        assert np.min(np.linalg.eigvalsh(H)) > -2e-12
        assert max(abs(sample(H, rho, ang)-sample(P, rho, ang))
                       for rho, ang in grid) < 2e-11
    for t in (-0.1, max(cap, 0.0)+0.1):
        H = P + t*K
        assert np.min(np.linalg.eigvalsh(H)) < -1e-6
    if cap > 1e-6:
        H = P + cap * K
        ev = np.linalg.eigvalsh(H)
        assert abs(ev[0]) < 3e-11 and ev[1] > 1e-8


for r, s in [(0.55, 1.7), (0.8, 1.2), (1., 2.), (2., 3.)]:
    for q in [np.array([0, 1, 0], complex),
              np.array([0.03+0.01j, 1, 0.1j]),
              np.array([1, 0.01j, 0.3]),
              np.array([0, 0, 0])]:
        check(r, s, q)
P = np.diag([0, 1, 0]).astype(complex)
H = np.diag([4/5, 0, 1/5]).astype(complex)
assert abs(np.trace(P)-1) < 1e-13 and abs(np.trace(H)-1) < 1e-13
for rho in (1, 2):
    for j in range(9):
        assert abs(sample(P, rho, 2*np.pi*j/9)-sample(H, rho, 2*np.pi*j/9)) < 1e-11
assert abs(sample(H,3,.76)-sample(P,3,.76) - 8) < 1e-12

# Separate quadrature test of the Gaussian-STFT three-tone realization.
nodes, weights = np.polynomial.hermite.hermgauss(100)
Om, tim, omg = .3, .4, -.1
a = np.array([.3+.2j, -.1+.05j, .4-.1j])
x = tim + nodes/np.sqrt(np.pi)
f = sum(a[k]*np.exp(2j*np.pi*k*Om*x) for k in range(3))
quadrature = np.sum(weights*f*np.exp(-2j*np.pi*omg*x))/np.sqrt(np.pi)
q = np.array([a[k]*np.exp(-np.pi*k*k*Om*Om) for k in range(3)])
rho = np.exp(2*np.pi*Om*omg)
theta = 2*np.pi*Om*tim
analytic = np.exp(-2j*np.pi*omg*tim-np.pi*omg*omg)*np.sum(q*np.array([1,rho*np.exp(1j*theta),rho*rho*np.exp(2j*theta)]))
assert abs(quadrature-analytic) < 1e-12, (quadrature, analytic)
print('TWO_CIRCLE_PSD_FIBER_CHECKS_PASSED 16_SETS_AND_GAUSSIAN_STFT')
