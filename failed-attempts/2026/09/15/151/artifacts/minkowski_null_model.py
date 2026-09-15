"""Closed H^{m-2}-null set with infinite upper (m-2)-Minkowski content.

Model (m=3, so s=m-2=1): E = {0} U union_{j>=1} E_j, where E_j is a maximal
s_j-separated net on the sphere S_{R_j} of radius R_j = 2^{-j} in R^3, with
separation s_j = 2 * r_j, r_j = 2^{-j^2}/4. Each E_j is finite; E is countable
(hence H^1(E) = 0) and compact (finite union near any r>0 plus accumulation at 0).

Lower bound: M_j = #E_j >= c*(R_j/s_j)^2 (sphere area / cell area). The balls
B_{r_j}(p), p in E_j, are disjoint, so |B_{r_j}(E)| >= M_j * (4/3) pi r_j^3.
Ratio |B_{r_j}| / r_j^2 >= M_j * (4/3) pi r_j -> infinity since
M_j * r_j ~ (R_j/s_j)^2 * r_j ~ R_j^2 / r_j = 2^{-2j+j^2}/4 -> inf.

This proves in general that H^{m-2}-null (Thm 1.5) cannot imply the target
Minkowski bound without extra structure; the missing structure (uniform decay /
holes control) is exactly what Routes A/B show to fail.
"""
import math

print(f"{'j':>3} {'R_j':>10} {'r_j':>10} {'M_j lower':>12} {'Vol lower':>12} {'Vol/r^2':>12}")
for j in [1, 2, 3, 4, 5, 6]:
    R = 2.0**-j
    r = 2.0**(-j*j) / 4.0
    s = 2*r
    c = 0.5  # packing efficiency constant (conservative)
    M = c * (R/s)**2
    V = M * (4.0/3.0) * math.pi * r**3
    print(f"{j:3d} {R:10.2e} {r:10.2e} {M:12.2e} {V:12.2e} {V/r**2:12.2e}")
print("\nVol/r^2 -> infinity: H^1-null does NOT imply finite upper Minkowski content.")
print("E countable => H^1(E)=0; E compact (only accumulation point 0).")
