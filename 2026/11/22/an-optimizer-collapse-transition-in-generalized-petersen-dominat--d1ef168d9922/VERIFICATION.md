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

The two labeled graphs have exactly the rim ±1, inner ±2, and spoke neighbors in the frozen definition. Only unselected vertices enter the [1,2] test. Independent set-based enumeration exhausted every cardinality through six and verified that all lower layers are empty and the sixth layers have sizes 248 and 9. Testing the trace count 2^k for each support through k=6 gave 1,16,116,464,812,32,0 and 1,18,81,0,0,0,0; downward closure excludes every larger layer. A support is maximal precisely when none of its one-vertex enlargements is shattered, giving 660 four-facets and 32 five-facets at n=8. The two stated representatives have disjoint dihedral orbits of size 16 and their union is the full five-support layer. At n=9, on each shore an unselected vertex has exactly one same-shore selected neighbor (the two steps are the nonzero residues modulo three), and its spoke can add at most one. Thus all nine independent phase pairs are feasible, and the exact exhaustion leaves no others. On a single shore a pair of queries either agrees always or cannot be simultaneously positive, whereas cross-shore phases are independently selectable. This proves the graph K_(9,9) is the shattering complex; contracting a spanning tree gives a wedge of 81−18+1=64 circles. For the adaptive census, a query must split a residual family into two nonempty strictly smaller families; maximizing one plus the smaller attainable branch depth is exactly the full-tree depth. The independent recursion gives depths 6 and 2 with 91615 and 49 memoized states. At n=9 the first positive branch fixes a shore's phase, leaving only three hypotheses, which cannot support two further complete levels; the cross-shore VC witness attains depth two. The supplied code/logs were inspected, not executed. Independent replay: run independent_gp_check.py with each of arguments 8 and 9 under /workspace/branches/155acdf6-7d25-4517-97db-8181569e78c7/ and compare gp8_check.out and gp9_check.out. The mathematical conclusion is only for these two orders.

## originality

PASS

The all-order work already determines both domination numbers and gives one extremizer at each order. The supported distinct claim is the complete labeled minimum families' counts and their associated trace, facet, orbit and online data at these two orders, including the nine independent phase pairs. Neither retrieved primary results nor exact nearby catalogue statements imply that claim. This is a bounded determination, not a certification of priority; two plausible primary bodies remain uninspected.

## value

PASS

These consecutive natural orders share the known optimization cost, making the comparison about optimizer structure rather than size alone. The classes change from a rich nonpure complex with a strict adaptive advantage to a two-factor phase family with no adaptive advantage. Exact orbit and facet data give meaningful finite benchmarks, and the phase description explains the smaller complex and rank. This does not claim an all-order phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
