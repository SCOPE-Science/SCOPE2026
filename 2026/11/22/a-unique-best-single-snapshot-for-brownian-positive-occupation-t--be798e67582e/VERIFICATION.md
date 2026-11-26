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

For standard Brownian motion starting at zero, at a predetermined time x>0 the full observation is equivalent to Z=B_x/sqrt(x). Two independent conditional Gaussian residuals that share Z have unconditional sign-input correlation rho_x(s)rho_x(t); the Gaussian orthant identity therefore gives the stated double integral for Var(E[Q|B_x]). In log time the two straddling rectangles contribute zero to the derivative, while the two same-side squares give e^(-2r)(C-G(r))/pi. This can be justified by splitting at the moving boundaries (the boundary terms cancel by continuity) and using the locally integrable kernel (e^(a+b)-1)^(-1/2). Integrating H'' over the square gives G=H(2r)-2H(r); G rises strictly from zero to infinity, so the derivative changes sign exactly once. The endpoints x=0 and x=1 are covered, with V(0)=0 and V(1)=(1-log 2)/4. Projection in L² yields risk 1/8-V(x). Independent scalar evaluation gives x=0.58958511090724239247 and risk 0.02553546323245417006; the closed variance agrees with an independently evaluated 100,000-term arcsine series to 7.90e-15, within the uniform bound 1.60e-11. The series tail follows from a decreasing cubic bound. The line calling the result 'minimax' is a terminology slip: the objective proved is minimum unconditional Bayes risk under a specified Brownian law, not a worst-case criterion.

## originality

PASS

No inspected source establishes the full-real-state, fixed-in-advance one-point optimum for Brownian positive occupation. Conditional-mean estimation and Gaussian orthant identities are prior ingredients. The supported distinction is the exact design risk as a function of time and its unique optimizer, not conditional expectation, the arcsine law, or occupation estimation in general.

## value

PASS

One noiseless state is a natural sparse-information constraint, and Brownian positive occupation is a nonlinear path summary for which optimal timing for reconstructing the path is not a substitute. An exact global location and risk solve that design problem and give testable benchmarks against terminal or one-bit observations. The explained-variance comparison is substantive (about 79.57% at the optimum versus 61.37% at the endpoint under the same experiment); the analytic uniqueness rules out alternative equally good deterministic designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
