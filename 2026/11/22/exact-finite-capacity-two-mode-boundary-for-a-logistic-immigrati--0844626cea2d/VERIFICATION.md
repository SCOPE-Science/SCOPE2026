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

Irreducibility and detailed balance give a unique positive stationary count law and R_1=Na. For t=j-1, the sign of R_j-1 is that of (N-t)(a+bt/(N-1))-(t+1), a concave quadratic in t. The positive ratios relative to 1 lie in a single interval, so the pattern is descent, ascent, descent with absent phases or ties allowed, giving at most two separated modal components. A strict initial descent plus a later rise is precisely a<1/N and b>min_t b_t(a); at equality all later ratios are at most one. To verify the envelope, write b_t=(N-1)/N*[delta/t+(N+1)/(N-t)]. Minimizing by Cauchy–Schwarz gives the displayed t_c and B_c; the numerator of b_t-B_c is a quadratic with leading coefficient B_c and a double zero at t_c. The function decreases on one side of t_c and increases on the other, so the two clipped bracketing integers suffice. The affine lines have slopes -(N-1)/t, ensuring strict decrease, concavity and motion toward smaller minimizing integers. For fixed eta<1 the minimizing integers equal sqrt((1-eta)N)+O_eta(1); bounded rounding displacement over denominator of order N^(3/2) contributes O_eta(N^(-3/2)), and the expansion of B_c gives the stated two correction terms. In the independent rational example with b=8/5 the first four ratios are 1/5, 89/100, 676/675 and 581/600; the unique threshold 639/400 makes R_3 exactly 1 and gives no rise. A separate exact finite replay checked 44,550 threshold/ratio comparisons at and near the transition.

## originality

PASS

The same stationary count law and its ratio are genuinely prior, and the at-most-two strict-mode observation has broader prior coverage. The finite inequality is a direct consequence of the old law. What supports this pass is the explicit real-envelope/integer-discrepancy boundary, optimizer geometry and fixed weak-immigration asymptotic of the modal onset, not a new model, invariant law, or observation of two peaks. The closest inspected sources do not give this boundary geometry, and moving from the law to it requires optimizing the discrete onset locus and controlling its rounding in a joint scaling regime.

## value

PASS

Observed vacancy and occupied peaks make the finite stationary count onset a natural invariant separate from active-time or metastability approximations. The continuous minimum alone can wrongly predict a finite-integer rise; the explicit lattice discrepancy, exact tie rule and candidate indices make the boundary usable at any capacity. The weak-immigration expansion identifies both the magnitude and immigration dependence of a meaningful finite-capacity offset from b=1 and the occupancy where it first occurs. This is more useful than re-reporting the stationary ratio or a particular numerical peak plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
