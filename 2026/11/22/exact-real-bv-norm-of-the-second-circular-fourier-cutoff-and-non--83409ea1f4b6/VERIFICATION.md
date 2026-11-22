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

Run `python3 checks/check_bv_fourier2.py` in the root of the delivered extracted files (Python 3 standard library only). The verification program checks exact algebra in \(\mathbb Q(\sqrt2)\), reconstructs the sharp critical angle and coefficient, independently integrates absolute differences of degree-two Dirichlet kernels with exact trigonometric primitives and explicit sign intervals, and stress-tests 120 random finite real zero-mass atomic derivative measures.

Expected terminal line:

`ALL_BV_FOURIER_SECOND_CUTOFF_CHECKS_PASS`

The exact algebra is finite, and the kernel integrations use floating-point arithmetic only as a redundant check of the analytically derived continuous formula. The general all-BV inequality is proved by the measure coupling argument in RESULT.md; the random samples do not certify it. This is not a machine-formalized proof or independent verification. The source historical-priority assessment also remains open to independent inspection.
