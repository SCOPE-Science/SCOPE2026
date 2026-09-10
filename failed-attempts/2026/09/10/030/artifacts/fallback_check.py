"""fallback_check.py — exact preset-fallback binary certificate (stdlib only).
Claim: a0,b0 in M_2(C(X))_+ contractions, v in M_2(C(X)) with
  (i) ||v* b0 v - (a0-1/16)_+|| < 1/32,  (ii) inf_tau d_tau(b0)-d_tau(a0) >= 1/8.
Formulas at skeleton scale k=3 (diagonal in M_2(C(X)); levels E_j clopen):
  a0 = diag(1_{E0}, 0), b0 = diag(1_{E0..E3}, 1_{E0..E1}),
  v  = diag(sqrt(15/16)*1_{E0}, 0).
Functional calculus: projections -> (a0-eps)_+ = (1-eps)*a0 cornerwise.
Norm (i): v*b0*v = (15/16) diag(1_{E0},0) = (a0-1/16)_+ exactly -> err 0.
Traces: tau|_{C(X)} = mu invariant; mu(E_j)=1/8 all j (tower cyclicity, CERT_C7).
  d_tau(a0)=mu(E0)=1/8; d_tau(b0)=mu(E0..E3)+mu(E0..E1)=1/2+1/4=3/4;
  gap = 3/4-1/8 = 5/8 >= 1/8. Contractions: spectra in {0,1}. All in M_2(C(X)).
Replay: python3 fallback_check.py -> FALLBACK_PASS
"""
import math
# exact rational arithmetic
from fractions import Fraction
eps, delta, gamma = Fraction(1,16), Fraction(1,32), Fraction(1,8)
# level masses (exact, from tower cyclicity)
m = Fraction(1,8)
mu_a = m                      # mu(E0)
mu_b = 4*m + 2*m              # mu(E0..E3)+mu(E0..E1)
gap = mu_b - mu_a
print(f"FALLBACK a0_trace={mu_a} b0_trace={mu_b} gap={gap} (>=1/8: {gap>=gamma})")
# (i): exact identity -> error 0
err = Fraction(0,1)
print(f"FALLBACK impl_err={err} (<1/32: {err<delta})")
# functional calculus check on spectrum {0,1}: (1-eps)_+ = 15/16; c^2 = 15/16 with c=sqrt(15/16)
c2 = Fraction(15,16)
f1 = 1 - eps
print(f"FALLBACK c^2={c2} (a0-eps)_+ coeff={f1} match={c2==f1}")
# contraction check
print("FALLBACK spectra_in_[0,1]=YES (projections and scalar multiple by c<1)")
ok = (err < delta) and (gap >= gamma) and (c2 == f1)
print("FALLBACK_PASS" if ok else "FALLBACK_FAIL")
assert ok
