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

In a fixed total-order insertion gap, the new point's predecessors are initial segments and successors are terminal segments of the two chains, restricted by the gap. If both sets are nonempty they must be in the same chain because every predecessor must precede every successor in the base poset. Conversely these conditions suffice for all new transitivity relations. This gives the displayed gap polynomial and counts each diagram once. Finite extensions are realized over the named base and homogeneity equates identical diagrams with identical complete types. Arbitrarily many copies of any such diagram can be added in the same gap, incomparable with one another, so none is algebraic. For an independent check of the defect formula, swapping adjacent BA to AB after i A-steps and j−1 B-steps changes only the intermediate gap, by 2(a−b)−4i+4(j−1). This matches the increment of 2∑[r_j²−(q_j−r_j)²] when q_j increases from i to i+1. The segregated base value from summing the gap formula is binom(n+3,3)+ab. In the nonnegative defect representation, vanishing requires all q_j equal at one endpoint; this works also when b=1. For a≥b, all nearest-integer choices to r_j=j+(a−b−1)/2 are within [0,a] and remain weakly increasing because successive centers increase by one. Completing the square proves the full optimizer classification; summing removes 1/4 per center for even d and zero for odd d, giving the two constants and the balanced limit. An independent transitivity enumerator checked 242 shuffles across 16 profiles with 1≤a,b≤4, reproducing both extrema and all equality cases.

## originality

PASS

Bounded coverage substantially overlaps on one-point extensions and on un-ordered two-chain counts, but the strongest inspected statements do not determine the number of compatible linear-extension gaps per diagram for a fixed shuffle. The exact dependence and extremal classification with the distinguished order survive these comparisons.

## value

PASS

Two incomparable chains are the first base family here with nontrivial variation of the distinguished order at fixed partial-order type. The formula quantifies that variation, gives every optimizing pattern and shows a factor 3/2 asymptotic change in the balanced case. The explicit defect identity is useful beyond recording extremal values and is not a routine single example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
