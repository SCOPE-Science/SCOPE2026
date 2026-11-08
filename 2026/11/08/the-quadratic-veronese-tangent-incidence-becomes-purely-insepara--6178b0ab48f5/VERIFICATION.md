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

# Verification notes

Execute `python3 verify.py` with SymPy. The attached output `verify.out` was produced from the packaged source on the same run and ends `ALL_CHECKS_PASSED`.

The executable verifies the tangent parametrization symbolically over the integers, the exact polynomial remainder, the rational nonsquare-class identity, the Chern/Segre degree, and exact finite-field point incidence for \(\mathbb F_2,\mathbb F_3,\mathbb F_5\). These computations corroborate the field-theoretic proof; checking finitely many fields is not a proof for arbitrary fields. The valuation and derivative arguments are mathematical, not finite computations.

The generic separability claim does not classify special fibers, ramification or all positive-characteristic analogues. Historical priority remains provisional. Independent validation is not performed.
