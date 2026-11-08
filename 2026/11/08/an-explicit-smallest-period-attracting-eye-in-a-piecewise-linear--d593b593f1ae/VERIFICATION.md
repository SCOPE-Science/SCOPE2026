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

The proof uses exact affine return equations, strict elementary polynomial sign inequalities, and a reflection identity. The accompanying `check.py` was executed from this package and reported `VERIFY_OK`; it checks the cycle relations, factorized window width, root uniqueness, endpoint identities, reflection, a rational interior sample, and high-precision quadrature of an analytically exact integral.

Computational sign tests and finite rational examples do not alone prove universal dynamical claims; the universal conclusions rest on the explicit algebra and monotonicity inequalities in `RESULT.md`. No independent external audit or complete numerical classification of other parameter components has been performed.
