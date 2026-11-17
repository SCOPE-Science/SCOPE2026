---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Graph is defined by directed distinct K4 arcs, each adjacent to the other two arcs with same first coordinate and its reverse. The successor map is applied to the complete 3^12 functional graph: finite peeling/forward-trace exhausts every state; cycle lengths and distances are exact. Independent freshly written exhaustive iteration matched all cycle/basin counts and the 10-step/384 count. S4 injects through the four intrinsic triangles and acts by relabeling, so the permutation orbit classification is checkable from canonical cycle representatives. Original independent source code implementing S4 checked.

## originality

PASS

Best-of-knowledge original graph-specific complete temporal and symmetry classification. Classical finite-graph circulation results determine asymptotic rates/synchronization but neither 3^12 exact periods/transients nor S4 orbit partitions; related published icosahedral, Heawood and Kneser graph censuses involve other graphs. Source code inspected at assigned tree.

## value

PASS

The truncated tetrahedral graph is a canonical Archimedean skeleton with a natural S4 action. The full finite-state cycle/basin/entry census and equality of site activity for periods 4 and 8 resolve natural dynamical invariants that general circulation theorems deliberately leave undetermined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
