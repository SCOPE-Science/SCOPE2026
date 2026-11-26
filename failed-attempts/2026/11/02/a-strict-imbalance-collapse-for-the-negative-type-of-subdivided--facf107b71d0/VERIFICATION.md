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

The distance classes in RESULT.md give the stated mass form and orthogonal grid and contrast blocks. With a=1+h, the contrast determinant is bounded below using (1+h)^3 >= 1+3h and 3^p-1 <= 2h; the resulting (1-h)(1+(k+3)h) bound is strict for 0<h<=1 in the preceding inequality, and the determinant is 1 at h=0. The grid eigenvalue is negative up to beta<1. At beta the mass difference u=(1,-1,0) has zero quadratic value and nonzero pairing with v=(1,1,-2); 4^p+2-2*3^p strictly decreases to zero at 1. Starting with D_0=all-ones minus identity therefore gives a first determinant zero below beta and a rank-one negative semidefinite mass form there. Strict fractional-power interpolation of a negative-type matrix rules out every higher admissible exponent. Schoenberg's distinct-point realization gives strict Gaussian positivity at the endpoint and the centered Gram rank gives the claimed dimensions. Above cutoff the positive powered-distance quadratic form on a zero-sum vector gives a negative kernel quadratic form to first order in small t. For p=O_m(1/n), the two mass diagonal entries are -1/m+O_m(1/n) and -(m+1)/(mn)+L_m p+O_m(1/n^2), and the off-diagonal is O_m(1/n); L_m=(4-1/m)log 2-2log 3>0. Uniform screening below the leading root, followed by the Schur complement at the root, gives the stated O_m(n^-2) remainder. The comparison beta also follows by restricting to original vertices, whose metric is twice the unsubdivided metric.

## originality

FAIL

A distinct same-date Resultary record already contains a mathematically equivalent classification on the full unequal domain, with the same endpoint nullity, dimension change and fixed-thin-side coefficient, as part of a broader theorem. The mass forms are explicitly congruent. Equivalent coverage is established; within-day priority is not. The direct contrast estimate and the standard kernel reformulation do not leave a distinct substantive claim of the frozen strength.

## value

PASS

As mathematics the all-unequal classification identifies when adjoining a natural class of vertices destroys a Hilbert-embedding threshold. The inverse-size collapse despite a positive limiting baseline and exact loss of one dimension at cutoff are meaningful structural conclusions, not incidental finite recomputations. This intrinsic value is separate from duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
