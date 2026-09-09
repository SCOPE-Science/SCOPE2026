"""Geometry of X=PSL(2,Z)\\H and shortest closed geodesic C5. Replay: python3 geom.py"""
import mpmath as mp
mp.mp.dps = 50
sqrt5 = mp.sqrt(5)
u = (3+sqrt5)/2          # norm-1 fundamental unit, disc 5
L0 = 2*mp.log(u)         # length
assert abs((u + 1/u) - 3) < mp.mpf('1e-45')   # trace 3
assert abs(2*mp.cosh(L0/2) - 3) < mp.mpf('1e-45')
volX = mp.pi/3
print(f"L0 = {L0}")
print(f"L0 float = {float(L0)}")
print(f"vol(X) = {volX}")
for r in [mp.mpf('0.1'), mp.mpf('0.15'), mp.mpf('0.2')]:
    area = 2*L0*mp.sinh(r)
    print(f"r={r}: tube area={area}  ratio={area/volX}")
# collar width: arcsinh(1/sinh(L0/2))
w = mp.asinh(1/mp.sinh(L0/2))
print(f"collar half-width w = {w}  (0.15 embedded: {mp.mpf('0.15') < w})")
# Liouville mean of majorant supported in 0.15 is <= area(0.15)/vol
M0 = 2*L0*mp.sinh(mp.mpf('0.15'))/volX
print(f"M0 upper bound = {M0}")
print(f"gap to 1-1/40=0.975: {mp.mpf('0.975')-M0}")
print("GEOM_OK")
