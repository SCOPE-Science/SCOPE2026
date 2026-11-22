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

The proof uses the recurrence and digit-product congruence in RESULT.md to establish an infinite classification, and does not interpret finite samples as a proof. `verify_run_spectra.py` is a standalone Python 3 script using only the standard library. Run `python3 verify_run_spectra.py` from the directory containing that file. It calculates the coefficients independently by an exact division recurrence and compares measured run-length frequency maps to the theorem for all primes between 5 and 101 and all depths with block size at most 15,000. The recorded independent-from-proof numerical check passed 125,867 direct index instances. This is computational corroboration only. Mathematical independent audit: not performed.
