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

The exact theorem and global proof are in `RESULT.md`. Run `python3 CHECK.py` (Python standard library) to reproduce the scalar-root approximations, the eleven representative order checks, all three signed weighted contacts, and coefficient perturbation tests. The explicit printed fifth-order norm and kernel values match the algebraic formulas.

The code checks 2,001 grid points per tested order and six nearby parameter perturbations. These finite tests are supplementary; the monotone root and affine three-contact arguments in the proof establish the all-order claim without finite enumeration. There is no independent mathematical audit or separate formal certificate.
