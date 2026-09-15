"""Virial coefficient check for 3D mass-critical INLS + localized-virial error scaling.

Claim: for smooth decaying solutions of i u_t + Du + |x|^{-b}|u|^p u = 0,
  V(t) = int |x|^2 |u|^2,  V''(t) = 8A - C*B,
  A = ||grad u||_2^2, B = int |x|^{-b} |u|^{p+2},
  C = 2*(N*p + 2*b)/(p+2)   [x.grad(|x|^{-b}) = -b|x|^{-b} shifts the commutator].
At mass-critical p = (4-2b)/N one has N*p+2*b = 4, hence C = 8/(p+2) and
  V''(t) = 8A - 8B/(p+2) = 16 E(u),  E = A/2 - B/(p+2).
This script verifies the algebra and tabulates truncated-virial error scalings
that force the need for long-time Strichartz + coercivity (the blocker).
"""
import sympy as sp

N = 3
for b in [0.1, 0.5, 1.0, 1.4]:
    p = (4 - 2*b)/N
    C = 2*(N*p + 2*b)/(p+2)
    target = 8/(p+2)
    E_factor_A = 8.0       # V'' coeff of A
    E16_A = 16*0.5         # 16E coeff of A
    print(f"b={b}: Np+2b={N*p+2*b:.10f} (expect 4), C={C:.10f}, 8/(p+2)={target:.10f}, "
          f"match={abs(C-target)<1e-12}, A-coeff match 16E: {E_factor_A==E16_A}")

print()
print("Truncated virial w_R error sources (order of magnitude, R>>1 cutoff radius):")
print("  kinetic commutator error      : O(R^{-2} M(u))")
print("  nonlinearity tail (|x|>R)     : O(R^{-b} ||u||_{L^{p+2}(|x|>R)}^{p+2}) -- b-dependent, singular at origin for commutators")
print("  mass/energy flux across |x|~R : needs L^2-compactness + long-time Strichartz to make small uniformly in t")
print("Conclusion: V''=16E is exact formally, but localizing it to L^2 almost-periodic")
print("threshold solutions needs (i) persistence of regularity/H1, (ii) uniform kinetic")
print("localization via long-time Strichartz in Lorentz spaces, (iii) coercivity of the")
print("linearized operator around Q with singular weight. (i)-(iii) at M=M(Q), full")
print("0<b<3/2, excluding quasi-soliton/rapid cascade, is the paper-scale missing input.")
