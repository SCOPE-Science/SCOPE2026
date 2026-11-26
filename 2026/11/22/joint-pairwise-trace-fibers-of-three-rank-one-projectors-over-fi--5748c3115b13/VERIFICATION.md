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

A projector is uniquely an ordered pair of distinct image and kernel lines, so conjugacy is transitive and fixing E=diag(1,0) costs a factor q(q+1). Cayley–Hamilton characterizes the remaining rank-one idempotents by trace one and determinant zero in every characteristic. Their off-diagonals satisfy xy=A and uv=C, and the third trace equation is xv+yu=d. If AC≠0, s=xv gives s+AC/s=d and each admissible s leaves precisely x∈K× free. If one product is zero the two coordinate-axis branches give 2(q−1) choices for d≠0 and intersect in the unique zero choice for each nonzero factorization when d=0. If both are zero, splitting (x,y) into its two open axes and the origin gives 2(q−1) for d≠0 and 2q(q−1)+(2q−1)=2q²−1 for d=0. In the nondegenerate support, s↦AC/s has one fixed point for even q and 1+χ(AC) for odd q; its orbits are exactly the attainable d values. For odd q the resulting summed bias is (sum_a χ(a(1−a)))²=1, by the difference-of-squares hyperbola count with 2 invertible. All 4(q−1) degenerate (a,c) pairs support all q values of b. These give the stated support for both parities, and the strict inequality 2q²−1>2(q−1) identifies exactly the four maxima, including q=2. An independent exhaustive fixed-E count over orders 4, 8 and 9 matched every cell, support 56, 368 and 509, and exactly four maximum cells in each case.

## originality

PASS

Pass for the exact ordered, unfused triple-trace fiber law, including the degenerate trace strata, even characteristic, support size, and maximum; not for rank-one parametrization, pairwise cross-ratios, or ordinary nonsingular Gram-matrix counting. The closest primary intersection tables for the hyperbolic scheme are on unordered line pairs and fuse genuinely different trace targets. The closest indexed conjugacy result gives exact pair orbits but not their three-projector incidence counts.

## value

PASS

The three pairwise traces are canonical two-factor conjugacy measurements for a triple of projectors. The all-field classification answers the natural realization and exact multiplicity questions lost under the unordered-pair fusion. It distinguishes degenerate extremizers, empty targets and the half-density obstruction without changing the sampling or restricting to one square class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
