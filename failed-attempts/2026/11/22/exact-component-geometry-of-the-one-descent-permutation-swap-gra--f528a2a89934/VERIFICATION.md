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

The Finding is correct. In the two increasing blocks with descent x>y, write L=(a<y) for the left flank if present and R=(x<b) for the right flank if present. At an interior descent the left and right swaps are legal iff L and R, respectively; the central swap is legal iff exactly one of L and R holds. The frozen proof's line 42 uses an inclusive-looking 'or' for the central swap, which requires this correction: for example 1324 allows both outside swaps, but its central swap produces 1234. This does not affect the nonisolation condition L or R, and the corrected calculation gives degree two at every mobile interior vertex. At either endpoint and n>=3, the one flank gives two complementary possibilities for legality of the central or outside swap, hence degree one. The nonisolation conditions force all but the displaced value to be increasing, in exactly the two stated template forms: L forces the initial d-1 values to be 1,...,d-1 with y=d, and R forces the final n-d-1 values to be d+2,...,n. The endpoint singletons give the same forms. The displayed steps between t and t+1 are adjacent swaps, so exhausting the legal degrees proves no chords or additional neighbors. The templates have only one inverse descent, at j, which distinguishes their lists. Nonempty proper prefix subsets other than initial value intervals yield 2^n-n-1 vertices, from which the component, isolate, edge and mobile counts follow. For n=2 the lone vertex is isolated and the n>=3 path formulas are not applied to it.

## originality

FAIL

The graph, including the path labels and the exact shortest distances, is a direct restriction of established Knuth and tableau dual-equivalence graphs via RSK. This is verified implication, not an assertion that Assaf explicitly printed this induced graph. The matching OEIS count alone would not suffice to reject originality.

## value

FAIL

The natural slice is readable as an illustration of dual equivalence, and its explicit state coordinates can be useful pedagogically. But the graph decomposition, distances and state coordinates are the elementary one-descent restriction of the established tableau graph, and the remaining counts are routine consequences. No independently valuable unknown exact invariant survives the coverage comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
