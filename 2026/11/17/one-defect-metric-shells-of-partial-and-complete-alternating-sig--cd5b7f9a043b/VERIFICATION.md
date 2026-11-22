---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For a partial alternating-sign matrix with unique -1 at (r,c), each row/column containing it has 1 or 2 positive arms. Frobenius squared distance lower bound δ²(1+(a-1)/2+(b-1)/2) with δ=Y_rc+1>=1 follows from saturation and Cauchy-Schwarz; the displayed zero-center and half-arm point attains (a+b)/2. Complete ASMs with one -1 are row/column-permutation equivalent to the 3x3 cross D⊕I_(n-3). Direct exact KKT potential h verifies X_ij=(A_ij-h_i-h_j)_+, nonnegative doubly stochastic rows/columns, unique nearest projection and squared distance 2+2/(n+5); choose 3 rows, 3 columns and remaining permutation to count C(n,3)^2(n-3)!. Independently built rational matrices n=3..35 and verified every row/column constraint, every complementarity entry and exact distances.

## originality

PASS

Heuer–Striker studies partial-ASM and matching-polytope structures, and Striker studies the ASM polytope; neither compared statement provides the all-order explicit nearest-point one-defect Frobenius shells. General nonnegative bistochastic projection algorithms are broader computational frameworks, not an existing fixed closed-form shell formula. Resultary nearest inradius/diameter and other Birkhoff projection families concern distinct points/metrics. Best of knowledge with older matrix-nearness residual risk.

## value

PASS

Three partial exact distance shells and an all-order exact complete-matrix projection exhibit how global row/column conservation delocalizes a single alternating-sign defect by 2/(n+5). These are interpretable, natural quantitative invariants of standard ASM and Birkhoff polytopes, with unique projections and full family counts, not a routine restatement of polytope definitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
