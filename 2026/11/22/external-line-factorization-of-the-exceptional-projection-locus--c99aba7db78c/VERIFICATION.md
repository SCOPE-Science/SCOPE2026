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

Run `python3 verify.py` from the extracted package. The standard-library script computes the augmented-Vandermonde polynomial in the direction variables, enumerates external conic lines over finite fields of orders 2, 3, 4, 5, 7 and 8, checks factorization up to scalar, and verifies all line-incidence multiplicities. These are exact computations over those finite fields, with no floating-point arithmetic.

The general proof relies instead on projective interpolation, specialization to a conic direction to show the determinant is nonzero, the characteristic-\(p\) identity \(h^{Q-1}(v)=1\) for each nonzero rational value of \(h(v)\), and the degree-exact count of external lines. The zeta function is obtained from a disjoint affine-product decomposition. The computation is not a proof for all prime powers, and no independent audit has been performed.
