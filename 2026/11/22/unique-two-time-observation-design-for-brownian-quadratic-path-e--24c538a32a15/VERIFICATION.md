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

For x=a and y=b-a, the normalized increments are independent Gaussians. Projection onto them gives the stated three inner products of the conditional mean basis; the independent residual adds only a deterministic trace to the conditional mean of Q. The residual after b is Brownian rather than a pinned bridge, which does not affect the projection argument. Isserlis and total variance give risk 1/3-2F, including duplicate and zero sites by dropping the redundant variable. Independent exact elimination reproduces the resultant and the linear relation y=-A/D. Sturm counting gives exactly three positive sextic roots, one per stated interval; on the first two brackets the signs of (A,D,-A-(1-x)D) are respectively (+,-,+) and (+,-,-), with zero counts for each sign polynomial. Only the first yields a feasible interior point. The witness 457/2916 exceeds 9/64 on both coordinate faces; its difference from the sloping-face polynomial is positive at zero and has no root on [0,1]. Compactness then forces the unique interior optimizer. Reproduced (a,b,risk)=(0.51844460651642214,0.85233448486089546,0.01965852971584853). The linear-area variance has cubic gap weights 1/12,1/12,1/3, giving (2/5,4/5); substitution gives quadratic risk 131/5625. Replay: python /workspace/independent_checks.py 3 (SymPy); original verify.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

Credit the exact global two-point classification for unpinned Brownian motion, not the Gaussian quadratic variance criterion, a result for arbitrary linear information, or an analogous bridge proof. The strongest indexed comparisons change the covariance or the admissible observations; neither supplies the constrained optimizer. This is a bounded best-of-knowledge finding, not a date-based priority inference.

## value

PASS

Two exact Brownian values are a natural physically constrained information budget. The global certificate supplies a concrete nonlinear-goal benchmark including repeated and endpoint designs, and the 15.588% risk reduction against the linear-area optimum has a mathematical explanation: quadratic explained variance depends on the squared inner products of the projected modes, not only on gap-area variances. The exact sites, rather than generic existence or the Gaussian reduction, are the useful addition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
