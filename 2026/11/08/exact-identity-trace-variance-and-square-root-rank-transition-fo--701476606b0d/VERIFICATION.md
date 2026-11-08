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

# Reproduction and limits

Run `python3 verify_tt_identity.py` from the directory containing this file and the checker. The proof uses only exact real Gaussian fourth moments and deterministic matrix algebra; NumPy is optional for seeded simulation cross-checks.

The bundled check run returned `VERIFY_OK 1510 exact/simulation checks`. Exact rational checks covered the two-core and three-core closed expressions, the rank-one product-Gaussian formula, positivity of the Frobenius-normalized risk above the unstructured Gaussian constant, and monotonic risk reduction under increasing bond rank. Finite large-parameter comparisons checked the two limiting formulas. Optional seeded tests directly assembled random Gaussian cores and compared observed norm-square variance with the exact recursion at three parameter settings.

The program does not prove the assertions for infinite parameter sets; the universal argument is in `RESULT.md`, via the two-invariant conditional fourth-moment recursion and the leading eigenvalue of the transfer matrix. Random-sampling fluctuations affect optional Monte Carlo comparisons, not the exact algebraic identities. No independent audit or certified floating-point stability study was performed.
