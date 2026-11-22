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

# Reproducibility and limits

Run `python3 transfer_check.py` alongside `direct_check.py` with Python 3 standard library. It proves the scalar recurrence by checking the first 24 Cayley–Hamilton error terms for the exact 24-state integer transfer and the corresponding eight terms of the row transfer. It checks Fibonacci and character integrality against 40 half-widths, then independently enumerates every perfect-matching-extendible face for half-widths 2, 3, and 4 and directly computes each signed Lefschetz character. Verified results: 24 states, 112 weighted transitions, eight row states, 16 weighted row transitions, and all assertions pass; the three direct checks enumerate 495, 12375 and 309480 faces. The external paper supplies the nonequivariant wedge homotopy theorem. Integer transfer correctness follows from the explicit boundary-state argument in RESULT.md, not the finite comparisons alone. An independent mathematical audit has not been performed.
