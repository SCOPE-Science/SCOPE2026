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

# Verification procedures and limits

Run `python projective_profile_check.py` with Python 3.9 or later. The script constructs projective points by normalizing nonzero vectors and tests triple collinearity through a nonzero two-by-two minor. It independently enumerates extension patterns from representative tuples of zero to three stationary points in eight prime-field geometries, and tests intersecting versus skew lines in projective dimension two versus dimension at least three.

The expected successful last line is:

`PASS: eight projective geometries, all five stationary classes, F04 profiles, skew-line boundary`

The source proof handles every projective dimension and all prime-power orders; the program deliberately only checks prime fields with orders two, three, and five. Projective non-Desarguesian planes are covered by the projective-plane counting identities, not enumerated. The computation does not constitute an independent mathematical review or a proof that there is no equivalent published theorem.
