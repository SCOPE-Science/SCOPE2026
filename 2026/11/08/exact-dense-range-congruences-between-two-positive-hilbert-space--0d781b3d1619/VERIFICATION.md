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

# Reproducibility and limits

Run `python3 check_dense_range.py` after extracting this package. The checker returns `DENSE_RANGE_EXACT_CHECK_OK 74089` using integers and exact rational arithmetic, and verifies sample index partitions, coefficients, and the pullback identities. The analytic proof covers every index, density of both ranges, and the Calkin spectral obstruction; finite tests alone do not establish any of these infinite-dimensional conclusions. No external independent audit has been performed.
