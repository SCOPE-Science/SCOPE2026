---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The reduced product-conductance Laplacian gives the claimed enumerator: deleting a B vertex, its Schur complement is X diag(y')−(X/Y)y'y'^T, with rank-one determinant factor y_deleted/Y. This proves the independent class multinomials. The unit-current equations give V_i−V_j=1/(x_iY)+1/(y_jX)−1/(XY); inserting half weights on both marked endpoints gives exactly r. The joint conditional orientation probability doubles only for a shared edge, while the same vertex cannot realize both events. This yields both diagonal terms, including the repeated-vertex subtraction, and the positive off-diagonal. For a=b=m the smaller magnitude eigenvalue is negative because (1−t)^(m−1)<1−t for m≥3, and equals zero for m=2. For fixed a, C_BB=−b/4+O(1), C_AA=O(c_A²), and C_AB/(bc_A) approaches a/[4(2a−1)]; normalizing gives exactly the negative determinant limit. Independently enumerating connected (a+b−1)-edge sets and all orientations for K_2,2, K_2,4 and K_3,3 gave 32, 1024 and 2592 outcomes; K_2,4 gave entries (−473/4096,81/256,−13/16) and witness 191/4096. This is a finite corroboration, not the proof. No assertion about uniqueness of an imbalance threshold is needed.

## originality

PASS

Qualified originality of the class-indexed matrix and change of inertia, not of the underlying weighted tree machinery. Neither a fixed-tree scalar bound nor an edge-incidence spectrum evaluates the degree-tilted edge excess and its competition with within-class anticorrelation.

## value

PASS

The inertia asks whether the same deterministic class weighting can turn source–sink anticorrelation into positive covariance. Entry signs alone cannot answer that question. The balanced proof, fixed-side reversal and small exact witness resolve this interpretation beyond a single numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
