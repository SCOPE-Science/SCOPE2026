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

Summing the product of the two birth-parent laws over matching ordered parent-label choices gives r^2/b+r(1-r)/(ab)+(1-r)/b^2; restricting to off-diagonal parent labels gives (1-r)^2(a-1)/(ab^2). At j the sibling event already avoids i; the independent remaining births contribute the products of one- and two-label avoidance probabilities on exactly the ranges given. At r=1 the products telescope to give single-tree pair probability a/[(n-1)(n-2)]; squaring it at r=0 gives n/[12(n-2)], and summing it at r=1 gives n/6. With D=(n-1)(n-2) the products are at most ab/D. Using step functions on the scaled label triangle, this gives uniformly bounded summands after scaling by n/b for the normalized leading sum, and n^2/b^2 for the accidental and different-parent sums. At interior points the logarithmic expansions give x^(2-r)y^(2-r) along any sequence tending to r. The middle term contributes at most r/2; the integrals give 1/[(3-r)(5-2r)] and 1/[(3-r)(4-2r)] before the prefactors. For r_n tending to zero the first and last coefficients tend to 1/15 and 1/12 separately, not with a single additive o(1) error when n r_n^2 diverges. At n=3 the exact probability is (1+r)/4 with no mismatched parents. Inspected the supplied checker without executing it; the proof does not depend on its finite checks.

## originality

PASS

The credited coupling and the endpoint expectations are antecedent. The distinct claim is the exact intermediate-coupling terminal-sibling overlap resolving mismatched parents, and its expectation crossover for vanishing alignment. No inspected distinct result gives or implies that combined claim.

## value

PASS

The overlap is a natural genealogy-sensitive statistic for the aligned pair of trees; degree and leaf totals cannot resolve it. The exact kernel separates a linear-order shared-parent contribution from bounded parent mismatches, and the two constants describe the competition of copied and accidental incidence at small alignment. This is useful as an exact expectation benchmark and does not assert concentration or detectability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
