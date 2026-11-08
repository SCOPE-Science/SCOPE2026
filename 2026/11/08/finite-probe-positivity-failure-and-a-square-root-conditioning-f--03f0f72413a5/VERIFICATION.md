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

# Reproducibility and limitations

Run `python3 verify.py` using Python 3 standard libraries. The program checks exact fraction identities for the Schur correction and bulk variance, the projected two-node Lanczos inverse quadratic form, independent chi-square numerical probability comparisons, finite-probe asymptotic illustrations, and strictly positive tridiagonal perturbations. Its success marker is `VERIFY_OK`.

The exact finite-parameter distribution and the limiting probability are proved analytically in `RESULT.md`. Seeded numerical trials do not establish general-parameter or asymptotic results, and an unperformed independent audit is not substituted by any executable test.
