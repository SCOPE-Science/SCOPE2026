---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The actual graph Laplacian is L_H⊗e0e0^T+I⊗Q, Q a positive weighted path Jacobi matrix. Each Q+theta e0e0^T has simple spectrum; strict interlacing with the common root-deleted principal submatrix separates ordered eigenbranches uniformly across theta. The endpoint coordinates of every eigenvector are nonzero by Jacobi recurrence; Hellmann–Feynman derivative |u_0|^2>0 separates distinct base theta within a branch. Therefore every eigenspace of the product is E_theta⊗span(u_j) and its endpoint-observation rank equals rank(E_theta->R^J). Summing exact symmetric-matrix PBH/Kalman eigenspace ranks yields multiplication by ell+1. Independent exact-rational Kalman ranks agreed in 128 combinations of positive edge weights, ell=1,2, n=2,3 and mixed root/tip index subsets; K2 with unit length-two fiber middle-node input has rank 5 versus 6 at either endpoint. This does not claim actuator energy or conditioning.

## originality

PASS

Hsu 2018 Theorem 3.4 provides the full controllability equivalence for a single root input in a special composite graph. The published 2026-11-01 weighted cyclic-comb theorem gives a similar Jacobi-branch argument and exact leaf ranks for a C_n base. Neither statement covers the exact arbitrary positive weighted base-graph rank formula for all multi-input mixed root/tip sets. The latter source is genuinely overlapping and credited; the general lift is the surviving scope.

## value

PASS

Exact controllability-rank transfer across arbitrary weighted base graphs is a natural structural invariance for rooted products; it reduces all endpoint placement questions to the base graph despite fiber weight heterogeneity and base spectral multiplicity. The sharp interior-node counterexample marks an operationally meaningful boundary. It is not merely a one-vertex case or a base-path specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
