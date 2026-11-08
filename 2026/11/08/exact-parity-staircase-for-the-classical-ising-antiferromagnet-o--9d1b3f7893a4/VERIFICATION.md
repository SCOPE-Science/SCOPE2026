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

# Verification and limits

The exact row-decomposition identity, parity minimization and the existence of regular graphs and Eulerian orientations constitute the all-order proof. The standalone `check.py` independently constructs the full graph from ordered pairs, enumerates all spin subsets for \(n=3,4,5\), computes maximum cuts by magnetization sector, and verifies the piecewise energies and off-transition magnetizations on a half-integer field grid. A successful run reports 80 assertions. This is finite corroboration, not a replacement for the proof.

All graph edges are uniformly coupled; no thermodynamic-limit phase transition, finite-temperature result or complete critical-state multiplicity formula is asserted. Independent audit has not been performed.
