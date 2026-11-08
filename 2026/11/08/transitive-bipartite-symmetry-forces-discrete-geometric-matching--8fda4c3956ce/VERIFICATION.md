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
Run `python3 verify.py` with Python 3 standard library only. The program enumerates invariant bipartite graphs, their ordinary rook-matching faces, and their fixed faces for shore-transitive actions. The expected fixed points are computed independently from admissible edge orbits. For the complete equal-shore cases it independently checks the group centralizer count.

Saved replay:

```text
ALL_VERIFY_OK actions 28 invariant_graphs 226 valid_orbit_samples 421 group_sizes_sum 976
CENTRALIZER_VERIFY_OK degrees_1_to_6
```

This is exhaustive for the listed 28 actions and 226 invariant graph choices, not for all groups, dimensions, or graphs. The unrestricted theorem rests on the orbit-projection proof. Integral homology follows from the proven discrete topology.
