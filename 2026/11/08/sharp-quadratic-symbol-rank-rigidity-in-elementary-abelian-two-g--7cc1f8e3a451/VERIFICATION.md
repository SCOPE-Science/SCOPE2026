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

# Verification and reproducibility

The mathematical proof is contained in `RESULT.md`. Run the Python 3 standard-library script with `python3 verify.py` from a directory containing this package. The script builds multiplication matrices in the squarefree monomial basis and calculates their ranks by finite-field row elimination; it does not take the homological rank formula as an oracle for the counted ranks.

The exhaustive binary four-generator census independently evaluates all 2048 augmentation-square elements and returns counts 1, 1, 30, 1120, 896 at ranks 0, 1, 2, 4, 6. The independent quadratic-symbol census enumerates all 4096 degree-two forms over the four-element field and returns 1, 1071, 3024 at alternating matrix ranks 0, 2, 4. Deterministic finite-field checks test the claimed rigidity with arbitrary sampled higher-degree coefficients at generator counts three to six, and the explicit sharpness examples at counts up to nine. The current package's verifier completed successfully with `VERIFY_OK`.

These computations verify the stated finite instances and provide regression checks. They do not prove the universal claims for arbitrary fields, all dimensions or all perturbations. Universal correctness instead relies on the explicit tensor-product homology, degree-filtered elimination lemma, and alternating-form orbit count in `RESULT.md`. The complete higher-nullity lift-rank distribution remains unproved and is not claimed here. Publication priority and independent mathematical validation remain outstanding.
