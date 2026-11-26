---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently checked the all-data iff theorem. Strict convexity and coercivity give a unique continuous fit. With the oriented penalty signs in the source the stationarity equations are m_j(u_j−y_j)+λ(q_{j−1}−q_j)=0. Sum over a proper fused block and then over its initial segment: its common fitted value is its data mass mean plus λ times (q_R−q_L)/M, and each interior flux is a mass-weighted convex average of q_L,q_R plus a fixed reciprocal-λ term. At any positive λ₀ take feasible initial fluxes; holding signs of nonzero exterior edges for a short right interval gives a feasible continuation by interpolation between the initial flux and that average. Equal penalties make every average feasible; on a proper two-site triangle block the two exterior signs are opposite, giving exactly the stated three inequalities, including equality. The initial λ=0 case works since every equal-data block has zero reciprocal-λ numerator, and a fully fused fit persists by scaling all fluxes by λ₀/λ (or constant data with zero flux at λ₀=0). Continuity and local right continuation at any finite putative first loss rule out loss even for simultaneous boundary events. Conversely choose a minimal edge adjacent to a larger one on n≥4; four distinct sites allow both exterior signs positive, forcing a strict average A>a_i. On a triangle a violated absolute-value bound gives a realizable opposite sign choice with the same strict inequality. Invert the KKT equations at λ=1 with internal flux −a_i and large prescribed exterior gaps. The uniform bound |u_j−y_j|≤λ(a_{j−1}+a_j)/m_j lets the gaps be chosen to keep actual exterior signs fixed to just beyond λ*=(A+a_i)/(A−a_i). Candidate fused flux A−(A+a_i)/λ is feasible on [1,λ*] but impossible beyond λ*, proving a positive-interval fusion followed by separation. The resulting proof applies to any positive masses and positive edge weights in the stated cycle regime. Direct substitution checked the displayed exact witnesses and stable nonconstant triangle; the independent conclusion does not use or rerun the frozen sample checker, whose 16 explicit KKT checks and finite obstruction tests were inspected.

## originality

PASS

The credited dual and graph-path techniques and known no-split sufficient settings do not cover the exact necessity for arbitrary positive masses on cycles of length at least four, or the strictly larger admissible triangle region. The closest distinct same-day statements involve paths and stars and were compared as mathematics, not ordered by date.

## value

PASS

This is the complete all-data decision boundary for using irrevocable fusions in a natural segmentation objective on a ring. The classification says that fidelity masses cannot rescue any nonconstant weighting at length four or greater, but explains exactly how a shared third vertex permits it on the triangle. Constructive witnesses show genuine separation after an interval of fusion, not mere failures of a sufficient condition or isolated numerical coincidences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
