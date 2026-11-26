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

The pins make the path precision positive definite, with stationary covariance K^(-1)/2 for identity diffusion covariance. Eliminating the free exterior tails and the interior resistors gives the two-endpoint matrix with diagonal kappa+1/d and off-diagonal -1/d. Exterior increments contribute s at distance s, and the bridge contributes t(d-t)/d plus the variance of the linear endpoint interpolation. Summation gives (5); at fixed d the only imbalance penalty is (ell-h)^2/4, making balanced tails necessary and sufficient and giving (1). After division by n^2 the parity and bounded constant terms actually incur O(n^-2) error for fixed c, uniformly over the gaps. Compactness and approximation of every continuum point by admissible grid points transfer minimizers. The cleared derivative has the stated signs outside [1/2,2/3], and the positive second derivative inside it gives one root. The mixed derivative has the sign of c r^2+6r-6, negative for c<9/2 and positive for c>12 throughout the candidate interval. This proves the required signs of r'(c) directly, avoiding the shortcut of differentiating the displayed big-O expansion in RESULT.md line 101. Eliminating c in the stationarity condition gives the unique admissible r=1-1/sqrt(7) and c=(7+4 sqrt(7))/3. Evaluating the cubic at r=3/5 gives the sole crossing c=5/3; dividing it by c^2 as c grows and using r>=1/2 gives the strong-gain limit, and c->0 yields 1/2. Direct exact cofactor traces for all 210 placements at each of the three gains on P_21 reproduce both the claimed optimizer sets and the exact distinct-gap margins 1307/2970, 19/240 and 169805/1666764.

## originality

PASS

The all-graph two-noisy-leader trace criterion is prior and covers evaluation by specialization; inverse-trace reentrance on other graphs is also prior. The supported distinct content is the exact path arrangement reduction coupled to the all-c asymptotic optimizer, strict overshoot and exact finite return on a unit path. The low/high-gain P_51 and P_101 examples in RESULT.md lines 111–113 were verified in Fitch's thesis §4.2.2; they should be attributed there rather than asserted to occur in the inspected 2014 arXiv version, whose explicit path corollary concerns noise-free leaders.

## value

PASS

Two equal leaders on a uniform path are a standard, simple instance in which exact optimal spacing might appear to grow monotonically from weak to effectively perfect feedback. The intermediate overshoot and its unique analytic peak refute that inference and the finite all-pairs certificate shows it does not depend on a continuum approximation. The fixed-gap formula also yields a linear-size exact search over gaps rather than pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
