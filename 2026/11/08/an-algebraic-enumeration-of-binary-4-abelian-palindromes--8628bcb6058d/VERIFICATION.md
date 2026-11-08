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

Run `python verify.py` from the directory containing this file. SymPy is required. The code builds the eight-state transition matrix directly from the four-bit factors, verifies two exact symbolic rational identities, computes algebraic generating-function coefficients, and independently compares the full length-at-most-four factor profiles of every binary word of lengths one through sixteen with the corresponding reversed words. It additionally checks the explicit boundary-and-one-imbalance characterization for each eligible word. The completed local run printed `VERIFY_OK symbolic_det_trace_gf, finite_n=1..16, words= 131070` and the coefficient list stated in RESULT.md.

The analytic root-exclusion argument and infinite asymptotic transfer are proved in RESULT.md; they are not certified by the finite enumeration. The code does not use historical files or external network resources. Independent mathematical audit has not been performed.
