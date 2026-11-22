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

# Reproduction and proof boundaries

Run `python3 verify.py` with Python 3 and the standard library. The program checks the exact three-state matrix inverse and its nine local disjointness decisions using a four-subatom Boolean refinement. For each of the four parameter values \(m\in\{1,2,3,4\}\), it constructs the matrix directly from the permitted type words, then computes its determinant using integer fraction-free Bareiss elimination. It verifies the respective dimensions \(1,5,19,65\) and exact determinants \(1,1,-1,1\), ending with `ALL_EXACT_CHECKS_PASS`.

The all-size determinant uses the ordinary Jacobi complementary principal-minor identity and the primitive permutation submatrix of \((B^{-1})^{\otimes m}\). The full inertia uses tensor-product eigenvalue signs plus the real symmetric Schur-complement identity. These steps are proven in RESULT.md rather than inferred from finite experiments. All countable homogeneity assertions follow from the finite Boolean-subalgebra back-and-forth argument. This package contains no independent audit or external mathematical certification.
