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

# Reproducibility and verification

Run `python3 verification_check.py` from the directory containing that file, using the standard Python library. The check completes with `PASS 44893 exact rational identities and inequalities`. It validates exact Toeplitz inverse identities, matrix normalization, and rational quadratic inequalities for finitely many separate degree/order pairs.

The general proof is analytic, in RESULT.md. The Gram matrix is strictly positive by a shift-convolution Gram representation; the closed form inverse vector is established by a finite difference identity; Cauchy–Schwarz and its exact quadratic defect give sharpness and rigidity; Eneström–Kakeya and polynomial reciprocity establish zero location. The checker alone does not justify infinitely many parameter values or any historical originality assertion.

No independent mathematical audit has been performed.
