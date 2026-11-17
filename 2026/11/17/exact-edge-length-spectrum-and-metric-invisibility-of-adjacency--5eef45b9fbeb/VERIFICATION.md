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

The exact integer checker `verification/check_edge_spectrum.py` was executed from the enclosing package directory with Python. It independently counted all unordered pairs of derangement permutation matrices for dimensions 3 through 7, compared the resulting single-cycle adjacency length classes against the rook-polynomial formula, and independently verified the cyclic matching coefficients up to cycle half-length 6. Its success marker was `DERANGEMENT_EDGE_SPECTRUM_PASS n=3..7; cycle_rooks k=2..6`.

The all-dimension equality is established by the forbidden-board inclusion–exclusion proof in RESULT.md. Infinite-dimensional Poisson limits and total-variation convergence are established analytically using fixed factorial moments, a summable upper bound, and countable-state truncation. The checker is a finite diagnostic, not an independent certification of these infinite claims.
