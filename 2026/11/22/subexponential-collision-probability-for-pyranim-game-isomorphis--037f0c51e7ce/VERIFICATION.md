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

Sampling is independent uniform on individual ideals, so the collision probability is the sum of squared class masses, not the reciprocal of the number of types. Put each distinct connected m-vertex type on a contiguous block in an umbrella ordering. Every edge interval forces precisely its subinterval chips; no cross-block chip is included, and unused bottom positions are absent. Permuting r blocks makes r! different ideals because the types are distinct. The block relabeling preserves the disjoint containment structures and the game, consistent with the cited graph criterion. Independently, one can establish the needed supply even without the exact connected-type formula: connected ordered umbrella graphs are specified by nondecreasing right endpoints R_i≥i+1 (i<m), R_m=m. Subtracting 1 from the first m−1 endpoints gives the Catalan sequences i≤R_i−1≤m−1, hence C_{m−1} patterns. For a fixed graph and a specified first vertex, BFS layers are contiguous cliques (their right endpoints are obtained by iterating R). Within each layer, preceding-layer neighbor sets are nested decreasing and following-layer sets nested increasing in any umbrella order. Sort by decreasing preceding degree and then increasing following degree; ties have identical neighbor sets by nesting and are interchangeable. Thus each first vertex produces at most one adjacency pattern, yielding c_m≥C_{m−1}/m, which already gives c_m≥n/m with the frozen m since (log n)^4 dominates m². Likewise, any ideal is coded by nondecreasing rightmost included endpoints R_i, with R_i=i−1 for an empty row; shifting by one and appending n+1 gives the Catalan sequences of length n+1. For m=ceil(log₄ n+4 log₄ log n), r=floor(n/m), Stirling gives log(r!)=n log 4−O(n log log n/log n), including an O(log n) flooring cost. Using C_{n+1}≤4^{n+1} and squaring the mass of this single class proves the asserted all-large-integer lower bound; p_n≤1 gives the root limit. It does not prove p_n tends to zero or give a sharp decay scale.

## originality

PASS

Credit the established game/graph correspondence and the connected-type enumeration. The distinct large class construction controls the weighted collision probability for uniform positions; neither the enumerated number of graph types nor the connected-type supply alone gives that lower bound. No demonstrated equivalent coverage beyond the identical target record was found in the bounded comparison.

## value

PASS

Determining the exponential rate for this natural collision experiment identifies a pronounced effect of the nonuniform class masses. A constructive single-class lower bound resolves the root-limit question as formulated in the frozen source, with an effective subexponential form rather than an extrapolation from counts at small n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
