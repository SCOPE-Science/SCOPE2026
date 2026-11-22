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

# Reproducibility checks and their limits

Run `python3 verify.py` alongside the supplied text files. The script requires only Python's standard library and uses integer and modular-inverse arithmetic. Its checked outcomes are: 120,000 direct rational-base digit-parity versus auxiliary-word comparisons, 30,000 signed pair-sum comparisons, 10,000 identity checks per oriented transition, and 18 complete exact CRT drift chains including size bounds.

These are finite consistency and reproducibility checks. The infinite upper bound follows from the exact contracting recurrence for the signed defect, and the infinite optimality statement follows from the CRT construction for an arbitrary positive number of steps, both fully proved in `RESULT.md`. The checks do not determine priority beyond the cited literature. Independent external scientific review or certification has not occurred.
