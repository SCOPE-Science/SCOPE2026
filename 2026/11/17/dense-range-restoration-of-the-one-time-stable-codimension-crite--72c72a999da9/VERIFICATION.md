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
The full proof is analytic and relies only on the primary theorem expressly cited in RESULT.md plus the independently derived stable-codimension lemma. At time zero the cocycle yields \(\mathcal S(0)=T(s,0)^{-1}\mathcal S(s)\). From the uniform noncritical inequality and bounded growth, the supremum of any bounded future orbit is controlled by a constant times its initial norm, so \(\mathcal S(s)\) is closed. The finite-dimensional complement image is disjoint from \(\mathcal S(s)\) and its sum is closed and dense, therefore the sum is the whole Banach space. This proves stable quotient dimensions at all positive times. Theorem 3 of arXiv:2611.08451v2 supplies the remaining dichotomy equivalence.

The diagonal example is exactly compositional, densely ranged at positive times because finite sequences are in its range, and non-surjective because the test sequence \((q^{n/2})_{n\ge1}\) is square summable while its formal inverse is not. The stable space and invariant splitting are evident from the multiplier formula. No finite experiments or automated theorem certification are used. Historical uniqueness is not asserted.
