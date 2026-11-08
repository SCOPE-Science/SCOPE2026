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

# Reproducibility and scope

Execute `python3 verify.py` using Python 3.10 or later. The checker uses only Python's standard library. It independently computes the auxiliary function, numerically bisects its unique maximum, checks the root locations across the four phase regimes and the two critical boundaries, and verifies the exact algebraic reduction of the original drift at numerous high-precision points.

These finite numerical computations do **not** certify the global number of roots or the absence of other equilibria. The proof of unimodality uses the derivative sign, the strict decrease of \(\tanh(2x)/x\), and the endpoint signs in `RESULT.md`.

The decimal threshold is an approximation to a uniquely specified exact real constant. The scientific classification is for a single persuadable opinion with fixed zealots \(-1\) and \(+1\), sigmoid steepness \(\gamma=1\), and nonnegative \(\delta\). No independent scientific validation has been performed.
