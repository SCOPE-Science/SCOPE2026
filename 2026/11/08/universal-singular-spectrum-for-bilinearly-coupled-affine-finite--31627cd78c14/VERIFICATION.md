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

The theorem follows for every odd prime power from the explicit affine permutation and the exact slope-block decomposition in `RESULT.md`. The identity \(B_+-B_-=qww^{\mathsf T}\) and the two characteristic polynomials verify the boundary values. To reproduce finite corroboration, run `python3 CHECK.py` in this directory; no third-party modules or downloaded data are required. The checker directly enumerates rows and columns over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\), checks all column intersections, exact integer matrix annihilators, spectral power sums and affine normalization. It prints a `CHECK_OK` line on success.

These finite checks are not a proof for every field and do not constitute independent verification. They test the critical concrete formulas, while the proof establishes the quantified theorem. The mathematical claims concern the complete ordered-parameter operator only; no rank stability for partial samples or characteristic two is asserted.
