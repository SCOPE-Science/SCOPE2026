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

The proof checks the exceptional-fiber classification against Chen--Hu--Ma, Proposition 3.1, with the only positive-dimensional fiber \(\mathbf P^{n-k}\) over doubled cycles. It checks the dimension difference \(\dim Y-\dim G=n+\binom{k}{2}\) symbolically and applies the precise semismall inequality and projective semismall decomposition theorem to conclude the intersection-cohomology formulas.

An independent standard-library Python program, `verify.py`, reconstructs Gaussian polynomials recursively and checks dimension identities, nonnegative palindromic coefficients, cohomological top degrees, and the Euler characteristics for all tested admissible \((p,n)\) in the semismall range. It verifies the exact conic examples \((p,n)=(1,3),(1,4),(1,5)\). Output is `VERIFY_OK` if every test passes.

Computational tests support the polynomial arithmetic only. They cannot prove the geometric fiber classification, the decomposition theorem, historical priority, or the untested infinite parameter range. The proof establishes the latter mathematically. Independent audit: not performed.
