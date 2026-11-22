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

The included `check.py` independently generates all exactly-\(t\)-deletion descendants by choosing deleted positions and compares intersecting output sets with the claimed signed-rotation graph. It also enumerates all subcodes when the message universe has at most 16 vertices, verifying the exact independence number and total number of optimal subcodes. Invoke `python3 check.py` in the package directory. The all-parameter proof uses a clean aligned copy, cyclic gap enumeration, and Möbius inversion; testing is not claimed to prove infinite validity. This package has not undergone independent mathematical audit.
