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

The analytic proof constructs all factorizations on arbitrary torsion abelian group algebras. To corroborate the exact finite-algebra identities, run `python check_exact.py` with Python 3.10 or later from the directory containing this file and `check_exact.py`. The exact-rational test returns `FINITE_SUPPORT_LOCAL_OPENNESS_EXACT_OK 2367`. Its assertions check finite Fourier idempotents, convolution products, algebraic correction formulas, coefficient-norm bounds and corner inverses for Boolean groups with up to 32 elements. It does not enumerate infinite groups, establish original priority or replace the infinite-dimensional algebraic proof.

Self-review was performed on the explicit definitions, corner-unit density argument, every factorization and upper/lower aperture bounds. An independent audit has not been performed.
