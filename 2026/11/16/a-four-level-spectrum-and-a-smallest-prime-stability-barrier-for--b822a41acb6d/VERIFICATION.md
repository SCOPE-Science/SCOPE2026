---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The mathematical claim concerns exactly the normalized primitive-frequency Fourier matrix defined in `RESULT.md`, for two distinct primes and \(q\) consecutive input columns. `check_spectrum.py` builds the complex matrix directly, constructs the normalized Gram matrix again using prime Ramanujan sums, and checks the resulting complete eigenvalue list against rational formulas. The run passed 465 assertions across 93 prime pairs, with \(p\le13\) and \(q\le67\).

The proof's critical steps are the three-case Ramanujan kernel, the class-sum Cauchy inequality, the \(p\)-class block decomposition and its residual two-dimensional trace, and the separate \(s=1\) least-eigenvalue case. Finite tests do not prove these steps for all primes; the algebra in `RESULT.md` does. No independent external review or certification has taken place. A closely related published frame-potential result was accessible only as a summary, so the historical-priority assessment remains provisional.
