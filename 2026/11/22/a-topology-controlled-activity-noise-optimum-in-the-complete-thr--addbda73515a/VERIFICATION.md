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

Independently generated labeled edges by scanning the cyclic triples 110 and 101 and verified full directed reachability in both directions on 4, 10, 20, 35 and 56 states. For a separate symbolic calculation, represent states by cyclic vacancy gaps g₀,g₁,g₂ after ordered particles. A hop transfers one vacancy from positive gᵢ to gᵢ₋₁ at dimensionless rate 1_{gᵢ₋₁=0}+q1_{gᵢ=1}, including both channels and jumps staying in the same quotient orbit. On the gap quotient the checked stationary weight is the cyclic orbit multiplicity times q to the number of zero gaps. With escape rate r, generator L and stationary mean J, solve Lh=J−r in a fixed-state gauge. The corrected count Q_t−Jt+h(X_t)−h(X_0) is a martingale, whose stationary squared jump rate is the sum of π(g)w(g,g′)[1+h(g′)−h(g)]². The boundary correction is bounded, so this yields the long-time variance rate. It reproduced all five rational J and F pairs exactly, verifying positivity of each mean derivative and of F−1 for n≥5 (with F₄=1). Exact root tests and sign brackets confirm strict F₅ monotonicity and exactly one interior global minimum on each of n=6,7,8 in the three advertised intervals. With at least one vacancy, a gap of one enables a follower hop and a cyclic run of zero gaps ending before a positive gap enables a leader hop; all gaps ≥2 are frozen and first possible at n=9. Differences between different bond counts stay bounded by particle conservation, so an individual bond has asymptotic mean αJ/n and Fano ratio F/n, rather than the displayed total-count ratio. The frozen checker was inspected, not executed.

## originality

PASS

The process, stationary law, and stationary mean-current analysis are prior, as are tilted-generator and Poisson methods. The supported distinct result is the exact finite integrated activity variance-to-mean classification over the complete three-particle active range, including the change from monotonic/Poisson behavior to unique interior minima. The closest inspected primary results and same-date indexed cases do not supply that classification under the same dynamics and observable.

## value

PASS

Fixing three particles and examining the whole irreducible active range is a natural, exhaustive cutoff rather than selecting sizes with a desired effect. A finite-size transition from Poisson or monotone activity noise to a unique nonzero optimum, while mean throughput remains increasing, separates time correlations from stationary transport. Exact signs and thresholds are useful small-system benchmarks for constrained transport, independently of a large-ring theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
