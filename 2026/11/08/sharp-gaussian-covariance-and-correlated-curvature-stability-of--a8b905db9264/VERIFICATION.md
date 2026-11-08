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

With Python 3 standard library, execute `python3 check.py` from the directory containing that file. The recorded `check_output.txt` reports 427 passed assertions, including exact rational covariance-map identities for constant-diagonal matrices, exact rational anisotropic moment fixed points, checks of the strict sharp gain and boundary witness, and numerical evaluations for the global envelope. The checker is self-contained and has no external files or network dependencies.

The proof in `RESULT.md` is analytic: the universal covariance law and high-step divergence follow from the exact energy drift, while the sharp two-coordinate threshold follows from the positive-cone self-adjoint covariance operator and the two-by-two Sylvester reduction. Finite checks cannot establish these universal assertions and are provided only to detect implementation and algebra errors. The source-based novelty comparison has historical-coverage risk; no independent validation is represented by this document.
