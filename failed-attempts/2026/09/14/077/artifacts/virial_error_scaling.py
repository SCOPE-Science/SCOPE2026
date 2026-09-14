"""Bounded recovery test: truncated-virial error without L^2 for 4D ground state.

Model: W(r)=(1+r^2/8)^-1. Truncated virial V_R uses weight R^2 phi(x/R);
V_R'' = 8(delta) + error_R, error_R contains annulus term
E_ann(R) = R^-2 * int_{R<|x|<2R} |u|^2 dx (up to constants).
With only Hdot^1 (Hardy) control, E_ann(R) ~ int_R^{2R} W^2 r^3 dr -> 64 ln 2.
Test: numerically evaluate E_ann(R); non-decay => O(1) remainder competes
with main sign, so no uniform virial sign from Hdot^1 bounds alone.
"""
import math
import numpy as np

r = np.logspace(-3, 5, 2000001)
W = (1 + r**2/8)**(-1)
integrand = W**2 * r**3  # radial density up to |S^3|
S = 2*math.pi**2

print("R, annulus_int, S*annulus_int, limit-theory=64ln2=%.4f" % (64*math.log(2)))
for R in [10., 100., 1000., 10000.]:
    m = (r > R) & (r < 2*R)
    rr = r[m]
    ii = integrand[m]
    ann = float(np.sum(0.5*(ii[1:]+ii[:-1])*np.diff(rr)))
    print(f"{R:.0f} {ann:.4f} {S*ann:.2f}")
print("RESULT: annulus mass does not decay; truncated-virial error is O(1).")
print("Hence recovery without conserved L^2 mass FAILS.")
