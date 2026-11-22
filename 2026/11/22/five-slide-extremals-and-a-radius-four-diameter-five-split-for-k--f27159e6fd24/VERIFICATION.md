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

# Reproducibility

From this directory run:

```
python3 verify_slide_orbits.py > orbit_replay.json
python3 verify_independent.py > independent_replay.json
```

Compare parsed JSON against `orbit_output.json` and `independent_output.json`; both contain `"status":"PASS"`. Each checker uses only the Python 3 standard library and independently computes the legal three-token moves and exact reachability layers on \(\operatorname{KG}(n,2)\) for \(8\le n\le12\). The second also performs the original neighborhood-observation and propagation procedure on all candidate selections with at most three vertices for \(n=8,9,10\).

The all-order inference is mathematical rather than an assumption of stabilization: any source-target pair uses at most twelve base labels, and the relabelled order-twelve path remains valid at every larger order. Exact degree formulae are also checked against every state for every certified order. No performance-dependent timeout is used as evidence. These computations support the claimed finite certificate; they do not constitute independent external auditing.
