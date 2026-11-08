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
# Reproducibility

Run `python3 check.py` in the same directory as the complete text of `RESULT.md`. Only the Python 3 standard library is needed. Expected output begins with `PASS:` and reports 44 additional admissible parameter triples.

The checker uses two distinct calculations: direct rational evaluation of rooted diversity for every size-specific selected-leaf subset and symbolic coefficients of variance from affine edge-length vectors. Both compare to the exact claimed quadratic polynomials and to the rational witness \((\alpha,\beta,\gamma)=(14/15,1/3,2/5)\). The exact gaps are \(67/4500\) and \(19/4500\); no floating-point tolerance is used. The impossibility for fewer than five taxa is the separate general argument in the proof, not a finite computational assumption. Verification is an internal self-review, not an independent audit.
