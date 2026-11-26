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

For a connected bipartite graph, omitted opposite-side vertices have opposite distance parity from every vertex, so an equalizer contains a whole class. For two omitted vertices in the same class of a tree, the projection of a candidate witness to their path must be its midpoint. If this midpoint is in the selected class it is itself a witness; if not, any third branch gives a neighbor in the selected class. The only remaining obstruction is a degree-two midpoint in the unselected class. Its distance to either endpoint is at least two by parity, so neither neighbor is a leaf. Conversely, a degree-two vertex of the unselected class with two nonleaf neighbors is the unique equalizer of the two vertices obtained by continuing one step out each way, so the selected class fails. This covers both a singleton complement and equal part sizes. Parity determines all size-minimizers when the bound is attained, and upward closure plus inclusion–exclusion gives exactly the stated all-set family and polynomial when both classes work. Independently enumerating subsets on P4, P5, and K_{1,3} confirmed the two directions, including P5 (dimension 3 versus bound 2; the midpoint of the endpoints is the unique witness). On P4 the exact counts are 2z²+4z³+z⁴. Replay: /workspace/branches/95c11748-460e-41a7-b023-f3cc976a380f/independent_tree_equalizer_check.py. The frozen checker sources were inspected, not executed; the universal result is proved by the midpoint argument rather than by finite checks.

## originality

PASS

The bipartite bound and simple midpoint obstruction are prior. The all-tree local converse and consequent simultaneous all-cardinality characterization were not found in the inspected statements. This is qualified, not absolute priority.

## value

PASS

Distinguishes exactly which tree classes achieve a foundational lower bound by a local test implementable in linear time. On a broad unbounded tree family (including every reduced tree), the answer classifies every equalizer by inclusion and cardinality using only the part sizes. This is useful structural information even though it does not compute the dimension for arbitrary trees outside the sharpness regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
