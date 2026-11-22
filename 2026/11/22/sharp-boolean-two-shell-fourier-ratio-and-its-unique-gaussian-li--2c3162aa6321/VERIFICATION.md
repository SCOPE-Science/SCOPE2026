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

The exact formulas were derived using the unitary Walsh convention. The supplementary `checker.py` ran on Python 3 and passed 503 checks: direct Walsh-transform equality and random complex comparisons in dimensions two through seven, exact rational binomial evaluations, larger-dimensional evaluations through dimension 320, and bisection of the Gaussian stationarity equation. The script uses no external packages and is bundled with the proof.

The infinite-dimensional statements follow from the analytic proof rather than finite enumeration. In particular, the checker cannot certify that no untested real parameter or complex coefficient beats the bound, nor can finite evaluations certify the Gaussian limit. Those facts use strict sign-sector concavity, Euclidean Minkowski equality and Gaussian-tail estimates.

The motivating source's initial public arXiv date was checked against its version history; it is September 18, 2026. Closest mathematical comparisons were made against accessible full-text discussions rather than titles alone. Equivalence to an unindexed earlier Gaussian two-mode extremal calculation remains possible. Independent mathematical validation has not been performed.
