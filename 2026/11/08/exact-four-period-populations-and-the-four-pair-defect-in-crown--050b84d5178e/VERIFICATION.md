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

# Reproducibility checks

Run `python3 verify_dynamics.py` and `python3 verify_phases.py` with Python 3 and no third-party libraries. Their reference standard outputs are provided as `dynamics_output.txt` and `phases_output.txt`. These scripts were actually executed from extracted package files. The first is a full state-space check at \(n=3,4,5,6\); the second enumerates the independent local phase constraints at \(n=3,4,5\). The mathematical proof, rather than these finite checks, covers all \(n\ge3\). Independent external validation has not occurred.
