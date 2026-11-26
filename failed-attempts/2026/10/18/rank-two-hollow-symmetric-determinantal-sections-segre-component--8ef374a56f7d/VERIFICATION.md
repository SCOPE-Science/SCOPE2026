---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The all-minor scheme calculation is valid: after pivoting on a nonzero a_pq and dehomogenizing, invertible block elimination turns each Schur entry into a unit multiple of the corresponding pivot minor, and every three-minor vanishes modulo those entries. Eliminating off-pivot entries leaves disjoint relations s_i t_i=0 since 2 is invertible. This squarefree regular sequence proves reducedness, pure dimension n-2 and lci locally. A branch chooses one orientation of each remaining vertex relative to the pivot; the corresponding rank-one cross block is the indicated Segre, with distinct complete-bipartite support at its generic point. Zero rows are exactly pairs with both coordinates zero. At a geometric point each other pair contributes one smooth coordinate, so the displayed completed ring has z nodal factors. The displayed smooth-factor dimension is for geometric points, as in the residue-field base-change interpretation, not the local dimension at an arbitrary nonclosed scheme point before base change. Reduced row-w locus is the same section on n-1 vertices; its components have generically just one zero row, so no duplicates occur across choices of w. This works also at n=3, where fixed zero row leaves a projective point. Vandermonde gives each degree after summing Segre degrees, and normalization is the disjoint union of the normal components. Inspected verify.py, without executing it: the pivot determinant, support and finite GF(3) checks corroborate but do not prove the ideal equality or the general local statement. No affine-vertex or characteristic-two result is inferred.

## originality

FAIL

The earlier directly inspected 2026-10-13 result a58bda70a733 already proves the same scheme-level local and global claims over C, including normalization, singular support as the union of smaller hollow rank-two sections, and the degree of every Segre. Its actual proof of the ideal equality and squarefree charts uses only that the pivot and 2 are units. The generalization to characteristic not two requires no new argument. Enumerating and adding the degrees of the earlier described zero-row copies gives exactly the new advertised singular-support numbers. This is demonstrated coverage of the mathematical contribution, not a finding based on similar titles or missing sources.

## value

FAIL

The geometric classification itself is useful, but it is already available for this object with a field-independent proof. The remaining differences are recording the immediate ring-theoretic base-field generality and mechanically multiplying known degrees and counts by n. They do not constitute a distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
