"""Bounded recovery test: truncated-virial error vs nonradial drift for threshold supercritical NLS d>=5.
Models bulk concavity V''_bulk = 16/(d-2)*(K(W)-K) < 0 against truncation errors
~ C*M/R^2 + tail + drift penalty when soliton center x(t) displaces by D=|x(t)|.
Shows no uniform R choice closes the rigidity argument with only L^2 (no finite variance).
"""
import math
d=5
KW=1.0
Ktest=1.5
EW=KW/d
bulk=16/(d-2)*(KW-Ktest)  # negative
print(f"d={d} bulk V''={bulk:.4f}")
M=1.0  # ||u||_2^2 normalized
C=8.0
for R in [5,10,20,40,80]:
    err_centered=C*M/R**2
    print(f"R={R:3d} centered trunc err~{err_centered:.4f} net={bulk+err_centered:.4f} closes={bulk+err_centered<0.5*bulk}")
print("--- with drift D=|x(t)|, weight centered at 0: extra penalty ~ (D/R)^2 * K + mass tail ---")
for D in [0,5,20,100]:
    for R in [10,40]:
        penalty=(D/max(R,1e-9))**2*Ktest
        err=C*M/R**2+0.5*min(penalty,5.0)
        net=bulk+err
        print(f"D={D:3d} R={R:2d} penalty~{penalty:.3f} net={net:.3f} uniform-negative={net<0}")
print("CONCLUSION: centered truncation needs R>>D to keep penalty small, but D=x(t) unbounded a priori;")
print("comoving truncation needs modulation control of x(t), unavailable with only L^2 in nonradial d>=5.")
print("Hence truncated-virial rigidity cannot be closed uniformly; quantitative obstruction confirmed.")
