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

# Verification and reproducibility

Run `python verify.py` with Python 3 and `mpmath` to reproduce `check_output.txt`. The checker evaluates normalized incomplete-gamma integrals, successive ratios, strict log-concavity and endpoint mode ordering, bisection thresholds, and the sharp large-degree conditioning coefficient at 70-digit precision. The five-step test (total degree five and second radius squared equal to two) checks every transition and its two-level maximum. Tested large-degree parameters include equal and unequal radii and degrees 60, 120, and 220.

These are finite-precision computations at selected parameters, not a certificate for all integers, all positive radii, or an infinite limit. The logical proof of those universal statements is the positive-series ratio argument and Stirling saddle analysis in RESULT.md. The known quasi-radial diagonalization is credited as prior work. Literature priority is provisional and no independent audit has been performed.
