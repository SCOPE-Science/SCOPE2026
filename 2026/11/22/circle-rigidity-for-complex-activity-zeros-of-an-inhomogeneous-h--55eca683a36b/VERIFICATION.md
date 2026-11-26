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

Condition on even occupations s_j∈{0,1}; the factor for odd site j is w_j=1+b_j if s_j=s_{j+1}=0 and 1 otherwise. Assigning z to the occupied row gives exactly the displayed transfer trace. The extreme coefficients count the corresponding even subsets, including for C₄ where the two adjacent odd vertices are distinct and c₁ coincides with the z^(n−1) coefficient. Nonzero equal-modulus roots have modulus R=c₀^(1/n), and reciprocal and first root sums give c₁/c₀=n/R². The normalized terms R²/(w_{j−1}w_j) have positive geometric mean one; equal arithmetic mean forces all adjacent products equal, which is equivalent to the stated two-periodicity. Failure of periodicity gives a strict coefficient witness; for n=3 and b=(1,2,4), c₀=30 and c₁=10>3·30^(1/3). For sufficiency, if λ,μ are the two transfer eigenvalues, λ^d+μ^d is the monic polynomial in t=λ+μ with roots 2√(λμ)cos((2j+1)π/(2d)); this follows from the recurrence with product λμ, so it also holds polynomially at zero or repeated eigenvalues. For an alternating pair, t=z²+2z+R² and λμ=bc z², giving the claimed even factors with no branch ambiguity. In the homogeneous odd case pair opposite cosines and keep the zero cosine, giving z+R and the stated squared-cosine factors. Distinct cosines (or squared cosines in the first quadrant) and strict |linear coefficient|<2R give simple, disjoint conjugate pairs on the circle. For unequal b,c, R>1+√(bc) uniformly separates the cosines from −1 and 1; in the homogeneous even limit the extreme cosine tends to −1 in the root-angle formula. The supplied script was inspected, not executed; it tests small cases and the all-n conclusion above is algebraic.

## originality

PASS

The constant-on-each-shore transfer setup and homogeneous-background route to zero locations are prior or direct from prior transfer formulas. Distinct content supported here is the iff criterion across every positive background vector, the unequal period-two family on one shore, and its exact simple-root and persistent angular-gap description. The inspected sources do not establish that classification. Historical uniqueness is not certified.

## value

PASS

The finite hard-core cycle with one common variable shore is a natural test of robustness of Lee–Yang-style circle localization under fixed spatial inhomogeneity. It gives a full and inexpensive test (strict inequality in one coefficient), identifies the nonuniform backgrounds that preserve localization, and provides quantitative angular exclusion and simple roots in that family. This is a structural finite-volume result, not a thermodynamic phase-transition claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
