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

## Reproducibility

From the directory containing `verify_bfs.py` and `verify_direct.py`, run:

```
python3 verify_bfs.py
python3 verify_direct.py
```

The first program performs exhaustive reachable subset-pair breadth-first search, with the full-state product as its root and every pair of singletons accepted. It checks the exact common reset threshold for each \(4\le n\le16\), not just that a proposed word resets. It reported `BFS_OK` and the thirteen expected thresholds \(10,17,25,37,50,64,82,101,121,145,170,196,226\).

The second program separately applies the explicit words to **each** starting state in both factors for every \(4\le n\le70\), checking each formula and intermediate-image assertion. It reported `DIRECT_OK n=4..70`.

Neither finite verification is an exhaustive check of every integer \(n\). The unbounded quantifier is discharged by the modular single-factor argument, the interval-image induction and the three-state case split in `RESULT.md`.

No independent audit has been performed.
