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

For arbitrary real polynomials f,g of total degree ≤2, all four lines of Q=[-1/2,1/2]^2 are invariant. If finitely many boundary equilibria, each open edge contributes ≤2 and four fixed corners give N≤12. On an oriented invariant circle, each full hyperbolic sink is attracting from both adjacent arcs, requiring a separate intervening zero; 2S≤N, so N≤11 implies S≤5. If N=12, each edge has two distinct quadratic roots, exactly one tangential sink per edge. Opposite horizontal restricted quadratics share the x² leading coefficient and opposite vertical ones share y² coefficient, fixing simultaneous end orientations; at most one corner can attract along both incident edges. Hence ≤4 open-edge plus 1 corner sinks. For an identically stationary edge, hyperbolic sinks persist under generic coefficient perturbation, reducing to finite case. Independent direct evaluation of stated explicit f,g yields horizontal roots ≈(-0.204024,0.404024) and vertical roots ≈(0.0351978,0.3648022), 12 boundary hyperbolic equilibria classified as 5 sinks, 6 saddles, 1 source; all signs are strict, so open coefficient realization. Source exact checker check_boundary_sinks.py uses rational quadratic fields to certify witness; finite check not used for infinite coefficient bound.

## originality

PASS

PASS best-of-knowledge: older boundary count restricts coefficients and counts all equilibria; the general arbitrary-quadratic-factor bound counts full-planar hyperbolic sinks, and its 12-equilibrium five-sink witness is outside the restrictive counting conclusion.

## value

PASS

Five is a sharp boundary capacity for a natural broad quartic invariant-square model. It distinguishes full-plane stability from one-dimensional tangential attraction and from total equilibrium counts, with synchronized opposite-edge leading coefficients producing a genuine structural sharp bound. Useful when examining boundary attractor configurations in planar polynomial dynamics; not an arbitrary unmotivated sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
