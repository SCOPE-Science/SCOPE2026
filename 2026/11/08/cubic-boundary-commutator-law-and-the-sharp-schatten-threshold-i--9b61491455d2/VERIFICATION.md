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

The exact polynomial block identity was reconstructed from the Jacobi three-term recurrence. The packaged `check.py` recomputes matrix entries from Gaussian quadrature for several weights, orders and angular frequencies and checks the exact commutator against the formula in `RESULT.md`. It also checks the expected cubic high-frequency coefficient for two polynomial symbol pairs, with 264 assertions in total.

Run: `python check.py` (requires NumPy and SciPy). Expected output:

`POLY_BERGMAN_COMMUTATOR_CHECKS_PASS 228`

`POLY_BERGMAN_GENERAL_JETS_PASS 264`

The analytical proof, rather than finite tests, establishes the infinite-order asymptotic, the singular-value counting law and the Schatten threshold. The calculation assumes fixed order and fixed weight. No independent mathematical audit or external certification has been performed.
