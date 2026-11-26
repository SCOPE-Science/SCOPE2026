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

For a generic slice each face is determined by its minimal simplex-face support, a mixed subset of j+2 vertices; the binomial formula includes the empty cases. Centering and normalizing Gaussian coordinates gives the exact threshold bar G + c_n s_n with c_n=√n t_n. For deterministic bounded c_n the centered empirical count over the random O_P(n^{-1/2}) threshold displacement has fluctuation o_P(√n): on the n^{-3/4} grid the union bound costs O(n^{1/4}) and each count variance is O(√n); between grid points monotonicity or the binomial cell bound controls the remainder. Expanding s_n and the normal tail gives the two orthogonal Gaussian score projections and variance p(1−p)−φ²(1+c²/2)>0. The central face deficit uses the exact even binomial polynomial: its z² coefficient for z=K−n/2 is n^j/(2^j j!)+O_j(n^{j−1}), and the half-integer correction divided by n^{j+1} vanishes. The common scalar CLT then gives (1); ordinary Taylor gives (3), and in (2) the linear derivative is 2^{1−j}φ(0)c_n/j!+o(c_n), while the O_P(n^{j+1}) error is negligible precisely because nt_n→∞. K/n tends to an interior fraction, making empty slices negligible. These are proof checks, not reliance on the frozen simulation.

## originality

FAIL

A distinct preceding record contains the same fixed-scaled Gaussian and microscopic noncentral rank-one laws with the identical constants and studentization correction. The stronger critical wording nt_n→h is obtained by that record's count CLT with a remainder o(n^{-1/2}) in its α_n. The intermediate regime is not expressly stated there, but its exact sign-count and face formulas plus the same local empirical increment estimate recentered at deterministic c_n immediately give it by Taylor expansion. The frozen paper presents covered material as new; neither a different Euclidean unit nor this routine interpolation supports a repaired original finding.

## value

FAIL

The paired laws are mathematically informative but already available. The distinct residual wording is the moving-centered intermediate formula, produced by immediate Taylor rescaling of the existing rank-one face polynomial and the same local count bound. There is no new finite invariant, obstruction, quantitative bound or other downstream mathematical content beyond that routine interpolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
