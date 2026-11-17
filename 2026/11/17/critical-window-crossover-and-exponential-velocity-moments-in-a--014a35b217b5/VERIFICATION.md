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

# Verification record

The exact first integral and speed-square graph were differentiated and reconstructed independently of the period integral. The proof's required nonstandard steps are the uniform moving-endpoint bounds, a separate high-speed Laplace calculation for fixed moment orders above one, and a compact-parameter domination argument for the critical moment window. Each is written with hypotheses and explicit integrable bounds in RESULT.md.

Running `python verify.py` with Python 3.10 or newer and no external packages returns `CUBIC_CENTER_CAUCHY_MOMENT_CHECK_OK`. The checker tests the first-order speed equation against its exact graph, original-time period normalization, all fixed-moment regimes, the exact geometric first moment and critical-window integrals at multiple positive coefficient pairs. The checks are deterministic finite numerical corroborations, not a machine proof of infinite limits. No independent audit has been performed.
