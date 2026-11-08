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

Run `python3 check.py` in the same directory as the other files (Python 3.8+; standard library only). The checker constructs both literal nine-vertex incidence matrices, checks connectivity and individual degrees, computes every surviving-subset outcome exactly, checks an independent pair-union covariance formula, and enumerates all connected labeled bipartite graphs on up to eight vertices. The expected terminal line is `MINIMALITY_OK p+q <= 8; graphs 70479 degree_classes 352 variance_profiles 403`. Observed exact replay reached this line successfully. The finite census, formula and witness are all supplied; no inaccessible assets, external datasets or third-party software packages are required.

The proof of pair-union formula is mathematical, not substituted by code. The census is an exhaustive finite verification for the asserted cutoff, not evidence of unspecified behavior at larger sizes. Historical-priority claims are conditional on the inspected materials. Independent audit has not been performed.
