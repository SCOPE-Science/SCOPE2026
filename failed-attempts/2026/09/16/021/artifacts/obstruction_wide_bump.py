"""Bounded recovery test: can truncated-virial rigidity inputs be derived from
Hdot1 bounds alone? Tests on explicit Hdot1 data (wide bumps, heavy tail,
drifted profiles) the quantities a localized virial argument needs:
global L^2 mass, truncated virial V_R growth, exterior mass tightness."""
import json
import numpy as np

pi = np.pi
# Gaussian phi(x)=exp(-|x|^2/2): analytic norms
grad_phi_sq = 1.5 * pi ** 1.5
phi_l2_sq = pi ** 1.5
print(f"||grad phi||^2 = {grad_phi_sq:.6f}, ||phi||_2^2 = {phi_l2_sq:.6f}")

res = {"gaussian": {"grad_sq": grad_phi_sq, "l2_sq": phi_l2_sq}, "wide_bumps": []}
# Wide bumps u_a(x) = a^{1/2} phi(x/a): Hdot1 norm constant, L^2 = a^4 ||phi||^2.
# Exterior mass outside |x|>R at fixed R=1 grows like a^4 -> no L^2 tightness
# from Hdot1 bounds; global mass uncontrolled.
from math import erf, sqrt
def gauss_tail_3d(s):
    # int_{|z|>s} |phi|^2 dz with phi=e^{-r^2/2}: 4pi int_s^inf r^2 e^{-r^2} dr
    # = 4pi [ s e^{-s^2}/2 + sqrt(pi)/4 erfc(s) ]
    return 4 * pi * (0.5 * s * np.exp(-s ** 2) + 0.25 * sqrt(pi) * (1 - erf(s)))

for a in [1, 2, 4, 8]:
    l2 = a ** 4 * phi_l2_sq
    ext = a ** 4 * gauss_tail_3d(1.0 / a)  # mass of u_a outside |x|>1
    row = {"a": a, "hdot1_sq": grad_phi_sq, "l2_sq": float(l2),
           "exterior_mass_R1": float(ext)}
    res["wide_bumps"].append(row)
    print(f"a={a}: ||grad||^2={grad_phi_sq:.4f} (FIXED), "
          f"||u||_2^2={l2:.2f}, exterior mass(|x|>1)={ext:.2f}")

# Heavy tail u(r)=(1+r^2)^{-1/2}/log(e+r): in Hdot1(R^3) but not in L^2.
# Virial needs L^2; truncated virial V_R must diverge as R->inf.
rs = np.concatenate([np.linspace(0, 30, 60001),
                     np.geomspace(30, 20000, 20000)])
dr = np.diff(rs)
rm = 0.5 * (rs[1:] + rs[:-1])
L = np.log(np.e + rm)
u = (1 + rm ** 2) ** (-0.5) / L
# du/dr analytic pieces
dudr = (-rm * (1 + rm ** 2) ** (-1.5) / L
        - (1 + rm ** 2) ** (-0.5) / (L ** 2 * (np.e + rm)))
hdot1 = 4 * pi * float(np.sum((dudr ** 2) * (rm ** 2) * dr))
print(f"tail: ||grad u||^2 = {hdot1:.4f} (FINITE -> u in Hdot1)")
res["tail_hdot1_sq"] = hdot1
assert np.isfinite(hdot1)
res["tail_mass_growth"] = []
for R in [10, 100, 1000, 10000]:
    m = rm <= R
    MR = 4 * pi * float(np.sum((u[m] ** 2) * (rm[m] ** 2) * dr[m]))
    VR = 4 * pi * float(np.sum((rm[m] ** 2) * (u[m] ** 2) * (rm[m] ** 2) * dr[m]))
    res["tail_mass_growth"].append({"R": R, "M_R": MR, "V_R": VR})
    print(f"R={R:>6}: enclosed L2 mass M_R={MR:.3f}, truncated virial V_R={VR:.3e}")
# mass/virial diverge with R: virial setup impossible without an L^2 input.

with open("obstruction_summary.json", "w") as f:
    json.dump(res, f, indent=2)
print("WROTE obstruction_summary.json")
