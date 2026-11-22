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

Execute `python3 verify.py` using Python 3 and the standard library. The program runs two independent exact calculations on all 4096 masks: a flat-incidence formula and determinants over the rational quadratic field defined by zeta^2+zeta+1=0. It asserts their identity for every subset, checks exactly 58 lines and 43 planes on the full configuration, identifies the five negative-defect subsets, verifies four planar six-point exceptions, and checks that each of twelve single deletions has defect 6. These checks were executed against the script included in this package; a subsequent extraction replay must confirm packaging integrity.

The enumeration is finite and exhaustive for the specified twelve-point configuration. It is not a statistical sample or a proof of any global minimality statement. Independent validation has not been performed.
