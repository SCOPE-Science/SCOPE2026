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

Run `python3 verify_exact.py` followed by `python3 verify_independent.py` from the directory containing these files. Both scripts require only the Python 3 standard library.

The exact program enumerates the 42 tableaux as linear extensions, constructs every admissible event up to four fixed labels, deduplicates its Boolean incidence columns, forms 42-by-42 integer Gram matrices, and computes their ranks using fraction-free Gaussian elimination. It also verifies the 24-supported cubic alternant and the explicit nonzero four-event witness. Output was: degree 0 to 4 ranks 1, 11, 31, 41, 42; signed witness 1; `VERIFY_EXACT_OK`.

The independent program enumerates the tableaux via growth of three-row Young shapes, constructs observation columns by fixing cells instead of labels, and computes modular ranks over the primes 1000003, 1000033, and 1000037. It returns 1, 11, 31, 41, 42 in each field and `VERIFY_INDEPENDENT_OK`.

A modular rank is a lower bound on rational rank; it alone is not a proof of equality. Equality of the finite ranks follows from exact integer Gram elimination in the first program. The cubic upper bound also has the explicit signed cancellation proof. Neither method proves an infinite-family theorem beyond the shape considered. The external independent audit has not been performed.
