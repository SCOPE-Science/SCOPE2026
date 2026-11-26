---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A prescribed-size coloring induces the edge vector of a disjoint union of cliques of sizes r_a, uniformly relabeled. With B the unsigned incidence of K_N, BBᵀ=(N−2)I+J and the orthogonal pair modules are constants, Bᵀ of centered vertex vectors, and ker B, of dimensions 1, N−1 and N(N−3)/2. To check scalar action directly, covariance depends only on equal, incident or disjoint edge pairs; their matrices are spanned by I, BᵀB and the all-ones matrix. The total pair sum is deterministic. Each row of the co-color pair array has random degree r_color−1 with variance s², and the row covariance off diagonal is −s²/(N−1) because the sum of rows is fixed. Dividing the centered row eigenvalue by N−2 recovers the star eigenvalue. The pairwise variance p(1−p) fixes the trace and hence the cycle eigenvalue, including N=4. Centering degrees by 2W/N and using the incidence identity gives the stated star projection norm; subtracting both the constant and star norms gives the residual norm and hence the variance formula. For a binary additive edge vector a_i+a_j, unequal coefficients a_i>a_j differ by one, since comparison to any third vertex gives a positive difference of bits. All other coefficients then equal −a_j. As N≥4 their mutual bit is 0 or 1, giving a star or co-star; equal coefficients give a constant graph. Of those graphs only the empty, complete and co-star are unions of cliques. The star mode vanishes exactly when the clique degrees are all equal. The two null modes therefore yield exactly the four stated graph cases. In the one-singleton case the statistic is m−d_H(J) for a uniform singleton J, independently confirming the regular-graph condition. The frozen checks were inspected, not executed; N=4–8 checks range over histogram multisets, and for all graphs at N=4,5 the classifications are compared to the formula, with direct coloring tests for a subset of cases. They are finite corroboration, not a substitute for the proof.

## originality

FAIL

No inspected catalogue hit states the full prescribed-size theorem verbatim. Nevertheless, both parts are mechanically covered: Schur orthogonality for the standard three pair modules gives the complete variance decomposition for an arbitrary uniformly relabeled edge vector, and the known classification of Boolean degree-one functions on J(N,2) gives exactly the binary additive graphs used to determine the null modes. Specialization to a disjoint union of cliques requires only its deterministic degree multiset and the fact that a star on N≥4 is not a union of cliques. The failure is by explicit mathematical implication, not by the inaccessible equal-block citation or by a near title match.

## value

FAIL

A zero-variance diagnostic for fixed-histogram permutation tests is naturally motivated and the presentation is useful. The exact diagnostic in this record, however, is obtained by two standard pair-mode norms and direct use of the known Boolean degree-one classification; the cluster restriction only deletes the star and identifies regularity with equal class sizes. There is no remaining unknown invariant or further structural case requiring a new argument, and no distinct extension is supplied to repair the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
