---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For strictly interior data the simplex is invariant and the exposure derivative is y=1−p>0. Independently, let w=z/x and L=1/x. In exposure s the difference of log derivatives first gives w=w0 exp(−hs); the remaining equation is L'=aL−b−(b+B)w. Integrating with exp(−as) and subtracting the edge condition L=1+w gives 1/p−1=(1/p0−F)/M with M=exp(−as)(1−q0+q0 exp(−hs)) and F as stated. Its derivative is exp(−as)[−(1−q0)A+q0D exp(−hs)]. For D≤0, or D>0 and q0≤A/(A+D), F is strictly decreasing for s>0 (including the equality at s=0). Otherwise it has the single positive maximum stated in the finding and H>F(0)=1. With no contact 1/p0−F is bounded below by a positive constant; positive y before any putative finite endpoint forces s→∞, and M→0 then forces p→0. A first simple root on the rising branch gives y proportional to the remaining exposure, exponential decay in t, and q>q_* by the strict logistic decrease. A double root at the maximum gives y=K(s_*−s)^2+O((s_*−s)^3) with K=hAD/[2(A+D)]. The physical-time integral diverges there and (s_*−s)t→1/K. The logistic slope gives (q−q_*)/(s_*−s)→h q_*(1−q_*), and z−q differs by O(y), proving both stated limits and their independence from the initial point on the separator. The independent replay python3 /workspace/checks/frozen_math_checks.py 1 uses the reciprocal x equation for the exact rational example; it verifies the threshold inequalities and exposure amplitudes 1/25 for y and 1/10 for z−1/2, consistent with physical-time coefficients 25 and 5/2.

## originality

PASS

Wang–Chen–Szolnoki already give the global ODE, the local edge threshold and phase portraits with basin proportions. Credit these results. Their root-of-f_G wording is not a covering exact interior theorem: Appendix B uses f_G for instantaneous drift, and the frozen critical example does not lie on its zero set. The distinct contribution is the exact initial-data separator, the global first-contact classification and the physical-time critical asymptotics.

## value

PASS

Local edge stability and phase portraits do not identify the outcome of an arbitrary strictly interior population state. An explicit global basin split resolves that issue in an established game, and the equality branch shows quantitatively different critical slowing with an initial-condition-independent coefficient. The value is in the full global classification and critical dynamics, not the integrating factor alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
