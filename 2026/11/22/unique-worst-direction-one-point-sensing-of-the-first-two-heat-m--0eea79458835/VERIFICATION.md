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

Reassessed the repaired heat claim. The decays are e^(-t) and e^(-4t) at the specified diffusivity and Euclidean amplitude normalization. Their energy Gram is positive definite for all T>0; the reflected objective vanishes at the endpoints and midpoint and is positive in each open half. The repaired background argument correctly factors 1+exp(z) out of the sign-conjugated inverse; the residual matrix has log-convex nonzero entries (positive irreducible for b≠0, diagonal otherwise). Convexity of its log spectral radius plus the strict scalar factor and divergent inverse tails gives precisely one optimum on each half. Independently, the squared area identity for the Gram determinant gives Delta_T/T⁴ -> 3/4 by integrating 9(r-q)²/2 over the unit square. The stable trace/determinant formula then gives uniform convergence of T^(-3) Lambda_T to 3u(1-u)/(1+4u), whose unique maximizer is (sqrt(5)-1)/4. At infinity the uniform eigenvalue limit has positive gap for 0<u<1 due to its off-diagonal entry, so interior stationarity gives a characteristic-polynomial resultant of -9(1-u)²(50u³+19u²+4u-9)/10000. The cubic is strictly increasing on [0,1] with opposite endpoint signs; its unique interior zero must be the limiting optimizer. Uniform convergence on the compact design interval justifies both argmax limits. Independently reproduced the sites 0.3123764311071713 and 0.2737605526096953. The determinant comparator has unique u=1/3 independently of T, as stated in the repair. Replay: python /workspace/independent_checks.py 5 (SymPy). Original verification and program were inspected, not executed; no claim about monotonicity, measurement noise or higher modes is made.

## originality

PASS

For the repaired claim, credit only the exact short- and long-horizon optimizers for the specified single-point, two-heat-mode worst-direction design. The general convexity/uniqueness assertion is treated as classical machinery applied to these gains. None of the strongest checked spatial or spectral design results gives the two exact horizon endpoints under this criterion and admissible set. This is a best-of-knowledge judgment, not absolute priority.

## value

PASS

A one-point, two-amplitude experiment is the simplest heat model in which weak observability arises from nearly indistinguishable temporal modes. The endpoints show a precise horizon-dependent change in worst-direction design, contrasting with determinant design whose optimizer is horizon invariant. The short-time rank loss is reflected in cubic-in-time information; the late optimal point is instead determined by the integrated modal Gram. These exact limits are useful benchmarks for sensor design and numerical methods near temporal degeneracy, without claiming a temporal monotonicity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
