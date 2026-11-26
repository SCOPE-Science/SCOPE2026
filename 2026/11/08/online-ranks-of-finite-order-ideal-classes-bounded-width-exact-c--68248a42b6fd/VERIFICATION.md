---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The actual domain is membership queries on all lower ideals of an explicitly given finite poset. Starting with [∅,P], an available x∈U\L genuinely splits the interval: after a positive label the lower endpoint is L∪↓x, and after a negative label the upper endpoint is U\↑x. Each free set shrinks, so induction gives the maximum over root queries of one plus the lesser branch rank (a singleton has rank 0, including for an empty poset). The number of ideals is bounded by counting antichains of maximal elements, including the empty antichain. Thus there are at most (Σ_{j≤w} binom(n,j))² endpoint pairs and at most n queries at each; checking and updating bitsets and preprocessing the order is polynomial overhead. This establishes XP, not FPT. VC shattering is equivalent to being an antichain: comparable points forbid the upper-only pattern, and the downclosure of chosen positives realizes every labeling on an antichain. On the two-row grid the ideals are exactly pairs 0≤b≤a≤n. For each t, the rectangle t≤a≤n, 0≤b≤t is a product of threshold classes with n−t+1 and t+1 concepts; median queries give the sum of the floors of their binary logarithms by concatenation, even when one factor is a singleton. At n=2^(k+1)−2 and t=2^k−1 this gives 2k. The whole grid has 2^(2k+1)−2^k ideals, so the binary leaf count gives the upper bound 2k for every k≥1. Taking t nearest n/2 also proves the all-n logarithmic estimate without claiming the formula holds at every n. This is a full proof replay (RESULT.md §§1–5); the supplied verify.py and its finite coverage were inspected, not run.

## originality

PASS

Credit the earlier exact polynomial-state two-row recurrence and finite grid census to Resultary 6262182a47f2. The distinct claims supported here are the explicit endpoint-state transition bound for all finite bounded-width posets and the uniform sharp dyadic rank, not the width-two four-endpoint recurrence, its sample values, the generic Littlestone recurrence or the VC-width identity. The earlier exact computation evaluates every fixed grid but does not give the universal dyadic equality without a separate all-k tree construction.

## value

PASS

The result gives tractable exact online-rank evaluation throughout the natural class of posets of each fixed width, rather than just one structured grid. The rank certificate on the infinite dyadic family realizes the information upper bound in a class with fixed VC dimension; it gives a concrete, quantitative comparison of static and adaptive complexity and an exact benchmark for algorithms. The bounded-width transition estimate and the uniform exact subsequence, not the already available width-two rank table or the elementary VC formula, supply the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
