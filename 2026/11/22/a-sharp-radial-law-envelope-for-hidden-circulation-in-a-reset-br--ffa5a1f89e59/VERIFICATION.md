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

For positive temperatures, 0<u<1 and independent full Poisson resets with centered marks of covariance mI, conditioning on the last reset gives the stationary OU mixture. The shifted Lyapunov equation has a unique solution and diagonal difference 2(T_y−T_x)/(r+2). The conditional future mean e^{−(A+rI)τ}Z_t gives C_r(τ)=C_r e^{−(A+rI)τ} (A symmetric); negative lags transpose. In the high-rate limit the age and noise go to zero in probability and g is bounded and continuous at the mark almost surely since R>0. Put W=R² and f=E[cos(2Θ)|W]. The exact attainable set of f is |f|≤1 with E[Wf]=0: conditional antipodal axis masses implement every such f and give zero cross moment and zero mean. The qualifier E[Wf]=0 is implicit from the preceding constraint and is needed in the implementation paragraph. For an explicit optimizer, use a median b>0 of the probability law with weight W/EW and let f be +1 below b, −1 above b, balancing its value at b. Then E[Wf]=0 and E[f]=E|1−W/b|. The upper bound E[f]≤E|1−aW| for every a≥0, followed by sign flip and scaling, proves the entire closed interval, including atoms and single-radius laws. At the two specified radii, the weighted masses are both 9/10; the dual objective is 4/5 on [1/9,1]. For r=5000 the norm drift/noise bound is at most 9/10000+sqrt(12/5000), giving error strictly below 509/1250 in E[g] and opposite angular velocities beyond ±491/2500, while L=2/5002 for both. The zero-reset Gaussian integral is strictly positive because the diagonal difference is T_y−T_x>0. Writing Ω(r) as r times the Laplace transform of the bounded fixed-age angular expectation also gives real analyticity for r>0; opposite signs therefore entail a strict crossing, not a zero plateau. The observable is the specified continuous-flight forward mean, not winding or jump rotation.

## originality

PASS

Credit the prior forward angular formula, ordinary moment closure, and fixed-point orientation-dependent reversal. The supported distinct result is the sharp constrained range at an arbitrary prescribed radial law, with a covariance-matched pair that has opposite signs at one finite rate while both angular momenta stay positive. The covariance formula itself follows routinely from the linear renewal model and is not the independent novelty claim.

## value

PASS

The nonlinear angular observable can reverse sign even when all position covariance functions and the reset radial law agree, and even when angular momentum remains positive. The exact extremum identifies how radial heterogeneity and angular allocation produce this identifiability failure, rather than merely giving another example of unequal higher moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
