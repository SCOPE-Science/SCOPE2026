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

For a Gaussian of variance v and center m, division by its density gives the time derivative as a quadratic polynomial in the centered variable. Matching constant, linear, and quadratic terms against diffusion plus linear growth gives the three component equations in RESULT.md lines 23–39. The equal variances give equal center shifts and a fixed center gap; subtracting logarithmic component mass derivatives gives the displayed logistic equation. For fixed s(t) the linear equation is conjugate to the heat equation by an exponential linear multiplier and a time-dependent translation; hence the Gaussian representation agrees with the nonnegative Cauchy solution. Closing s(t) in the moment equations gives a locally unique scalar ODE. Positivity follows by the integrating factor for the mass and the susceptible variable and by the logit for the mode weight; their conservation and bounded center drift on finite intervals give global existence. If s retained a positive limit the center drift would force arbitrarily large positive per-capita growth, contradicting bounded total infected mass. In the derivative of conditional variance the weight factor g(p)=p(1-p)(2p-1) has a unique maximum 1/(6 sqrt(3)); the common feedback is strictly below its initial value for every positive time. This verifies strictness at equality. Starting at the maximizing weight below cutoff, the weight increases strictly, so the positive g and the feedback each decrease strictly thereafter, their product tends to zero, and the derivative crosses zero just once. For the frozen reversal certificate, the exact fractions in lines 52–60 give opposite initial and intermediate derivative signs. The bound on the common feedback follows by applying Gronwall to the sum of the two nonsusceptible fractions, not just to instantaneous infected mass. The needed logit inequality follows from exp(1)>8/3 by the degree-four Taylor partial sum. Exhaustion gives a later positive derivative, hence at least two turning points. The finite-dimensional vector field is analytic, so no flat intervals can create ambiguous extrema, and the initial positive sign persists at strictly positive times. The attached script was inspected and not executed; the mathematical certificate was checked directly.

## originality

PASS

The distinct assertion supported by comparison is the sharp uniform variance threshold and the two types of turning behavior for an equal-variance two-mode mixture under endogenous feedback. Neither Gaussian propagation, linear-trait heat-equation reduction, nor susceptible exhaustion is credited as new. Available scope-matching summaries concern the susceptible limit or the mean trait in a discrete model, not this conditional variance classification. The cited originating manuscript's decisive original passages were inaccessible; known formulas and potential unseen prior coverage are separated below.

## value

PASS

The exact solution isolates when a skewness term can overpower a positive diffusion contribution and supplies a rigorous counterexample to variance monotonicity in a closed mathematical model, including a case where the initial derivative has the misleading sign. The distinction between a sharp uniform bound and trajectory-specific reversals is materially useful for checking moment closures, without interpreting the example as pathogen manipulation or physical control guidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
