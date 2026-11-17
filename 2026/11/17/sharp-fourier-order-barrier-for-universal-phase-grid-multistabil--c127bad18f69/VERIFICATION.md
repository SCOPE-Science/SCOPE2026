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

# Reproducible verification

Execute `python3 verify.py` using the Python 3 standard library; no external packages or downloads are required. The recorded run printed `PASS: 34631 grid configuration/Jacobian tests and all checked root-sums`. The test exhausts grid labels for each integer network size from 2 through 6 and each grid cardinality from 2 through 7, checks the vector field and all Jacobian entries numerically, and checks trigonometric root-sums for each lower harmonic index in those finite ranges.

These are finite consistency checks, not a proof at arbitrary sizes. The general proof relies on exact two-cluster dynamics, the finite Fourier identity and classical gradient-flow/covering arguments. No independent mathematical audit was performed.
