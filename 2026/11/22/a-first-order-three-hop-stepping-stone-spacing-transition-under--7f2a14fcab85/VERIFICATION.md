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

# Verification and limits

Reproduction: run `python verify.py` using the standard Python library; the actual package script returned `CHECKS_PASSED 76359`, `THRESHOLD 2.847567859346249`, and short/long normalized gaps near `0.629489479444062` and `1.588588900458124`. Decimal bisection at 65-digit precision independently reproduced the threshold, in agreement with the analytic crossing equation. Supplementary finite grid/random checks cover feasible triples and all objective regions but are not exhaustive proofs.

The mathematical proof is in RESULT.md: compactness and inward first variation, classification of all stationary points, Hessian exclusion of a second branch, exact endpoint cost signs, and strictly negative envelope derivative. The algebraic two-hop identity independently establishes continuity of the shorter-route transition.

The outcome depends on three mandatory conditionally independent hops, identical inverse-quadratic length success, and a fixed sum of nonnegative gaps. It does not establish any empirical species calibration, species-specific optimal reserve design, absolute historical first discovery, or independent expert audit.
