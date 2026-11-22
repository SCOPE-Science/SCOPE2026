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
# Verification and reproducibility

Run `python3 checks/check_unicyclic.py` with Python 3.10 or later; there are no nonstandard dependencies. It derives each incidence-support indicator directly from the graph edge bits, computes an independent in-place integer Walsh–Hadamard transform and checks every computed coefficient against the formula. It additionally checks exact maximum and least strictly positive magnitudes and the closed unicyclic rank for every \(2\le n\le8\) and all \(1\le j\le n\). The current run completed 2,009,837 exact arithmetic assertions successfully. The all-length proof is algebraic, not a computational extrapolation. No external independent validation has been performed. Historical priority and all-root classifications at higher excess are beyond the verification claim.
