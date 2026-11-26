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

On the event that the observations lie in (0,1), the continuous likelihood has score n(t-F_n(t))/(t(1-t)) except at the sample knots. The score is positive before the first knot and negative after the last, and the log likelihood is convex between knots. Integration, also at 0 and 1, gives the exact centered profile. Changing variables on the two pieces gives the population log likelihood log(2)-1, including the limiting densities. On a compact interior subinterval apply Donsker and continuous integration (the bridge limit is continuous); the expected uniform truncation error on either end is at most the integral of 1/sqrt(t(1-t)) over that end, both before and after taking the limit. This proves convergence in C([0,1]) and a.s. existence of continuous improper integrals. The bridge area I has covariance t(1-t)/2 with B(t) and variance 1/12. Thus subtracting 6I t(1-t) leaves a Gaussian path independent of 6I, and after integration the conditional process is a fixed continuous function plus an independent linear tilt with a continuous slope law. A tie between distinct locations forces distinct subgradients of the convex supremum in the slope variable, an exceptional Lebesgue-null set. The compact argmax mapping at a unique maximum applies to every measurable selection. The transformation B(t) -> -B(1-t) reflects the profile, and its derivative at the midpoint is a nondegenerate normal variable. This proves both half-probabilities and nonconcentration. The uploaded script was inspected only; its finite diagnostics are not needed in this proof.

## originality

PASS

The distinctive claim is convergence of the whole centered likelihood in the fully unidentified uniform case and the resulting nondegenerate global maximizer law, not the finite-sample knot rule or standard ingredients of the proof. It is not supplied by the closest inspected identified-mode asymptotics.

## value

PASS

The uniform case is a concrete, completely unidentified boundary where expected likelihood alone gives no optimizer selection. The exact functional limit and random MLE law explain that failure, including endpoint control and tie-rule independence; the result is stronger and more useful than observing a flat expected criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
