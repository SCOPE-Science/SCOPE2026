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

# Verification

Run `python checker.py` in the same directory to reproduce deterministic checks of triangular gap distributions, exact power-only band moments, unbiased quadrature decomposition, summability exponents and numeric convergence of critical logarithmic tail-root constants. The script runs without third-party dependencies. The paper proof, rather than these finite checks, establishes all asymptotic and almost-sure assertions. The test exercises the singular density and the constants used in the second Borel–Cantelli argument but does not independently certify any infinite limit. Any sampling design that shares randomness across different \(n\) is outside scope. Independent audit has not been performed.
