---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For equal generated embedded sets, each generator is a word in the other and its inverse, so ranks are equal. On a path of v vertices a word of net exponent t has rank at most max(v−|t|,0); on cycles it is exactly the corresponding full permutation power. A word of exponent zero is idempotent, while |t|≥2 loses rank on a nontrivial path. At t=±1, rank equality forces the entire available shift on every chain, hence exactly the original map or its inverse. In the a=1 case the generated set is the cyclic group on its support together with the global identity. For proper support, the global identity alone does not generate it; the group law and the support distinguish all remaining cases, including the empty map, partial identities, and full support at k=1. Labeled j-vertex paths contribute z^j and cycles z^j/j. Divisor inversion extracts the exact cycle LCM, subtraction imposes an exact nontrivial maximum chain size, and division by the proved fiber gives the formula for literal subsets. Rank n and n−1 supply (n+1)n! ambient maps, whereas permutations on subsets total at most e n!, yielding the stated bound for the cycle-only fraction. Fresh independent_check.py in /workspace/branches/6b81b380-80ca-44f5-84dc-774a0d8fac77/ enumerated exact generated sets for 1≤n≤6 and confirmed every joint profile and fiber; totals were 2,6,24,126,838,6841. The frozen verifier was inspected, not executed.

## originality

FAIL

The distinct indexed finding d8394c30e54e demonstrably gives the same embedded subsets, generator fibers, both joint-profile coefficient formulas and the total. Under h=a−1 (including a=1), m=k, A=P and B=Q, the formulas are identical. This is existing coverage at review, not an assertion about which work came first: the frozen and indexed records have different displayed dates, which by themselves do not establish priority or dependence. The 2023 type-count paper by itself would not warrant rejection.

## value

FAIL

Exact labeled multiplicities are a natural companion to the abstract type count and would be independently useful if unavailable. Here the literal-subset profile and all advertised counts are already present in an exact census; changing the chain parameter from arrows to vertices adds no new information. The larger finite check confirms that same quantity rather than certifying a new mathematical boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
