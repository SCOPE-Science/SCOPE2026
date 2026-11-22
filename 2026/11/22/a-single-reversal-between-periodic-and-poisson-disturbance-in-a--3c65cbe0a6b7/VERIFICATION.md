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

The theorem is based on exact renewal-reward identities, explicit stage probabilities and a strict monotonicity argument for logarithmic elasticity. `check.py` is a standalone Python 3 numerical and rational diagnostic using only the standard library. Its complete replay reports 12,924 passed assertions, including 8,064 rational stationary-balance identities, separate integration tests and randomized parameter crossovers.

The checker tests finite parameter examples only; uniqueness for every positive rate pair is established by the proof of strict decrease of \(r(x)\) in `RESULT.md`. No external audit or field calibration has been conducted. Source access limitations are described in `REVIEW.md`.
