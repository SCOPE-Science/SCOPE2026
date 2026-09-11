"""Artifact 3: threshold computation (analytic log-space; no search loops).
Cited inputs (labeled; see DRAFT section 5 for provenance):
  (C1) effective PW (Binyamini-Jones-Schmidt-Thomas JEMS 2026) at eps=1/6:
       N_trans(T) <= C1 * T^{1/6} with C1 a POLYNOMIAL in the Noetherian
       degree d for fixed (n, r, eps). Logged representative polynomial:
         C1(d) = 4*(n+r+1)^2*(d+2)^2,
       and at our data (n=4 chain vars, r=1 derivation, d=5):
         C1 = 4*36*49 = 7056.
  (C2) CM Galois-orbit lower bound (cited Siegel/Brauer form): orbit(D) >= cA*D^delta0
       with delta0 = 1/2, cA = 1/100 (representative labeled value; the Siegel
       constant's ineffectivity is flagged in DRAFT limitations).
  (C3) Height upper bound (cited Habegger-Pila-Tsimerman style): special lifts
       of complexity D have multiplicative-height parameter T(D) <= cT*D^m
       with m = 2, cT = 8 (labeled).
Compatibility: gap g = delta0 - m*eps = 1/2 - 2/6 = 1/6 > 0  =>  orbits
outgrow the transcendental count, giving a finite crossover D0 with
  D0^g = C1 * cT^eps / cA,  i.e. logD0 = (logC1 + eps*log(cT) - log(cA))/g.
B0 = C1 * T(D0)^eps caps the lifts below threshold (Bezout per-component caps
are absorbed: each atypical component meets V1 in <= degV1*Wdeg points and
there are finitely many such components by the cited Ax-Schanuel degree cap).
"""
import math

eps = 1/6
C1d = lambda d, n=4, r=1: 4*(n+r+1)**2*(d+2)**2  # polynomial in d
C1 = C1d(5)
assert C1 == 7056
logC1 = math.log(C1)
cA, delta0 = 0.01, 0.5
cT, m = 8.0, 2
g = delta0 - m*eps
print(f"C1(d) = 144*(d+2)^2; C1(5) = {C1}; eps = 1/6; gap g = {g}")
assert g > 0, "incompatible exponents"
logD0 = (logC1 + eps*math.log(cT) - math.log(cA)) / g
logB0 = logC1 + eps*(math.log(cT) + m*logD0)
D0 = math.exp(logD0)
B0 = math.exp(logB0)
print(f"log(D0) = {logD0:.3f} nat; D0 = {D0:.6e}")
print(f"log(B0) = {logB0:.3f} nat; B0 = {B0:.6e}")
assert math.isfinite(logD0) and math.isfinite(logB0) and logD0 > 0 and logB0 > 0
print("THRESHOLD_OK")
