"""Bounded recovery test for target: flux balancing on non-round C3 boundary pairs.

For a free-boundary minimal surface Sigma in B^3, minimality (Delta x = 0) plus
the free-boundary condition (outward conormal eta = position vector x along
dSigma) gives the balancing law  sum_i int_{Gamma_i} x ds = 0 in R^3.

Question tested: does this law obstruct non-round C3-invariant boundary curves,
i.e. could flux alone rule out exotic candidates (supporting uniqueness) or
constrain them? Family: z(phi) = c + eps*cos(3*phi), rho = sqrt(1-z^2), which
is C3-invariant (phi -> phi + 2pi/3) and an embedded graph over a latitude
circle for small eps. Mirror pair z -> -z models a top/bottom annulus boundary.
"""
import numpy as np

def flux(c, eps, n=400001):
    phi = np.linspace(0.0, 2 * np.pi, n)
    z = c + eps * np.cos(3 * phi)
    assert np.all(np.abs(z) < 1.0), "curve must stay on the sphere"
    rho = np.sqrt(1.0 - z ** 2)
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    dz = -3.0 * eps * np.sin(3 * phi)
    drho = -z * dz / rho
    dx = drho * np.cos(phi) - rho * np.sin(phi)
    dy = drho * np.sin(phi) + rho * np.cos(phi)
    speed = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    dphi = 2 * np.pi / (n - 1)
    w = np.ones(n)
    w[0] = w[-1] = 0.5
    Fx = float(np.sum(x * speed * w) * dphi)
    Fy = float(np.sum(y * speed * w) * dphi)
    Fz = float(np.sum(z * speed * w) * dphi)
    L = float(np.sum(speed * w) * dphi)
    return Fx, Fy, Fz, L

print("c, eps -> (Fx, Fy, Fz, length) per component; pair total")
for c, eps in [(0.5, 0.0), (0.5, 0.05), (0.5, 0.10), (0.3, 0.08)]:
    top = flux(c, eps)
    bot = flux(-c, -eps)  # mirror: z -> -z (C3 preserved)
    total = tuple(a + b for a, b in zip(top[:3], bot[:3]))
    print(f"c={c} eps={eps}: top F=({top[0]:+.3e},{top[1]:+.3e},{top[2]:+.6f}) "
          f"L={top[3]:.6f} | pair total=({total[0]:+.3e},{total[1]:+.3e},{total[2]:+.3e})")
print("CONCLUSION: Fx=Fy=0 for every eps by C3 symmetry; the mirror pair cancels")
print("Fz exactly for every eps. Flux is one scalar constraint met by a continuum")
print("of non-round candidates -> unobstructive. Test result: NEGATIVE (no decision).")
