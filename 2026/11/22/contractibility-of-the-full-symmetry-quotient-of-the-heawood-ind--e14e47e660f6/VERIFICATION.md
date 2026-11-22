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

# Exact computational verification

Run `python3 verify.py` from the directory containing this file. Python 3.10+ and SymPy are required. The program regenerates the graph and all 21 incidences, its full 336-element graph automorphism group, its 457 nonempty independent subsets, every barycentric simplex and orbit, and six exact integer boundary matrices. It checks every \(\partial^2=0\), all Smith factors and all quotient homology ranks; a nonunit or unexpected invariant aborts execution. It then constructs a spanning tree and verifies that the 149 triangular attaching words eliminate all 51 fundamental-group generators by unit relators.

Observed successful output:

```
HEAWOOD_FULL_AUTOMORPHISM_ORBIT_CONTRACTIBLE_OK
independent_sets=457 automorphisms=336 quotient_cells= [14, 64, 149, 218, 210, 120, 30]
integral_boundary_ranks= [13, 51, 98, 120, 90, 30] all_nonzero_Smith_entries=1
pi1_spanning_tree=13  generators_killed=51  triangular_relators=149
```

All calculations are exact finite enumeration and integer reduction, not Monte Carlo and not extrapolation to higher-order incidence graphs. The final homotopy conclusion uses Hurewicz and Whitehead after the finite cellular proof. The verification is reproducible but has not been independently audited.
