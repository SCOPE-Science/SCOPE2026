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

The renewal-resolvent proof determines the exact stationary density, its derivative jumps, its strictly monotone exterior branches, and every possible critical point in the interior interval. These arguments apply for all parameter values in the stated open domain, including the boundary equalities in the modal partition.

The standalone Python checker `CHECK.py`, with `scipy>=1.11`, was executed and returned `PASS 516 deterministic checks`. Numerical integration compared the piecewise formula with normalized resolvent constraints, and comparisons checked endpoint derivatives, the critical separation, and both parameter branches. Computation is corroboration, not the proof of completeness or novelty. The publication-comparison limitations described in REVIEW.md remain; no independent audit is claimed.
