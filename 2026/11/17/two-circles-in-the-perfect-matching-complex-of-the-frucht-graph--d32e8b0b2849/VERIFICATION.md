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

The cyclic edges and signed chord list give the cubic 12-vertex, 18-edge Frucht graph. Independent code reconstructed and enumerated it without running the frozen verifier: both least-unmatched-vertex branching and exhaustive cardinality-six subset filtering yield the facet masks 168481,150561,166026,140554,74290,35026,9554,84108. The face counts by cardinality, including zero, are (1,18,88,147,118,48,8); all facets have dimension five. The 117 ordinary disjoint pairs can also be counted as binom(18,2)−12 binom(3,2), while exactly 88 appear in the perfect-matching complex, leaving 29. Its eight full simplicial facets cover it, with each nonempty intersection a simplex, so the finite simplicial nerve theorem applies. Two independent constructions of the nerve give (1,8,25,22,7,1). The 26 proposed collapse pairs were transcribed, not rediscovered, and each was verified against the complete surviving face set as a codimension-one pair with a unique strict coface. The final connected graph has five vertices and six edges, and contracting a spanning tree gives the integral two-circle homotopy type. In particular nonzero reduced H1 contradicts the top-degree-only homology of a pure shellable complex of dimension five. Replay the independent check at /workspace/branches/2bc5ef84-6e19-421d-97b5-d9b794e7786f/frucht_independent_check.py; output is frucht_independent_check.txt beside it.

## originality

PASS

The exact perfect-matching extendibility topology on this particular graph is the distinct claim. The inspected exact same-graph results are for the strictly larger ordinary matching complex, and the inspected same-construction classifications and computations do not cover this graph. Neither classification of the ordinary complex nor enumeration of perfect-matching counts alone implies the topology or even the incidence count of extendible pairs.

## value

PASS

The Frucht graph is a canonical small cubic graph with trivial automorphism group, in contrast to symmetry-driven families previously studied for perfect matching complexes. Its extendibility topology is demonstrably different from its known ordinary matching topology: enforcing global completion changes a wedge in degree three to a free rank-two fundamental group despite a pure five-dimensional complex. The full exact collapse and 29-pair obstruction make this a useful comparison example for extendibility and nonshellability, not simply an isolated count of matchings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
