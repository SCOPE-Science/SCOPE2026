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

# Finite verification and logical scope

Run `python3 cycle_recoloring_systole_verify.py` from the directory containing this file. It uses only the Python standard library. The script checks actual target-cycle graph-homomorphism coloring adjacency, rather than assuming the token formula; constructs the asserted positive generator loop; and uses signed-voltage breadth-first search to confirm six manageable shortest nonzero-winding loops.

Recorded output from executing the embedded script:

```
(m,n,r)=(4,5,2): coloring vertices=30, shortest witness=20, exhaustive signed-voltage BFS: length=20, states=59
(m,n,r)=(6,5,3): coloring vertices=100, shortest witness=30, exhaustive signed-voltage BFS: length=30, states=198
(m,n,r)=(7,5,1): coloring vertices=35, shortest witness=35, exhaustive signed-voltage BFS: length=35, states=69
(m,n,r)=(8,6,1): coloring vertices=48, shortest witness=24, exhaustive signed-voltage BFS: length=24, states=47
(m,n,r)=(8,6,4): coloring vertices=420, shortest witness=24, exhaustive signed-voltage BFS: length=24, states=414
(m,n,r)=(9,5,2): coloring vertices=180, shortest witness=45, exhaustive signed-voltage BFS: length=45, states=359
(m,n,r)=(10,6,2): coloring vertices=270, shortest witness=30
CYCLE_RECOLORING_SYSTOLE_CHECKS_OK
```

BFS explores finitely many signed-displacement states and is exhaustive only for the indicated individual finite inputs. The first four steps of the main proof establish the infinite all-parameter result; no extrapolation from the examples or any independent certification is asserted.
