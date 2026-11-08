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

# Reproducible checks and scope

Run `python3 check_adjacent_stretch.py` with the package files together. The program uses Python's standard library only, enumerates all normalized half-integer potentials on the exact feasible coordinate grid for \(N\in\{4,5,6\}\) and \(t\in\{1,3/2,2\}\), and retains precisely those whose tight graph is connected. It gives:

```
EXACT_VERTEX_ENUMERATION_PASS: 9 cases
ALL_ADJACENT_STRETCH_CHECKS_PASSED
```

The checked counts, for \(N=4,5,6\) respectively, are \((14,18,12)\), \((30,46,28)\), and \((62,102,60)\), with triples ordered by \(t=1,3/2,2\). Each coordinate at a vertex is a sum of edge lengths along a tight spanning tree from the basepoint, so the half-integer search grid is exhaustive for these particular rational inputs, not an approximate grid. For arbitrary real \(t\) and unbounded dimension, validity rests on the exact tight-graph classification in `RESULT.md`, not on finite enumeration. No external independent audit is represented.
