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

# Verification and reproduction

The exact claim can be replayed using `python check_functional.py` (standard library only) and `python check_trajectory_symmetry.py` (requires `networkx`). Both programs were run against the package's 11-vertex, 18-edge graph, and both passed. The former uses 11-bit integer masks and complete functional-graph decomposition; the latter constructs the graph from an independent edge list, directly follows each of the 2048 tuple-valued state trajectories, and determines the 12 graph automorphisms.

Both runs assert 20 fixed points, 61 primitive two-cycle orbits, maximum entry time 6, 48 maximally delayed states, all displayed basin spectra and time-by-period counts. The first additionally asserts the global identity \(F^8=F^6\) and rejects \(F^7=F^5\); the second confirms 6 spatial fixed-point classes and 11 spatial two-cycle classes.

Proof scope is exactly the finite graph and exact binary rule specified in `RESULT.md`. Exhaustive computation on this complete 2048-element state space is not extrapolated to other graphs. Reproduction is deterministic; mathematical checking and historical-priority assessment remain subject to an external audit.
