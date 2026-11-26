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

Conditional independence multiplies the no-call probabilities; subtracting the two gives J=e^{-Bb}(1-e^{-Ba}). Budget fractions yield exactly the convex hull of modality points. Since J increases strictly with a and decreases strictly with b, its optimum lies on the efficient lower increasing chain between the highest-signal minimum-background point and the lowest-background maximum-signal point. After merging collinear segments the slopes are strictly increasing. On the chain, log J is strictly concave (the log signal term has second derivative -B^2 e^{Ba}/(e^{Ba}-1)^2 and -Bf is concave). Its derivative divided by B is 1/(e^{Ba}-1)-s_j on edge j. Thus Ba=c_j on a mixed edge, and the one-sided derivatives at a vertex give exactly the displayed closed interval. Because c_j decreases strictly and a_j increases, the positive-length pure and mixed regimes join in order without skipping a vertex or producing a tied effective optimum at a boundary. Two adjacent retained vertices suffice, while equivalent allocations involving duplicate or collinear rates need not be unique. The singleton hull is immediate. For the example the slopes are 3/10 and 3/4; a_j=j, b_j=j^2 produces strictly increasing slopes and realizes the claimed sharp count for any r.

## originality

PASS

The supported claim is the sharp ordered schedule of exact pure and mixed effort regimes for this Poisson OR/Youden objective, not two-point convex-hull reduction, Youden scoring, or Poisson allocation in general. The closest actual allocation and false-positive design objectives differ in observables, losses or feasible controls. Abstract-level historical comparisons have the limitations noted below.

## value

PASS

For a specified detector rule and meaningful false-alarm tradeoff, the result answers a design question across all budgets rather than just writing optimality equations or identifying a two-mode upper bound. It tells a planner when mixing is strictly needed in the reduced representation, proves every exposed vertex has a positive-length pure regime, gives the widths of those regimes, and supplies an exact benchmark for testing adaptations of sensing-time optimization. The sharp schedule is the substantive contribution, not routine differentiation of one fixed objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
