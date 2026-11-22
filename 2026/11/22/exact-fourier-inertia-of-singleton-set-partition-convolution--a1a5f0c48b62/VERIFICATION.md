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

The independent character-sum and restricted-growth-string reconstruction in `check_singleton.py` was run using integer arithmetic. It produced `PASS: 12652 exact assertions; direct enumeration through n=11; all sign classes through n=90`.

The executable uses only the Python standard library. It verifies the full Walsh spectrum for every \(1\le n\le11\), independent direct Walsh character sums for \(1\le n\le7\), the Bell-moment formula and sign classification through \(n=90\), and the strict inequality underlying the infinite tail proof. Computations through finite \(n\) are reproducibility checks; the proof of all \(n\) is the elementary Poisson-summand comparison in `RESULT.md`. No external independent review has been performed.
