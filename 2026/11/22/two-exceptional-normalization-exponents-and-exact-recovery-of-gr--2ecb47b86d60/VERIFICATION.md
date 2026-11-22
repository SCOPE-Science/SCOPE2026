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

# Verification boundaries

A self-contained analytic proof is in `RESULT.md`, and an executable, ordinary exact-rational diagnostic is in `check.py`. Running `python check.py` produces `PASS: 2501 exact rational checks`; it verifies the microscopic hypergeometric formula, the two distinct-protocol ambiguity pairs, exact integer-exponent rank transitions, and arithmetic-plus-inverse-mean joint injectivity for many support triples. These finite computations do **not** prove the rank formula for arbitrary real normalization exponents. The exact global proof uses the nonvanishing curvature of the curve \((t^p,t^{p+1})\) for \(p\notin\{0,-1\}\), and the explicit rank-two relations at the two exceptions. No independent scientific audit or external certification has been performed.
