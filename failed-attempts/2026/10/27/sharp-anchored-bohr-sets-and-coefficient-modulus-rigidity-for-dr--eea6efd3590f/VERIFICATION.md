---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The constant function has norm one and M_phi 1=phi. Thus the nonconstant coefficients have weighted squared norm at most one. The degree-n sum of |x^alpha|^2/w_alpha is ||x||^(2n), also for countably many coordinates by monotone finite-coordinate truncation, so weighted Cauchy–Schwarz gives absolute convergence and the claimed inner ball. For a unit direction v, multiplication by its linear coordinate is contractive: the Drury–Arveson coordinate row is contractive, as the kernel identity for I-sum_j M_zj M_zj* leaves the constant kernel (finite partial sums are positive, with limiting sum in the countable case). The one-variable contraction calculus for s(r-s)/(1-rs) is justified by uniform Taylor convergence on the closed disk since r=1/sqrt(2). Its degree-n coefficients have absolute value r^n, including degree one. Choosing the coordinate along x realizes the homogeneous absolute sums (r||x||)^n and proves the sharp obstruction beyond r and attainment everywhere on the sphere. On the sphere the profile b has weighted norm one and weighted inner product with |c| equal to the majorant; expanding |||c|-b||_w^2 gives the exact identity. Both terms are nonnegative, and matching moduli is sufficient as well as necessary. No assertion about all phases is needed.

## originality

FAIL

A distinct earlier published record, faf5bb2ac122, already proves the same zero-centered ball, boundary attainment and coefficient-modulus characterization in a range including both frozen dimension regimes. The displayed defect and its stability bound are immediate expansions of the same weighted norm and inner product identities; they leave no supported distinct remainder. This is positive coverage evidence, not a verdict based on an unavailable paper.

## value

FAIL

The zero-centered radius and rigidity are natural and useful facts, but the frozen package adds only an elementary norm expansion and its immediate inequality to an existing theorem with the same mathematical content. As a distinct contribution there is no new exact invariant, stability estimate beyond that identity, or phase classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
