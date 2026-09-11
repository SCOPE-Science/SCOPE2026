"""Kerr horizon deficit curve + trivial Rayleigh proxy vs claimed floor (m=1).
Proxy: H_star = 1/sqrt(lam_triv), lam_triv = 4*pi/A (constant-test-function upper bound
on principal eigenvalue, ignoring -|S|^2 and shear terms which only lower the average).
Claimed floor: H_floor = sqrt(A)/(8*sqrt(delta)).
Ratio R = H_star/H_floor = 8*sqrt(delta)/sqrt(lam_triv*A).
If R -> 0 as delta -> 0, the standard trivial bound cannot establish the floor;
a delta-explicit eigenvalue bound lam1*A <= 64*delta would be needed (up to logs/onset).
Stdlib only.
"""
import math
m = 1.0
print(f"{'a':>8} {'r+':>8} {'A':>10} {'J':>8} {'delta':>12} {'lam_triv':>12} {'H_star':>8} {'H_floor':>10} {'R':>10}")
for a in [0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 0.9999]:
    r = m + math.sqrt(m*m - a*a)
    A = 4*math.pi*(r*r + a*a)  # = 8*pi*m*r
    J = a*m
    delta = (r*r + a*a)/(2*a*m) - 1.0  # = r/a - 1 for m=1 since r^2+a^2=2r
    lam_triv = 4*math.pi/A
    H_star = 1.0/math.sqrt(lam_triv)
    H_floor = math.sqrt(A)/(8*math.sqrt(delta))
    R = H_star/H_floor
    print(f"{a:8.4f} {r:8.5f} {A:10.5f} {J:8.4f} {delta:12.6e} {lam_triv:12.6e} {H_star:8.4f} {H_floor:10.4f} {R:10.4f}")
# Check: A = 8*pi*m*r identity
# delta = r/a - 1 check
print("sanity: for a=0.99, r/a-1 =", (1+math.sqrt(1-0.99**2))/0.99 - 1)
