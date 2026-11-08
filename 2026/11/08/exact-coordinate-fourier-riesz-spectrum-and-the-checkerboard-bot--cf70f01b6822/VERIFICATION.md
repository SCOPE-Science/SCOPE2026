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

# Reproducible checks

Run `python checks/verify.py` with Python 3 and NumPy. The checker directly enumerates the affine Segre cones over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) and \(\mathbb F_5\), evaluates all nontrivial coordinate characters pointwise and forms the full complex Gram matrix from scratch, then compares all eigenvalues and multiplicities with the formula, and tests the exact checkerboard eigenvector. For \(\mathbb F_4\), the field is represented by \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) and a field-trace additive character. All tests passed.

The observed smallest eigenvalues are respectively \(1/7\), \(3/43\), \(4/94\), and \(5/173\). The maximum eigenvalue is the upper root of the two-dimensional block in the proof; the exact squared optimal condition number is the ratio of that root to the smallest eigenvalue.

Completion marker: `SEGRE_COORDINATE_FOURIER_RIESZ_PASS`.

The checker is finite corroboration; it is not an exhaustive test of every prime power. The symbolic character-sum, Hamming-cube diagonalization and strict shifted-determinant argument prove the universal result. Independent review and exhaustive historical-priority validation have not been performed.
