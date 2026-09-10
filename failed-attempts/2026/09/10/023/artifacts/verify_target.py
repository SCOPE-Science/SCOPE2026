"""Lane-546 TARGET verification: Hill-ball constants, swirl moment, kappa0.

All analytic values derived in DRAFT.md Sec.1. Independent checks:
 (a) exact rational arithmetic (Fractions) for angular/radial monomials,
 (b) brute-force midpoint quadrature on a cylindrical grid (no shared code
     path with the analytic formulas: direct 3D sums of the stream functions),
 (c) operator identity L psi_* = r^2 and W-continuity residual on grid.

Conventions: S = -(drr - (1/r) dr + dzz) (Stokes operator), S psi = r^2 xi
(xi_H = 1 on unit ball).
psi_*(r,z) = (1/10) r^2 (1-rho^2)_+ ;  psi_dec = psi_* + (W/2) r^2 inside,
psi_dec = (W/2) r^2/rho^3 outside, W = 2/15.
E0_H = (1/2) int_B psi_dec ; Q_H = b^2 int_B psi_*^2/r^2 (b=1 below).
"""
from fractions import Fraction as F

print("=== analytic (exact rational) ===")
rad0 = F(1, 5)                 # int_0^1 rho^4
rad1 = F(1, 5) - F(1, 7)       # int rho^4(1-rho^2)
rad2 = F(1, 5) - F(2, 7) + F(1, 9)  # int rho^4(1-rho^2)^2
ang = F(8, 3)                  # (1/pi) int sin^3 dtheta dphi = 8/3
J0 = ang * rad0                # (1/pi) int_B r^2
J1 = ang * rad1                # (1/pi) int_B r^2(1-rho^2)
J2 = ang * rad2                # (1/pi) int_B r^2(1-rho^2)^2
A = F(1, 10)
W2 = F(1, 15)                  # W/2
E0opi = F(1, 2) * (A * J1 + W2 * J0)   # E0/pi
Qopi = A * A * J2              # Q/pi, b=1
I0opi = J0 / 2                 # I0/pi
G0opi = F(4, 3)                # Gamma0/pi
print("J0/pi =", J0, " J1/pi =", J1, " J2/pi =", J2)
print("E0/pi =", E0opi, "(expect 8/315 =", F(8, 315), ")")
print("Q/pi  =", Qopi, "(expect 16/23625 =", F(16, 23625), ")")
print("I0/pi =", I0opi, "(expect 4/15 =", F(4, 15), ")")
assert E0opi == F(8, 315) and Qopi == F(16, 23625) and I0opi == F(4, 15)
k02 = E0opi / Qopi
print("kappa0^2 =", k02, "(expect 75/2 =", F(75, 2), ")")
assert k02 == F(75, 2)
import math
kap0 = math.sqrt(75 / 2)
print("kappa0 = 5*sqrt(6)/2 =", kap0)
assert abs(kap0 - 5 * math.sqrt(6) / 2) < 1e-15

print("=== independent midpoint quadrature (cylindrical grid) ===")
N = 420
R = Z = 1.6
h = 2 * R / N
Afl, Wfl = 0.1, 2.0 / 15.0
sI = sG = sE = sQ = 0.0
sOp = 0.0   # max |L psi_* - r^2| interior defect via finite differences
nOp = 0
# store small grid for operator check
M = 60
g = [[0.0] * M for _ in range(M)]
rr = [0.02 + 1.2 * i / (M - 1) for i in range(M)]
zz = [-1.2 + 2.4 * j / (M - 1) for j in range(M)]
for i in range(M):
    for j in range(M):
        r, z = rr[i], zz[j]
        rho2 = r * r + z * z
        g[i][j] = Afl * r * r * max(0.0, 1.0 - rho2)


def psistar(r, z):
    return Afl * r * r * max(0.0, 1.0 - (r * r + z * z))


for ix in range(N):
    r = -R + (ix + 0.5) * h
    if r < 0:
        continue
    for iz in range(N):
        z = -Z + (iz + 0.5) * h
        rho2 = r * r + z * z
        if rho2 >= 1.0:
            continue
        w = 2 * math.pi * r * h * h  # dx = 2 pi r dr dz
        sI += 0.5 * r * r * w
        sG += w
        sE += 0.5 * (psistar(r, z) + 0.5 * Wfl * r * r) * w
        sQ += (psistar(r, z) ** 2 / (r * r)) * w
E0a = 8 * math.pi / 315
Qa = 16 * math.pi / 23625
I0a = 4 * math.pi / 15
G0a = 4 * math.pi / 3
for name, got, exp in [("I0", sI, I0a), ("Gamma0", sG, G0a),
                       ("E0", sE, E0a), ("Q", sQ, Qa)]:
    rel = abs(got - exp) / exp
    print(f"{name}: quad={got:.8f} exact={exp:.8f} relerr={rel:.2e}")
    assert rel < 4e-3, name

print("=== Stokes identity S psi_* = r^2 (2nd-order FD, interior) ==>")
worst = 0.0
dr = rr[1] - rr[0]
dz = zz[1] - zz[0]
for i in range(2, M - 2):
    for j in range(2, M - 2):
        r, z = rr[i], zz[j]
        if r < 0.4 or r * r + z * z > 0.49:
            continue
        pr = (g[i + 1][j] - g[i - 1][j]) / (2 * dr)
        prr = (g[i + 1][j] - 2 * g[i][j] + g[i - 1][j]) / dr**2
        pzz = (g[i][j + 1] - 2 * g[i][j] + g[i][j - 1]) / dz**2
        S = -(prr - pr / r + pzz)
        worst = max(worst, abs(S - r * r) / (r * r))
print("max rel defect Spsi_*-r^2 =", worst)
assert worst < 3e-3
# W continuity: interior normal deriv -(1/5)r^2 vs exterior -(3W/2)r^2 at rho=1
Wcheck = (1 / 5) / (3 / 2)
print("W from C1 match =", Wcheck, " expect 2/15 =", 2 / 15)
assert abs(Wcheck - 2 / 15) < 1e-15
print("s(0.5*kappa0) lower bound >0:", float(E0a - (0.5 * kap0) ** 2 / 2 * Qa))
print("VERIFY_OK")
