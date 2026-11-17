---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For connected conductance allocation, each R_ij is convex by its variational supremum, so averaging over matching-pair permutations and bipartition swap produces an unrestricted global minimizer with matching conductance x and nonmatching y. The Laplacian decomposes into eigenvalues my, z=2x+(m−2)y (each multiplicity m−1), and 2d=2(x+(m−1)y), giving R_same=1/(my)+1/z, R_match=2(m−1)/(mz)+1/(md), R_nonmatch=1/(my)+(m−2)/(mz)+1/(md). R_same−R_nonmatch=y/(zd)>0. Set t=x/y, budget y=B/[m(Pt+m−1)]; the two piecewise smooth scalar objectives meet at gamma=(sqrt(m(m−2))−(m−2))/2. Differentiation and one-crossing monotonicity yield price thresholds P1,P2,P3 and 4 branches; P3−P2=1/(2m²)+O(m^−3). Independent rational grounded-Laplacian tests and scalar numerical minimizers corroborated nontrivial parameter cases. Unrestricted asymmetric optimality follows from convex averaging, not unsupported uniqueness.

## originality

PASS

PASS for maximum pair resistance (diameter) under a matching-price budget on K_m,m, not the preexisting total-resistance/Kirchhoff-index matching-price problem. Ghosh–Boyd–Saberi explicitly proposed generic convex minimax effective-resistance design in 2006, but neither that work nor the inspected 2026 matching-priced Kirchhoff-index solution determines these four closed phases, crossover or narrow width. Same objective on a priced complete graph is a distinct edge topology.

## value

PASS

Exact network-design support transition and active-pair switch for a natural symmetric priced bipartite family; shows the optimal maximum resistance removes matching edges in a narrow price regime not predicted by spectral-gap or total-resistance objectives. The m^{-2} phase width adds meaningful asymptotic structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
