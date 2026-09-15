"""Scaling obstruction for L^2-free localized virial (radial energy-critical NLS).

Model profile v(y) = exp(-|y|^2/2) (Schwartz stand-in for a tight profile).
Spreading sequence u_lam(x) = lam^((N-2)/2) v(lam x), lam -> 0
(fixed Hdot^1/energy scale, L^2 mass ~ lam^-1 -> infinity: no L^2 bound).

Weight: COMPACTLY SUPPORTED phi_R(x) = R^2 phi(x/R), phi(z)=|z|^2 for |z|<=1,
smooth cutoff to phi = 0 for |z| >= 2 (finite on Hdot^1 data without L^2).
The constant-at-infinity truncated weight is deliberately NOT used: it needs L^2.

Quantities vs lam:
  V_R(lam)        = int phi_R |u_lam|^2            (virial action)
  ext_frac(lam)   = int_{|x|>R} |u|^2* / int |u|^2* (fraction of nonlinear error outside R)
  mass_err(lam)   = R^-2 int_{R<=|x|<=2R} |u|^2     (Delta^2 phi_R mass-error scale)
Fixed R: V -> 0 but ext_frac -> O(1), so V'' = 8Q + O(1)*Q has uncontrolled sign.
Adapted R = R0/lam: ext small but V ~ lam^-2 -> infinity, so concavity crossing
time T* ~ sqrt(V/delta) -> infinity: no UNIFORM finite-time bound.
Either way no time-uniform virial contradiction along a spreading sequence.
"""
import numpy as np

def smoothstep(t):
    t = np.clip(t, 0.0, 1.0)
    return t**3 * (10.0 - 15.0*t + 6.0*t**2)

def phi_of_z(z):
    z = np.asarray(z, dtype=float)
    out = np.zeros_like(z)
    m1 = z <= 1.0
    m2 = (z > 1.0) & (z < 2.0)
    out[m1] = z[m1]**2
    out[m2] = z[m2]**2 * (1.0 - smoothstep(z[m2] - 1.0))  # C^2 cutoff to 0 at z=2
    return out

def compute(N, lam, R, rmax=80.0, n=400001):
    r = np.linspace(0, rmax, n)
    dr = r[1] - r[0]
    w = r**(N-1)  # radial surface factor up to constant (ratios only)
    u = lam**((N - 2) / 2.0) * np.exp(-0.5 * (lam * r)**2)
    phiR = R**2 * phi_of_z(r / R)
    V = np.sum(phiR * u**2 * w) * dr
    p = 2 * N / (N - 2)
    dens = np.abs(u)**p * w
    tot = np.sum(dens) * dr
    ext = np.sum(dens[r >= R]) * dr
    ann = (r >= R) & (r <= 2 * R)
    mass = R**(-2) * np.sum((u[ann]**2) * w[ann]) * dr
    return V, (ext / tot if tot > 0 else float("nan")), mass

for N in [3, 4, 5]:
    print(f"N={N}")
    for lam in [1.0, 0.5, 0.2, 0.1, 0.05]:
        Vf, frac, mass = compute(N, lam, R=5.0)
        Va, fraca, massa = compute(N, lam, R=5.0 / lam)
        print(f"  lam={lam:5.2f} fixedR: V={Vf:9.4f} ext_frac={frac:.3f} mass={mass:.4f} "
              f"| adaptedR: V={Va:12.1f} ext_frac={fraca:.3f} mass={massa:.4f}")
    print()
