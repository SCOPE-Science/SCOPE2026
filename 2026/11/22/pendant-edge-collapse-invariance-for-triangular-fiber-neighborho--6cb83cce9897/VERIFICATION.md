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

The universal claim is proved by the explicit free-face argument in `RESULT.md`, not by finite extrapolation. The standalone standard-library script `verify_leaf_collapse.py` constructs neighborhood faces directly from graph adjacency, executes every stated triangle-edge and cone pair, checks that each smaller simplex has exactly the asserted unique coface at removal time, and compares the terminal face set exactly with the smaller graph's neighborhood complex.

The recorded execution is in `verification_output.txt`: 320 leaf-attached graphs, 22,080 individually checked elementary pairs, 11 path-homology cases, and a four-color counterboundary comparison. The recorded counts are those actually printed by the script. No independent audit has been performed. Full enumeration in these cases does not establish the unrestricted theorem; its argument is in the proof.
