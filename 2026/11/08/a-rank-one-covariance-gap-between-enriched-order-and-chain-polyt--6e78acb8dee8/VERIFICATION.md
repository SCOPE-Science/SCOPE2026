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

Install the packages listed in `verification/requirements.txt` and execute `python verification/verify.py` at the package root. The script uses convex-hull facets only as a triangulation scaffold; all actual simplex volumes and first and second moments are evaluated by exact integer determinants and rational arithmetic. For eight parameter pairs, both direct polytope moment tensors agree with the all-parameter formula, and all volumes agree exactly. The pairs are \((1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2)\). The code also checks \(22{,}500\) exact rational parameter ratios, strict bounds, reversal identities, and one near-sharp example. Expected final markers are `EXACT_INTEGER_FAN_TRIANGULATION_CHECKS_PASSED` and `COVARIANCE_RANK_ONE_AND_SHARP_RATIO_CHECKS_PASSED`.

The finite hull stage uses floating point to select faces, and the exact arithmetic then integrates the resulting integer simplices. This is independent finite corroboration of the integral argument, not a proof for untested dimensions or a computer-generated certification of generality. The all-dimensional argument is in `RESULT.md`. Historical priority has been checked against the cited original enriched-poset papers and closest public mathematical records, but cannot be guaranteed by finite searches.
