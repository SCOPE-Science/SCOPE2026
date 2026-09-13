"""Script M: certified bunching data. det Df = 1 exactly; uniform bounds:
stable contraction Lambda_s <= 0.221 (certified, kappa=0.5 cone);
unstable area expansion: det(Df|_{Ku}) >= ? via det=1/Lambda_s_row... simpler:
for v1,v2 in unstable cone, |Df v1 wedge Df v2| >= sigmin(B)^2 ... with certified
sigmin(B) >= 1.371 => area factor >= 1.88 pointwise. Report all certified numbers."""
import math
print("certified sigmin(B) >= 1.371  =>  unstable area expansion >= 1.371^2 =",1.371**2)
print("stable contraction <= 0.2206 (kappa=0.5 cone, script K)")
print("spectral values of A: 0.1980622642 / 1.5549581321 / 3.2469796037 (exact bisection, script A)")
print("weak expansion (linear): 1.5549; certified nonlinear per-vector lower bound on Ku(0.5):")
print("  |y'| >= (sigmin(B) - kap|c|)|y| = 1.371-0.5*0.4756 =",1.371-0.5*0.4756)
print("  => lambda_w >= 1.133 pointwise CERTIFIED (>1: uniform expansion, no mostly-expanding subtlety)")
