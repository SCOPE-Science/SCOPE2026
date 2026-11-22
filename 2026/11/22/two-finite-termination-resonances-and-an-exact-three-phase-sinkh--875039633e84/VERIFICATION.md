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

# Reproduction and boundaries

Run `python3 verify.py` from the directory containing this file; no packages outside the Python standard library are required. Expected output: `PASS: 5605 finite exact-rational and numerical assertions`.

The script independently constructs the affinity matrices, searches the scalar balancing equation by bracketing, tests row and column sums, the exact rational mode-switch identities, the critical parameters, and a centered finite-difference Jacobian of one complete factor sweep. It also tests first-step versus two-step finite termination and a collection of non-resonant parameters. Numerical comparisons use stated tolerances; rational crossover identities are exact.

The infinite family, arbitrary positive affinity, uniqueness, and complete finite-termination classification are established by the written proof and the cited earlier at-most-two-scalings theorem, not by finite enumerations or an external proof assistant. No independent mathematical audit or exhaustive literature-priority certification has occurred.
