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

# Verification
The embedded `verify.py` (Python standard library only) reads `matching.json` in the same directory, enumerates all diameter-at-most-two simplices of the four-cube, constructs antipodal orbit cells, establishes unique proper face incidences, checks the full acyclic 76-pair matching, and verifies exactly four relative three-dimensional critical cells. It also computes signed cellular boundary ranks modulo 2 and 3 independently. Run `python verify.py` and require the line `ALL_VERIFY_OK`. Finite computation is exhaustive for this specific 16-vertex complex; it is not a proof of an infinite-family statement. The homotopy argument uses the relative discrete-Morse theorem and the elementary fact that the universal cover of real projective three-space is the three-sphere. The arithmetic checks do not establish independent external validation.
