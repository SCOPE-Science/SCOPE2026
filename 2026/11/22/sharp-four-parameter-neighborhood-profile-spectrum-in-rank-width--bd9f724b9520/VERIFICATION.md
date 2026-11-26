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

The minimal subtree on the four marked leaves, with degree-two vertices suppressed, has a central edge. An original tree edge inducing that split has two parameters on each side and binary cut rank at most one. Restricted rows or columns have at most two possible patterns on the opposite pair (zero and at most one nonzero pattern), even when the realizing vertex is a parameter. This confines the traces to at most two rows and two columns of the four-by-four table, giving at most 12. Shattering any larger set would shatter each of its quadruples. A fresh exact check verified connectedness and distance-hereditary reduction certificates for both witnesses, the twelve listed four-set traces, and the eight different triple traces. In the 13-vertex witness three traces already occur among the parameters, and each of the other nine vertices realizes a different additional trace. Induced subgraphs retaining the parameters retain exactly their selected profiles, so all 3–12 occur; four isolated vertices and the four-vertex star give 1 and 2. The eight-vertex connected witness shatters three, and no smaller witness can realize eight traces. The replay script is branches/fec4ef40-fb63-42da-b771-ef60cc56fd99/independent_check.py, with CHECK_OK in the completed run. The supplied checker was inspected, not executed. The finite witness checks do not establish the universal bound, which follows from the cut argument.

## originality

PASS

The known cut-rank lemma gives the cross-cut row/column template, not the exact global spectrum. The supported distinct content is the sharp four-parameter maximum and attainment of every cardinality, together with exact triple shattering in the full distance-hereditary class. The broader complexity bounds, different VC notions and closest exact catalogue results inspected do not provide the 12-profile extremizer or four-parameter spectrum for this class.

## value

PASS

This gives the first parameter size past the class's shattering threshold, where a mere VC bound misses three cells. The rank-one cut explains the sharp obstruction, and the certified graph construction shows its full strength can be attained simultaneously while also determining the intervening cardinalities. This is a useful exact benchmark for adjacency types in distance-hereditary graphs, not just a count from a finite graph list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
