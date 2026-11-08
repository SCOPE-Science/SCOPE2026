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

Run `python3 verify.py` in the directory containing this file. The verifier uses only the Python standard library and computes integer binomial coefficients modulo the exact target modulus. It checks the signed theorem for finite prime powers and many exponents (both odd and even), and independently checks that even-exponent sums coincide with unsigned sums. A successful run prints `VERIFY_OK` with case counts.

The proof in `RESULT.md`, especially the valuation of nonlinear binomial terms in its induction, is the justification for unbounded exponents. A finite computation is not an infinite proof. The published comparison with one relevant 2017 paper remains text-limited; no independent audit has been undertaken.
