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

`checker.py` is standalone and requires only Python 3 standard-library modules. Execute `python3 checker.py` from the extracted directory. It returned `PASS 4246 assertions`; the exact rational components verify the beta-mixture formula for sample sizes 1 through 30, the harmonic normalization and first two reciprocal-degree moments, the two-tag rectangle relation on a rational grid, the exponential minimum identity, and direct-versus-offline graph-degree calculations. The seeded simulation of 2,000 samples with 500 vertices returned empirical mean 6.61600 and variance 16.60854, compared with theoretical mean 6.79282 and asymptotic variance benchmark 18.64382.

Finite enumeration and simulation do not certify the infinite limit. That limit is proved analytically in `RESULT.md`, using an explicit negligible-direct-edge bound, the exponential coordinate transformation, and dominated convergence of an integrable shared-neighbor overlap kernel. The exact limiting overlap integral equals two; the tagged marginal contribution equals one. No independent external audit or validation has been performed.
