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

Gaussian strict positive definiteness ensures invertibility for finite positive lambda. Reflection fixes the weight vector and gives the positive-definite even block with determinant Delta>0 and the two stated Cramer numerators. Independent integration of the first three Taylor terms reproduces Delta=8(b²-a²)² lambda²+O(lambda³) and the stated numerator coefficients, so both limiting weights are positive when a²<1/3<b². An independent rational certificate uses signed Lagrange remainders: orders 23 and 24 enclose exp(-z) for z>=0 and can therefore also enclose each translated Gaussian mass by termwise integration. Outward rounded exact intervals for outer numerator, inner numerator and Delta at lambda=2 are respectively [-0.021574,-0.021572], [0.132727,0.132729] and [0.243788,0.243789]. For fixed interior nodes, sqrt(lambda)F tends to sqrt(pi)/2 and the even block tends to identity, giving eventual positivity. Continuity supplies two distinct outer-weight zeros and an open neighborhood of radii with the same sign-return pattern. Exactly two positive weights at lambda=2 attain the known general two-of-four lower bound; there is no need for a full count of outer-weight zeros or for the inner weights to stay positive at every shape.

## originality

PASS

The verified addition is a fixed four-site Gaussian design on a uniform interval attaining exactly two positive weights at an intermediate shape and recovering strict positivity at both shape extremes, robustly in the radii. Neither negative weights in general, the lower bound, nor convergence to polynomial weights in the flat limit is new.

## value

PASS

A fixed-node rule may be positive in both standard asymptotic regimes yet fail to be a positive functional at a practical intermediate scale. The strictly negative outer pair shows that the general half-positive bound is sharp even in a simple symmetric Gaussian design; the certificate and open-neighborhood result exclude a floating-point artifact or a single fine-tuned geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
