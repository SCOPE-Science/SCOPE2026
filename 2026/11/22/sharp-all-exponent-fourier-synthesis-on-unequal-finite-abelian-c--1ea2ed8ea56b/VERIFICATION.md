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

On the dual grid, the unnormalized transform of the two-axis support is exactly the additive subspace F=u(chi)+v(psi), by inversion on the factors. Translating a largest entry by a character modulation and scaling it to 1 gives the normalization; the computed minimizer itself has every other entry of modulus strictly below 1. The counting-measure r-power is strictly convex on complex arrays for r>1. Independent permutations fixing the trivial index preserve additivity and the constrained minimum; the unique constrained minimizer therefore has four levels, 1,a,b,t, with t=a+b-1. For M=m-1 and N=n-1 the objective minus 1 is N|a|^r+M|b|^r+MN|t|^r, under a+b-t=1. As a cross-check, weighted Hölder bounds this below by [N^(-1/(r-1))+M^(-1/(r-1))+(MN)^(-1/(r-1))]^(-(r-1))=MN/D^(r-1), with equality at (a,b,t)=(alpha,beta,-1)/D and no other triple. Inverting gives the claimed arm levels by character orthogonality and the center by subtracting the arm masses from 1. At r=2 the result reduces to sqrt((m+n-1)/(mn)), and on equal orders the fixed-r asymptotic follows by retaining the two growing terms in D. The sign is measured on the distinguished sum-normalized representative, not after an arbitrary complex scalar. Its numerator equals mn at r=2, is positive below 2, and for both orders above 2 decreases strictly to 2m+2n-mn. This limit is zero exactly at the finite-r strictly positive boundary (m-2)(n-2)=4; a negative limit gives exactly one crossing after 2. If m=2 the numerator is 2+2 beta>0, and the transpose gives the n=2 case. With equal orders q>=5 solving the crossing equation gives the stated logarithm. Endpoints are not part of the uniqueness assertion.

## originality

PASS

The exact finite-field equal-order r=4 specialization, its equality cases, and its sign split already occur in distinct catalogue records, and the transitive (2,2) case is covered by a primary theorem. The supported distinct contribution is the exact all-r additive-product solution for arbitrary factor orders and the resulting complete origin-sign transition, not those special cases or the general synthesis framework. The exact overlapping catalogue records share the assigned date, which does not determine relative priority.

## value

PASS

A cross is a natural non-product Fourier support beyond the usual transitive synthesis model. The exact result shows how asymmetric arm multiplicities jointly control synthesis at each exponent and gives a concrete cancellation phenomenon: as r passes the unique threshold, the normalized central coefficient can vanish and then become negative even though both punctured axes remain positive. Unlike a single Fourier table, this distinguishes the support of the optimizer and its coefficient signs throughout the parameter range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
