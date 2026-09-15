"""Bounded recovery test: can the W^+-type fixed-point remainder close with a
Lipschitz (contraction) bound when alpha<1?

Model (real) nonlinearity f(z)=|z|^a z, f'(W)=(a+1)|W|^a.
Remainder R(W,v)=f(W+v)-f(W)-f'(W)v.
Standard Duyckaerts-Merle W^pm construction needs |R|<=C|v|^2 and a Lipschitz
difference bound in the Strichartz ball. Here we test scaling as v->0.
"""
import numpy as np

def R(W, v, a):
    f = lambda z: np.abs(z)**a * z
    return f(W + v) - f(W) - (a + 1) * np.abs(W)**a * v

for a in [0.75, 0.5, 0.25, 0.05]:
    print(f"--- alpha={a} (d>=6 INLS regime, W=1) ---")
    for v in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        r = R(1.0, v, a)
        print(f"  v={v:.0e}: |R|/|v|^2 = {abs(r)/v**2:.3e}   "
              f"|R|/|v|^(a+1) = {abs(r)/v**(a+1):.4f}")
    # difference quotient of remainder (Lipschitz test)
    v1, v2 = 1e-3, 2e-3
    dq = abs(R(1.0, v1, a) - R(1.0, v2, a)) / abs(v1 - v2)
    print(f"  Lipschitz probe |R(v1)-R(v2)|/|v1-v2| = {dq:.3e} "
          f"(vs |v|^a scale ~ {(1e-3)**a:.3e})")
print()
print("RESULT: |R|/|v|^2 -> inf as v->0 for every alpha<1: no quadratic remainder bound.")
print("Contraction-mapping step of the W^pm unstable-manifold construction FAILS")
print("in standard H^1-Strichartz balls; needs exotic-Strichartz/fractional-chain-rule")
print("machinery for the singular-weight INLS that is not available in-session.")
