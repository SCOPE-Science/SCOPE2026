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

The standalone script `verify.py` builds the graph directly and enumerates all potential vertex-selected sets for \(4\le n\le6\). Its geodesic test uses breadth-first shortest paths independently of the component decomposition; the counted polynomials are computed separately by a labelled component recurrence. Executing `python3 verify.py` produced:

```
n=4 geodesics=12 transversals=30 minimal=11 omitted-edge_counts={2: 3, 3: 8}
n=5 geodesics=60 transversals=131 minimal=15 omitted-edge_counts={4: 15}
n=6 geodesics=180 transversals=712 minimal=91 omitted-edge_counts={3: 15, 4: 60, 5: 6, 6: 10}
VERIFY_OK n=4..6 masks=33856 geodesics=252 valid_transversals=873 inclusion_minimal=117 BFS=PASS original_P4_equivalence=PASS two_EGFs=PASS
```

The finite sweep establishes only these finite cases. The unrestricted formal-series identities require the graph-theoretic proof in `RESULT.md`. Source comparison supports provisional originality, not a guarantee of priority or an independent audit.
