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

The original two-dimensional map was checked against the centered linear branch on 54 exact rational representative points. The independent standard-library script `check_exact.py` constructs the \(n\)-visit polygon from affine inequalities rather than the claimed closed form; over 94 rational ratios \(t\), including \(1/3\), \(3/4\) and \(2\), it checks exact areas, the two clip intersections, destination sum identities and affine inverse similarity for consecutive levels from three through twelve. Its successful terminal line is:

`THREE_CHANNEL_EXACT_RATIONAL_CHECK_OK cases=94 polygon_steps=9 original_branch_cases=54`

Run `python3 check_exact.py` from the extracted package directory. The analytic proof, including the explicit vertices, all boundary comparisons and infinite-step inverse induction, establishes the theorem. The finite checker is reproducibility support only; no independent audit, exhaustive numerical proof or external certification is represented.
