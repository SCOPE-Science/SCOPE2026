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

# Reproducibility

Run `python3 verify.py` using Python 3.9 or later and no nonstandard dependencies. The program compares two constructions of Apéry values for every integer parameter from \(8\) to \(1500\), checks minimum-coin lengths through \(10000\), and independently reconstructs gap membership and the entire pseudo-Frobenius set for every parameter from \(8\) to \(110\). It asserts all checks and prints `ALL_TESTS_PASS` only on success.

The infinite classification follows from the symbolic argument in `RESULT.md`; no finite enumeration is used as a substitute. No independent audit has been performed.
