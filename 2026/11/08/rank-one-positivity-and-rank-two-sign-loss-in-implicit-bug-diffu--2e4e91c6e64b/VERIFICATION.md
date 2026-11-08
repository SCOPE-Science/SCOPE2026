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

# Exact arithmetic verification

Execute `python3 verify.py` alongside this document. The script uses only Python's standard `fractions` module and elementary matrix operations. It solves each projected BUG equation by exact Gaussian elimination, checks the equations by exact substitution, and reconstructs the three-by-three output without using square roots or a floating-point QR factorization. The independent orthogonal-basis formulation is equivalent by invariance of Galerkin subspaces.

The original matrix \(W\) is entrywise nonnegative and has rank exactly two. The symmetric generator matrices have connected positive-weight path graphs and zero row sums. The exact output has
\[
-\frac9{100}<(W_+)_{33}<-\frac8{100}.
\]
The script also solves full backward Euler on the same nine degrees of freedom and verifies that each output entry is strictly positive. Twenty-four exact rank-one calculations corroborate the universal analytic statement.

The rank-one theorem is independently proved using positivity of irreducible graph resolvents and positivity of the scalar Galerkin coefficient. The finite rank-two claim is proved by its fully specified rational counterexample; the script's fraction comparisons are exhaustive for those specified finite matrices. No statement about all rank-two inputs, arbitrary high-order mass matrices, or an independently certified mathematical review follows from these computations.
