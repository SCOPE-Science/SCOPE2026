---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an inverse step y=g_a(x), the defining identity gives y^(−α)−x^(−α)=y^(−α)[1−(1+2^a y^a)^(−α)]. Expanding separately for a=α and a=β, and using y/x=1+O(x^α) for all intermediate points in a pair, gives c+α2^βu^(−θ)−α(1+α)2^(2α)u^(−1)/2+O(u^(−η)), η=min(2,β/α)>1, in either order. Each branch decreases positive x, and the limit must be zero, so u_n∼cn. For θ<1, summing u_j^(−θ) gives c^(−θ)n^(1−θ)/(1−θ) and the logarithmic and summable terms are negligible. For θ≥1 the preliminary bound u_n=cn+O(log n) fixes the coefficient of the harmonic sum with a bounded error. At resonance 2^β=2^(2α) and the two inverse-power coefficients add to give +2^(α−1)(1−α) log n; above it the β term is summable, leaving −2^(α−1)(1+α) log n. The coefficients do not depend on phase or starting point. This is a pair clock, for fixed parameters 0<α<1 and β>α, not a uniform near-resonance crossover or a full-map first-return distribution. Inspected checker.py and verification notes without executing the uploaded script; the conclusion is analytic.

## originality

FAIL

A stronger preexisting result covers the complete clock law, not just the previously known negative log. Mardešić–Resman–Rolin–Županović, arXiv:1710.01268, give an actual Abel coordinate for parabolic Dulac germs, with a finite divergent-part algorithm whose first correction, specialized here, gives all three regimes and exact coefficients. There is no need for a new theorem in order to pass from their algorithm to the displayed clock. The lack of a distinct identical Resultary entry does not change this implication.

## value

FAIL

The resonance is well motivated and the short elementary illustration is useful pedagogically. As a standalone mathematical finding, however, the fixed-parameter trichotomy is the first-block specialization of the existing general construction, with no new uniform near-resonance estimate or extension to a statistical observable. It does not supply an independently unresolved structural fact after that implication. No substantive surviving repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
