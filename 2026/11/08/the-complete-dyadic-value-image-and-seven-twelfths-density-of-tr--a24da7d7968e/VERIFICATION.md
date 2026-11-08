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

# Reproducibility and scope

Run `python3 verify_tribonacci_dyadic.py` with Python 3.10 or newer; only the standard library is needed. The verifier constructs the critical matrices, checks the analytic Mahler coefficients, computes a finite projection of the critical value, and independently enumerates all target fibers modulo powers of two through exponent fourteen. Successful output begins `VERIFY_OK levels=14 target_fibers=32766` and includes the checked image-size sequence and the critical residue 1264 modulo 2048.

The proof in RESULT.md establishes the result for all exponents. Finite enumeration has no independent-certification status. The computed critical value is a finite projection of an implicitly defined exact \(2\)-adic constant, not an assertion that the constant is an ordinary integer.
