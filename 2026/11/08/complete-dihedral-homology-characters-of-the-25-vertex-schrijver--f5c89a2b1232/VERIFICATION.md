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

The executable `verify.py` enumerates 25 stable four-subsets, 60 disjointness graph edges, all 19,907 independent faces including the empty one, checks each Hasse cover against a deterministic acyclic matching, builds a 16-term integral degree-three cycle and a boundary-annihilating projection, and computes signed Lefschetz traces for all ten rotations and ten reflections. Its stdout is in `verification_output.txt`.

The exact finite certificate establishes the homology action on this single simplicial complex, not a general family or independently audited priority claim. The prior nonequivariant sphere-wedge theorem is acknowledged as already known.
