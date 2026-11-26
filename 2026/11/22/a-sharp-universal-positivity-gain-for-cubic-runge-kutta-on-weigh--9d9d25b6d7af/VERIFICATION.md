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

Expanding L=D−W noncommutatively, bipartite parity eliminates unit- and three-edge terms for distinct same-class vertices. Exactly the shared-neighbor pairs contribute h²m_ij/2−h³c_ij/6, giving their one permanent crossing. Across classes, a distance-three entry is h³(W³)_ij/6; for an edge, division by hw_ij gives an upward quadratic with discriminant at most −(5d_i²+2d_i d_j+5d_j²)/12. More distant entries vanish. The stated diagonal follows since (W³)_ii=0. Every diagonal is a nonnegative spectral mixture of the cubic scalar Taylor multiplier; its derivative is strictly negative since λ>0 contributes −λ[(hλ−1)²+1]/2 and L_ii>0 ensures positive spectral weight there. It tends to minus infinity. Thus the minimum root is exact, included, and cannot be followed by a later positive interval. For F=I−hL, (I/3+F/2+F³/6) proves the lower bound and C4 has a distance-two cutoff 1/Δ. At a maximum-degree vertex, the diagonal at z=hΔ=α is the sum of (σ_i/Δ²)α²(3−2α)/6 and −(τ_i/Δ³)α³/6, strictly negative since α>3/2. For the m-leaf star at fixed z<α, the hub diagonal tends to the positive scalar cubic there, the common leaf diagonal tends to 1, and normalized distance-two thresholds tend to 3. Hence eventually the step z/m is allowed, proving liminf m h_*≥α; the strict upper bound gives the limit. Row sums equal one since L1=0. Source matrix-check code and reported finite tallies were inspected; they were not executed or used as uniform proof.

## originality

PASS

Credit the standard forward-Euler/SSP lower bound, general polynomial tests, and all identified exact family overlaps. The supported distinct content is the all-step graph-distance/diagonal formula and strict sharp upper bound on the whole arbitrary weighted bipartite class. The star value and limit are not independent new results; the same-day star theorem gives them explicitly, and its date does not resolve priority.

## value

PASS

A local lift of a generic root test to incident degrees and shared-neighbor moments makes the largest stochastic completed step identifiable without a global matrix search, including whether a distance-two pair or a diagonal controls it. The result proves that searching beyond the first failure cannot help and gives a sharp worst-case range relative to standard forward Euler. Both effects matter for interpretation of positivity limits and are not just recalculations of known stars or regular graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
