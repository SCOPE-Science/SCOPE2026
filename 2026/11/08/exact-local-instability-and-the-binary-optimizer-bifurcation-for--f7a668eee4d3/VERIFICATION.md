---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

New-entry event requires one uniquely missing coupon in the common (M−1)-block and matching entering coupon; independence and inclusion-exclusion derive weighted flux. Finite occupancy-number derivatives yield exact κ_{n,M}; leading positive (n−1)/n² (M−1)(M−2)((n−1)/n)^(M−3) for fixed n ensures local minimum, not global all-n optimizer. For n=2, derivative of μ=(t+t^M)/(1+t)^(M+1) has sign 1−Mt+Mt^(M−1)−t^M; monotonic derivative structure yields unique inner root for all M≥4 and only two globally maximizing asymmetric probabilities; M=2,3 have only balanced maximum. Independently checked polynomial Hessian coefficient for several n,M. Claimed asymptotic rare-one-type example is correct but known contextual bound.

## originality

PASS

The underlying weighted entry identity and a stronger global fixed-alphabet large-window asymptotic optimum were published already; these receive no novelty credit. The asserted all-n exact finite-M tangent-Hessian coefficient and the all-M binary global optimizer phase transition at M=4 are not implied by either the prior global asymptotics or published three-colour M=6 results. Originality is best of knowledge.

## value

PASS

A natural optimization problem exhibits an exact, nontrivial binary bifurcation at M=4, and an explicit all-alphabet finite-window local stability test for the same stochastic entrance functional. Unlike the known global asymptotic optimizer, these give finite-window structure and a sharp symmetry-breaking boundary, an independently useful mathematical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
