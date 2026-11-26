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

In the defined four-layer graph every vertex has one same-index neighbour and neighbours at the two adjacent indices, staying in its outer layer or swapping the two inner layers. For n≥3 this gives 4n vertices, distinct unordered edges, degree three and 6n edges. The graphs in the finite claim are connected. In an independent reproduction I formed shortest-distance layers, built a bitset for each landmark of the unordered edge pairs it fails to distinguish, and intersected the sets for every unordered pair, triple and four-set of landmarks. Empty intersections give exactly zero resolving pairs, triples only at n=10 (160), and four-set counts 141, 224, 590, 1644, 2380, 7536, 5202, 21600, 11308 and 42768. All stated witnesses resolve. Monotonicity excludes sizes below two and makes these minima 3 at ten and 4 at each other tested index. Checking all 40 shift/reflection/layer-swap permutations against the actual edge set and applying them to the six displayed triples gives disjoint sets of sizes 20,20,40,20,40,20 in representative order, exactly exhausting the resolving triples. The all-index corollary is the disjoint union with Iqbal et al., Theorem 1 on n≥13 as cited; the independent finite replay does not prove that tail. That primary theorem's full passage and exact graph definition were not independently recovered, so tail scope is taken from the specific citation and excerpts in the frozen evidence, not represented as an independently verified proof.

## originality

PASS

Credit the published parity-tail law rather than calling it new. The supported distinct work is the resolved initial range, in particular the tested failure at six and the first onset at ten, plus the exact small-set counts and six specified-subgroup orbits. The corresponding primary paper is highly relevant and excerpts in the frozen evidence identify its restricted theorem; lawful attempts did not recover its full text independently. The scope evidence and actual finite counts do not warrant treating the unqualified abstract parity pattern as a theorem for all orders. No accessible independent exact initial census was found; this is not a blanket priority claim.

## value

PASS

The finite range is forced by the break in the published tail, not chosen arbitrarily. The missing cases decide the true first occurrence of three landmarks and invalidate parity extrapolation at six. Counting all small resolving configurations and separating the exceptional optimal triples into complete subgroup orbits adds usable information about sensor choices unavailable from the dimension alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
