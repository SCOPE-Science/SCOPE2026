---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The endpoint reflection gives cyclic Jacobi blocks; their first-coordinate Krylov determinants are independent of w because the subdiagonals are fixed. The direct-sum Krylov determinant differs from their monic cross-resultant by a nonzero constant. The Fourier modes split into a shared pair for each nonzero double eigenvalue, with only the symmetric zero mode unshared in the symmetric block; the even-order alternating mode is antisymmetric. Varying w changes the first antisymmetric diagonal by 2(w−1). The trailing minor does not vanish at a shared eigenvalue, so each contributes one linear factor. The continuant at zero gives det A(w) = 1+(n−1)w in odd order and twice that in even order, including the smallest orders. The open-path triangular Krylov determinant determines the sign; polynomial identity on the real line also gives the complex extension. The rank at w=1 counts the distinct eigenvalues with nonzero endpoint projections. For fixed n the r vanishing singular values are each O(|w−1|); the exact determinant order r and the nonvanishing other singular values force matching lower bounds on each. The smallest real Gramian eigenvalue is its squared singular value. The uploaded checker was inspected, not executed; its finite reported tests are not the basis for the all-n result.

## originality

FAIL

A distinct indexed Resultary record already states the exact signed endpoint Kalman determinant with the same graph, vertex ordering, input and positive Laplacian powers, the same real roots and the same squared Krylov-Gramian determinant. Its real polynomial identity extends identically to complex w. The fixed-order least-singular-value and Gramian scaling are elementary consequences of that determinant, the standard uniform-cycle rank, and singular-value perturbation. This is demonstrated scientific overlap, not a conclusion about authorship or inferred priority from a catalogue date.

## value

FAIL

The explicit endpoint determinant would be useful if unknown, but is already stated for the same family. Beyond that overlap the fixed-n scaling and complex extension are routine deductions, not a different independently useful invariant. No sharp coefficient, uniform-in-size conditioning law or separate surviving result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
