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

# Verification and reproducibility

Two standalone files are included: `verify_signed.py` and `verify_geometry.py`. Run each with `python3`; both require only the standard library. `verify_signed.py` explicitly evaluates all \(2^{16}\) subsets of sixteen even-parity vectors, all \(1920\) even signed permutations, and all their actions on the admissible support masks. `verify_geometry.py` independently derives the same 16-curve intersection graph from blowup divisor classes, generates the full Weyl group using Picard-lattice reflections, recovers each signed type from five pairs of conic-pencil classes, and verifies the recorded 18-row table. Each program was executed on its actual saved source file with success.

The proof's non-computational ingredients are explicit: smooth quartic del Pezzo curves are the sixteen specified \((-1)\)-curves; negative-definite subsets are disjoint supports; rational supports descend through the given divisor \(D_B=-K_S+2B\). The programs do not prove universal finite-field existence of every signed type, and no independent mathematical audit is claimed.
