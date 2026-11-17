---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Any selected pair at underlying cyclic distance 2..2r has an outside-or-selected common neighbor on a shortest arc, forcing a closer selected pair under threshold-two convex closure, ultimately adjacent cyclic vertices; r>=2 then forces both outer neighbors repeatedly and hence the full cycle. Conversely, separated selected pairs have distance >2r, so any outside vertex cannot have two selected neighbors by metric triangle inequality. Ordering k>=2 selected points around labelled C_n gives all positive gaps >=2r+1, with weak compositions and n/k unmarking giving the binomial coefficient. n small and complete powers correctly give only empty/singleton/full; r=1 has a C7 counterexample. Independently enumerated all subsets n3..18 selected radii and matched adjacency definition and polynomial; proof is universal.

## originality

PASS

Dourado–Grippo–Lin–Protti 2026 full manuscript proves general complexity, generic exact algorithms and special tree/threshold cases, but not cycle-power structural characterization. González–Grippo–Safe 2020/2021 full arXiv text studies caterpillars/unit interval graphs; its cited 2-connected chordal pair-hull result covers analogous path powers but not nonchordal cycle powers such as C6². Prior antiprism/cyclic prism P3 results concern different graph families. No dominating polynomial identified after checking threshold-two bootstrap and cyclic packing equivalent formulations, with residual hidden-prior risk.

## value

PASS

Complete natural P3-convex set classification and all-cardinality polynomial on a nonchordal infinite two-parameter cycle-power family, reducing convexity to cyclic packing geometry. It gives meaningful counts beyond general algorithms or a scalar hull number and sharp r=1 boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
