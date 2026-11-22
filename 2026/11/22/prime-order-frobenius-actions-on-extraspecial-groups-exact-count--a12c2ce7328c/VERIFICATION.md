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

# Verification and reproducibility

`check_prime_cyclotomic.py` is a standalone Python 3 standard-library checker. Run `python3 check_prime_cyclotomic.py`. Expected terminal marker: `PRIME_CYCLOTOMIC_EXTRASPECIAL_CHECKS_OK`.

Its quotient-matrix loop exhausts all \(2\times2\) matrices over five selected prime fields and imposes the exact order, multiplier and eigenvalue tests. At \((p,\ell)=(5,3),(7,3),(11,5),(13,3),(29,7)\), the observed admissible matrix counts are \(0,2,532,2,10446\), and the predicted automorphism counts are \(0,98,64372,338,8785086\). It also checks all \(98\) automorphisms on all \(7^3\) elements at \((7,3)\), plus \(16\) selected automorphisms on all \(11^3\) elements at \((11,5)\), verifying fixed points, order and the noncommutative ordered product law. Finally it verifies the elementary eigenindex involution for several prime orders. These checks do not constitute exhaustive calculations at higher symplectic rank. The parameter-uniform group-theoretic proof is in RESULT.md.

The correctness, priority and value assessment is a self-review of the stated claim only. The independent audit is not performed, and no externally certified theorem proof is claimed. Key historical risk: a pre-existing calculation in specialist similitude conjugacy literature may give an equivalent formula.
