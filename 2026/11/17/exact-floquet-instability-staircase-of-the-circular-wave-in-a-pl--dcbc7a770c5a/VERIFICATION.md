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

Run `python3 verify.py` in the directory containing this document. The standalone script implements the entire characteristic determinant and its derivative using the Python standard library, verifies the predicted roots, checks the analytic transversality coefficient, and continues critical characteristic roots by Newton iteration on both sides of three thresholds for four positive rotation parameters.

Executed result:

`VERIFY_OK axis_substitutions=12 crossing_derivatives=12 root_continuations=24`

The proof of the universal statement is mathematical rather than computational. The verification script samples only finitely many angles and thresholds; it does not enumerate all characteristic roots. The infinity exclusion, zero-root simplicity, exact imaginary-crossing equation and root-count argument are supplied in `RESULT.md`. Independent audit has not been performed.
