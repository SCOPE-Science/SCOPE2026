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

The main result follows from the explicit two-geodesic lift calculation and an exact density cancellation, not from simulation. The included `verify_marked.py` independently samples endpoints in the original quotient rectangle, compares the exact crossing event and horizontal displacement conditional survival against five aspect ratios and three thresholds, checks density normalization and monotone-likelihood-ratio values, and checks both scaling limits. The executable script is part of this artifact package and can be rerun using the standard Python 3 library.

The geometric distribution is exact for every positive width and glide length under normalized area sampling. The usual measure-zero cut-locus/tie endpoints are excluded. Only self-review has been performed. Historical priority and independent validation remain open.
