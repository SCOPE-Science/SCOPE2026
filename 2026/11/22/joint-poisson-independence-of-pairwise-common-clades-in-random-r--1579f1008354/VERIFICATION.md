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

Contraction gives the claimed joint cherry probability for specified disjoint pairs. In the mixed factorial moment let g be the number of distinct leaf pair labels, v the number of distinct leaves, and e the number of incidences (distinct leaf pair, tree required to contain it). A feasible pattern contributes O(n^(v-e)); v<=2g and e>=2g. A repeated label across different overlap coordinates makes e>=2g+1, and a leaf shared by distinct labels makes v<=2g-1. The remaining distinct disjoint configurations give 8^(-R). The contraction formula for each clade size has increasing successive ratios; sizes 3 through n-2 are bounded by the equal endpoint probabilities, and size n-1 contributes n/(2n-3)^2. The resulting O(1/n) error transfers the array for fixed q; the joint zero event is a continuity set when tested using a box with half-integer bounds. In the exact covariance calculation, conditional independence given the shared tree reduces the covariance to its cherry-count variance times (2n-3)^(-2). The variance follows from the first two factorial moments, E C=binom(n,2)/(2n-3), E(C)_2=6 binom(n,4)/[(2n-3)(2n-5)], and simplifies to the stated positive expression for n>=4. Disjoint index pairs involve independent inputs.

## originality

PASS

The supported incremental claim is the complete fixed-q array in the rooted PDA model with an explicit finite-size shared-tree dependence contrast. The one-pair Poisson law, its rooted/unrooted relabeling, and the one-tree cherry variance are not credited as new. The closest all-pairs analogue has a different tree distribution and a different event (edge intersection).

## value

PASS

The relevant statistical object for more than two trees is the distance matrix, not a single entry. The full law answers a simultaneous extreme-distance event that scalar limits do not determine, and separates finite shared-tree dependence from limiting independence. This is a modest, meaningful extension in the standard uniform topology model; the scalar law and conditional variance algebra alone would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
