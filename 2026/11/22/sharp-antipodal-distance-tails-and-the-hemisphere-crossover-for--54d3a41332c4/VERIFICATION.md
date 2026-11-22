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

# Verification performed

The executable `verification/check_lune.py` was run using Python 3 from the extracted research package and printed `LUNE_ANTIPODAL_TAIL_CHECKS_OK 20`. Its 20 checks include independently evaluated one-dimensional versions of the four-dimensional tangent-cone volume, the two exact special-case values, finite-\(\varepsilon\) spherical-dot-product cubatures for three fixed lunes and four hemisphere-window openings, a far-window matching test, and a numerical monotonicity consistency check.

The equations in `RESULT.md` contain the analytical proof. The finite, deterministic computations neither certify the limiting quantifiers nor establish priority over all previous literature. An independent mathematical audit has not been performed.
