---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For theta in [0,1], Fθ′=fθ and Fθ″=1−θ+θ sech²(z/2)>0 yield proper strictly convex Hamiltonian ovals and unit small-amplitude frequency. On each level radial r(E,phi) strictly increases with E, and angular rate Omega=(1−theta)+theta*sum_(u=cos,sin)u² Q(ru), Q(z)=2tanh(z/2)/z strictly decreasing for positive |z|. Thus T0=2π; Tθ(E) strictly increases for theta>0, with Taylor small-E 2π(1+theta E/8+O(E²)). For fixed theta<1, dominated convergence gives plateau 2π/(1−theta); at theta=1 the large-E diamond yields T/E→1. Under epsilon=1−theta, V=epsilon*v,W=epsilon*w,s=epsilon*t, energy e=epsilon E, limit G0(z)=z²/2+2|z| and linear translated circular quadrant arcs yield epsilon*T(e/epsilon)→8 atan sqrt(1+e/2)−2π. Direct independent angular geometry identity checked at e=.4,1,3,8; inspected verify_period.py uses finite numeric corroboration, not proof of universal limit.

## originality

PASS

Pure Bayesian/logarithmic vs expected-payoff Matching Pennies endpoints, and generic separable-Hamiltonian period monotonicity criteria, are prior art. The two-parameter singular mixture epsilon E=e>0 and model-specific exact arctangent crossover are not stated or directly implied by inspected endpoint or general fixed-energy period results; best-of-knowledge originality remains with explicit accessible-literature limits.

## value

PASS

The sharp singular 1/(1−theta) energy crossover connects genuinely noncommuting high-energy and mixing limits in a natural replicator interpolation. The exact e-dependent trigonometric law and strict monotone period distinguish the mixed system from both endpoints; it is a motivated quantitative center-period invariant, not merely a generic theorem restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
