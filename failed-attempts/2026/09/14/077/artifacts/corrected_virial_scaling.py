"""Corrected virial-error scaling for 4D ground state W(r)=(1+r^2/8)^-1.

Corrects output/artifacts/virial_error_scaling.py, which reported the unweighted
annulus mass M_ann(R)=int_{R<|x|<2R}|W|^2 dx -> S*64 ln2 (constant) and called it
O(1) remainder. The true truncated-virial coefficient is R^-2*M_ann(R), which for
the FIXED profile decays like ~875/R^2 (see table). Pointwise-in-R decay holds.

The genuine obstruction is uniformity in time: for a noncompact trajectory with
only Hdot^1 bounds, sup_t R^-2*M_ann[u(t)](R) need not be small, by Hardy
sharpness and absence of conserved mass. This script documents both facts.
"""
import math
import numpy as np

r = np.logspace(-3, 6, 2000001)
W = (1 + r**2/8)**(-1)
S = 2*math.pi**2

print("R, M_ann, R^-2*M_ann (fixed profile W)")
for R in [10., 30., 100., 300., 1000., 3000., 10000.]:
    m = (r > R) & (r < 2*R)
    rr = r[m]
    ii = (W[m]**2)*(rr**3)
    Mann = S*float(np.sum(0.5*(ii[1:]+ii[:-1])*np.diff(rr)))
    print(f"R={R:>7.0f}  M_ann={Mann:8.2f}  R^-2*M_ann={Mann/R**2:.3e}")
print("CONCLUSION: pointwise decay holds for fixed W; uniform-in-t decay without")
print("L^2 mass conservation remains unproved and is the true blocking gap.")
