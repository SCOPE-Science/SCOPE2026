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

# Verification summary

Run `python checks/verify.py` from the extracted package root with standard Python 3. No external packages are needed. The saved output is `checks/output.txt`, with terminal marker `RIM_DELETION_HOMOLOGY_CHECK_PASS`.

The checker independently constructs the cyclic rim-fault Möbius graph and the twisted-corner ladder; exhaustively enumerates all independence faces for \(4\le n\le10\); calculates reduced simplicial boundary ranks over \(\mathbb F_2\); tests the graph-fold neighborhood inclusions in the ladder and link graphs; verifies the four-fold link recurrence by full graph adjacency comparison; and checks primitive maximal-face witnesses for \(n=7,11,15\).

This is finite corroboration. The unrestricted integral claim is proved by explicit graph folds, relative integral chains and a primitive homology map in `RESULT.md`, not by extrapolation or mod-two torsion detection. No external mathematical audit has been performed.
