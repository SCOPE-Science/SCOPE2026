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

Run `python verify_funk_pentagon.py` with Python 3.9 or newer; the checker uses only the standard library and prints `CHECKS_PASS 1353`. It directly constructs all five complex columns and the full Gram matrix for eleven interior latitude values; compares diagonal and off-diagonal entries with the stated exact formulas; tests inversion on random complex coefficients; checks 1,000 positive latitude parameters against the stated optimum; and separately integrates nine trace-free quadratic examples over perpendicular great circles.

The computer checks are finite tests only. The proof of the exact five-eigenvalue spectrum, all admissible latitudes, the uniqueness of the minimizer, the coincident lower-frame optimum, and the inverse formula is given in `RESULT.md`. The numerical checker does not certify algebraic identities for all real parameters or provide a general-purpose arbitrary-view optimization theorem.

Independent audit and independent validation have not been performed.
