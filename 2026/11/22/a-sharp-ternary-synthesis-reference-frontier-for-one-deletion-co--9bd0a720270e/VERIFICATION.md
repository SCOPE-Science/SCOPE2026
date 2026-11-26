---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For labeled ternary length-three words, singleton deletion shadows are exactly constants; two-shadow words are two-run and consume a diagonal digram. With five disjoint shadows, zero constants would exceed nine digrams, one constant would force four two-shadow words with only two diagonals free, and two constants would force at least two two-shadow words with one diagonal free. Thus five words require all three constants, and the only compatible remaining pairs are reversed permutations of the alphabet. This proves the global ceiling and T≥9 for five words. For shorter lengths, embeddings of distinct correcting words intersect in at most one position; two and three words need at least five and six positions respectively. The stated length-five, six, and nine witnesses and monotonicity yield the exact all-length frontier. At T=6 four embeddings have each position used twice by the degree count and each pair meeting once, hence positions are edges of K4. A constant aaa would force its three companion stars to each include exactly one a and otherwise use the two remaining symbols on the triangle. At least two companions must consume only one of the four a-involving off-diagonal digrams, hence have repeated adjacent non-a symbols; two monochromatic incident pairs on that triangle would force the same repeated symbol and a diagonal collision. Thus there are no constants. Three words must be two-run using distinct diagonal digrams, and the fourth uses all three symbols. At the distinct-symbol star, its three spokes must each supply a duplicate to the other endpoint, since the three triangle edges can supply at most three of the six required duplicate occurrences. Orientation of the triangle edges toward the vertex using their duplicate then gives a directed 3-cycle. With the distinct-symbol word normalized to 012, the two cycles force the remaining ordered words 200,110,221 or 100,211,220 by the unused off-diagonal digrams. The position constraints order the six edges uniquely in each case, yielding 201210 and 210120, respectively. These lie in disjoint relabeling orbits exchanged by reversal up to relabeling; within each orbit the distinct-symbol word and hence the code are unique. A separate exact nine-bit-mask exhaustion over all 729 references confirms capacities 1:39, 2:336, 3:342, 4:12 and one code per optimum. For the cyclic comparison, 011,022,120 fit in 012012 and adding 000 is possible in 0120120; the census excludes four at the shorter length. The two frozen scripts and VERIFICATION.md were inspected, not executed. The independent finite replay forms all index-triple words, deduplicates each one-deletion shadow, then iterates include/skip transitions indexed by occupied digram mask, counting optimizer ties.

## originality

PASS

The supported distinct contribution is the optimal synthesis-time frontier with short-reference rigidity, not the unconstrained five-word ceiling or the deletion-shadow criterion. The strongest prior formulates the exact same optimization and supplies finite-length bounds, but its bounds do not resolve the decisive lengths, optimizer orbit, or gap versus cyclic references.

## value

PASS

The smallest ternary case in this formulation gives a useful exact benchmark: it exhibits a one-cycle gap between an optimized reference and the unrestricted-subsequence-optimal cyclic strategy. The census makes the gap structural rather than an isolated witness, and determines when full use of the digram space is forced. The work does not claim scalability to longer words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
