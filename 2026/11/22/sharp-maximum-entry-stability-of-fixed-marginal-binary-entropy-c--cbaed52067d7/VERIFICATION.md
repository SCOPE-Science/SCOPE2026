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

With fixed interior marginals the feasible table is P(z)=(z,r-z,c-z,1-r-c+z). The first-order equation equates its log odds Theta(z) to the checkerboard contrast h(X). Theta is strictly increasing onto R, with Theta'=H, so every interior z is realizable and the positive optimum is unique. The input contrast has max-entry dual norm 4 and the output checkerboard has max-entry norm 1. Integrating the derivative gives the global bound, and perturbing the realizing kernel at z_* in the checkerboard direction proves sharpness as a supremum. H'' is twice the sum of the four inverse cubes, and endpoint blow-up makes its minimizer unique. Row and column reciprocal-pair bounds are 4/[r(1-r)] and 4/[c(1-c)], respectively, with equality exactly for equal splits in the relevant pairs. If c=1/2 the row bound attains the smaller variance, and symmetrically if r=1/2. At independence, H'(rc) is minus (1-2r)(1-2c) divided by the positive product r²(1-r)²c²(1-c)²; strict monotonicity of H' gives the association sign. Cost scaling by 1/epsilon is exact. No evidence of finite-pair attainment is needed.

## originality

PASS

Best-of-knowledge pass for the optimized fixed-marginal diagnostic and, in particular, its sharp variance-equality and association classifications. The fixed-margin odds parameterization and pointwise Sinkhorn differentiation are not new. Writing a global norm as the supremum of the pointwise norm is a standard step and is not credited in isolation.

## value

PASS

The optimized response is a natural conditioning invariant for a binary regularized transport block. The strict gap from the generic smaller-variance estimate outside the balance locus and the location of the worst table relative to independence are practically and mathematically informative, beyond rephrasing the inverse-odds formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
