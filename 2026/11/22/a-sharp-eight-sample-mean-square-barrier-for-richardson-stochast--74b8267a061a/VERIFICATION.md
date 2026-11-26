---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the stationary OU generator, Lx²=2−2x² and L²x²=−2Lx², so a_m=−2+2S₂/S₄ and b_m=−2a_m. The Gram S₄/m is positive almost surely and iid sample averages give a_m→−4/3 almost surely. With R²~χ²_m independent of U=ΣΘ_i⁴∈[1/m,1], a_m+2=2/(R²U). Its qth absolute moment is finite exactly for m>2q, and χ² small-ball normalization gives P(a_m>z)~E[U^(−m/2)]z^(−m/2)/Γ(1+m/2). The multipliers are polynomials of degrees 1,2,1 (degree 0 for generator-Taylor when h=1), with leading coefficients h,h²/2,h−h². The integrated squared loss against e^(−2h)x²+1−e^(−2h) is 3Q²−2(1+2e^(−2h))Q+1+2e^(−4h). Hence Q's second moment controls the loss, and a leading monomial k a_m^d in Q yields P(loss>z)~C_m(3k²)^(m/(4d))z^(−m/(4d)); there is no unbounded negative branch for a_m. This proves all thresholds, tail constants, and logarithmic divergence at exponent one. At h=1 the Taylor loss is the deterministic 2(1−e^(−2))². The frozen verify.py was inspected, not run; its exact finite algebra cannot establish integrability or asymptotics.

## originality

PASS

The update maps, Gaussian polar decomposition and inverse-chi-square moments are prior; the surviving contribution is their exact unconditional one-step risk comparison for this noninvariant OU dictionary, including the finite sample budgets, tail constants and Taylor cancellation. Closest inspected results do not cover this conjunction. Priority is bounded by the inspected evidence.

## value

PASS

The sharp mismatch at m=5,…,8 identifies a real statistical tradeoff for higher-order extrapolation: even an almost surely invertible Gram and negative population generator do not guarantee finite unconditional risk. The rare-error rates and exact budget needed to recover square integrability are useful design diagnostics, and the separate Taylor action isolates the cause. Scope is one unregularized, reused-sample step with the stated dictionary, not typical numerical accuracy or long-horizon behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
