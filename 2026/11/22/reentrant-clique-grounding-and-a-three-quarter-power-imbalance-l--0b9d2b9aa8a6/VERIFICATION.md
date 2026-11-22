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
# Verification of the split-network grounding theorem

Execute `python3 verify.py` using Python 3.9+; no nonstandard dependencies are required. The script constructs the exact combinatorial Laplacian and diagonal gains, computes rational inverses with Gauss–Jordan elimination, and compares their traces against the analytic contrast-plus-quotient formula. It also verifies the exact directional derivative via the diagonal of the squared inverse, both endpoint signs, the normalized clique-support inequality, selected graph-size regimes, the eight-vertex cubic, and asymptotic-scale witnesses. The completed execution reported **712 assertions passed**.

These are finite checks, not an infinite proof and not exhaustive software verification. The general statement is proved by the strict-convexity, spectral-decomposition, endpoint-derivative and threshold-minimization arguments given in RESULT.md. The numerical large-size checks are only witnesses away from the critical boundary, and no assertion is made at the asymptotic equality case. Independently audited verification has not occurred.
