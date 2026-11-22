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

# Verification notes

The supplied `check_hansen.py` is self-contained Python 3, uses only the standard library, and recomputes the finite distance histograms directly from independent sets and signed Hansen vertices. It separately computes the four-state transfer and coefficients of the rational third-order recurrences, compares all coefficients and total pair counts through \(n=12\), and checks the limiting moments at \(n=50,100,200\) by exact integer moment propagation.

Run with `python3 check_hansen.py` from the extracted package directory. The observed result was `HANSEN_PATH_CHORD_PASS: enumerated n=0..12; independent transfers, cubic recurrences, and asymptotic moments checked`. The infinite result follows from the written transfer-matrix and Perron-eigenvalue proofs, not from a finite exhaustion. No independent external audit was performed.
