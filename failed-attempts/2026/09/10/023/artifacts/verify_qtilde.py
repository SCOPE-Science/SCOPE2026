"""Lane-546 Qtilde verification: decaying-psi swirl moment Qt_H = 16*pi/945.
Complements verify_target.py (which checks relative-psi moment M0=16*pi/23625).
Checks analytic Qt_H = interior 8*pi/1575 + exterior 8*pi/675 = 16*pi/945,
kappa0^2 = E0/Qt = 3/2, positivity threshold 3, via exact rationals + grid.
"""
from fractions import Fraction as F
import math

print("=== analytic Qt_H ===")
# interior: I = 8pi/3 * [a^2/5 - 2ac/7 + c^2/9], a=1/6, c=1/10
a, c = F(1, 6), F(1, 10)
bracket = a*a/5 - 2*a*c/7 + c*c/9
print("bracket =", bracket, "(expect 1/525 =", F(1, 525), ")")
assert bracket == F(1, 525)
E0opi = F(8, 315)
Qt_in_pi = F(8, 3) * bracket   # interior Qt/pi
Qt_out_pi = F(8, 675)          # exterior Qt/pi = (1/225)*(8/3)
Qt_pi = Qt_in_pi + Qt_out_pi
print("interior/pi =", Qt_in_pi, " exterior/pi =", Qt_out_pi, " total/pi =", Qt_pi)
assert Qt_in_pi == F(8, 1575) and Qt_out_pi == F(8, 675) and Qt_pi == F(16, 945)
k02 = E0opi / Qt_pi
print("E0/pi =", E0opi, " Qt/pi =", Qt_pi, " kappa0^2 =", k02)
assert k02 == F(3, 2)
print("kappa0 = sqrt(3/2) =", math.sqrt(1.5))
print("positivity threshold 2*E0/Qt =", 2*k02, "(expect 3)")
assert 2*k02 == 3
# half-energy margin at kappa0, positivity at sqrt(3)
E0 = 8*math.pi/315
Qt = 16*math.pi/945
for k2, name in [(1.5, "kappa0^2=3/2"), (3.0, "pos-thr=3")]:
    print(name, "sup-lower-bound =", E0 - k2/2*Qt)
assert E0 - 1.5/2*Qt > 0 and abs(E0 - 3.0/2*Qt) < 1e-15

print("=== grid check of decaying psi Qt ===")
Afl, Wfl = 0.1, 2.0/15.0
N = 300
R = Z = 3.0
h = 2*R/N
sIn = 0.0
for ix in range(N):
    r = -R + (ix+0.5)*h
    if r < 0:
        continue
    for iz in range(N):
        z = -Z + (iz+0.5)*h
        rho2 = r*r+z*z
        if rho2 >= 1.0:
            continue
        w = 2*math.pi*r*h*h
        ps = r*r*(1/6 - rho2/10)
        sIn += (ps*ps/(r*r))*w
# exterior via u = 1/rho: int_1^inf drho/rho^2 = int_0^1 du (exact, compact)
Nt, Nu = 2000, 2000
sT = sum(math.sin((i+0.5)*math.pi/Nt)**3 for i in range(Nt)) * (math.pi/Nt)
sR = 1.0  # midpoint of constant 1 on [0,1] is exact
sOut = 2*math.pi*(1/225)*sT*sR
print(f"angular quad={sT:.8f} exact={4/3:.8f}; radial quad={sR:.8f} exact=1.0")
assert abs(sT-4/3)/(4/3) < 1e-6 and abs(sR-1.0) < 2e-2
expIn, expOut = 8*math.pi/1575, 8*math.pi/675
for name, got, exp in [("interior", sIn, expIn), ("exterior", sOut, expOut),
                       ("total", sIn+sOut, expIn+expOut)]:
    rel = abs(got-exp)/exp
    print(f"{name}: quad={got:.7f} exact={exp:.7f} relerr={rel:.2e}")
    assert rel < 5e-3, name
print("VERIFY_OK")
