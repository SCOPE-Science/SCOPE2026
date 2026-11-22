---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The theorem is established by the four-step simplicial collapse proof in `RESULT.md`: exact characterization of all newly independent faces, explicit decreasing-cardinality row and column face pairs, two fault-triangle and leaf removals per edge of \(H\), and the graph-of-spaces spanning-tree computation. Every stated removal is a genuine elementary collapse; no spectral or finite numerical extrapolation is required.

`verify.py` is standalone Python 3 using only the standard library. It constructs and checks each collapsed face pair against **all** current cofaces, compares the exact final face set with the stated core, and brute-force validates independent subsets directly against the graph adjacency rule for all labeled graphs on up to four vertices. It also tests graph extremes, cycles, multipartite graphs and seeded random patterns on five to seven vertices.

The actual invocation `python3 verify.py` returned:

```text
PASS: 134 fault-graph instances, 29108 explicit elementary free-face collapses; target complexes matched exactly.
All 74 complete instances n<=4; additional boundary, cycle, multipartite, random examples n=5,6,7.
```

These calculations establish the claimed *finite* checks, not uniqueness of the mathematical result and not any independent audit. The unrestricted statement depends on the complete elementary-collapse argument, which has separately been checked against the definitions and the relevant boundary cases.
