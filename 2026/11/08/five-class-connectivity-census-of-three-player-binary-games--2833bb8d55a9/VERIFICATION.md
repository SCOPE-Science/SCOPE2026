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

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3.8 or newer. The program enumerates all \(2^{12}\) edge orientations, not a random sample; computes the directed reachability matrix for every vertex; checks reachability again by backward graph search; tests acyclicity both recursively and by Kahn's topological algorithm; checks all \(48\) cube automorphisms, their \(112\) orbits, and Burnside's fixed sum \(5376\); and verifies the sink factorial-moment identities.

The program completed with `ALL EXACT CHECKS PASSED` on the embedded source. These finite checks prove the exact table because the finite search space and each predicate are explicitly defined. The structural claims for every orientation are additionally supported by the human-readable proofs in `RESULT.md`. No numerical simulation or extrapolation to infinitely many game sizes is used. Publication priority remains subject to coverage of unindexed sources.
