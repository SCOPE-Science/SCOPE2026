---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 gopel_verify.py` with Python 3.10 or newer. Compare the script's `fixed-node-profile` entries with the rational-node polynomials in `RESULT.md`. It checks all 720 label permutations and the equality of the affine-isotropic tetrad set with the set defined by trope incidence within the classical finite model. Its auxiliary unweighted orbit spectra recover previously tabulated quantities. The geometric reduction and fixed-mark argument in `RESULT.md` explain why the checks apply in any odd characteristic and why the table works after any finite extension.
