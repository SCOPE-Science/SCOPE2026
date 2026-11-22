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

# Computational verification

Run `python3 verification/check_fourcut.py` with Python 3.10 or newer. No optional packages are used. The attached `verification/collapse_pairs.tsv` records the complete finite elementary-collapse certificate as decimal twelve-bit masks. The checker builds all graph and complex data from first principles, checks all 132 free-face pairs including uniqueness of each proper coface in the **current** complex, and verifies the residual two-dimensional complex. It also computes separate exact mod-two matrix ranks for both complexes.

Execution from the actual packaged files completed successfully with the output in `verification/check_output.txt`: 369 disconnected induced four-sets, 449 dual faces, 3,647 cut-complex faces (including empty faces), 132 collapses, residual dual vector (12,60,112), and boundary ranks 306, 462, 49 and 11. Integer face counts and Euler characteristics are checked. The claim's integral and homotopy conclusions require the topological arguments in `RESULT.md`; the mod-two computations alone are not integral certificates.

Verification is limited to the finite object in the theorem. This is not independent external validation, and no external certification is asserted.
