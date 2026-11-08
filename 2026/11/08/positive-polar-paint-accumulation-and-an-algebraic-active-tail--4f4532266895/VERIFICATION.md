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

# Verification notes

The mathematical argument and its validity limits appear in `RESULT.md`. In this package, `verify.py` uses only Python standard-library arithmetic and regenerates the Laplace transform from the backward-generator decaying eigenmodes with prescribed hit-color boundary conditions. It checks 297 finite deterministic parameter/asymptotic assertions and returns a maximum relative discrepancy under \(1.1\times10^{-14}\) on the tested grid.

Run `python verify.py` after extraction. The test is a consistency check, not a proof of complete monotonicity, strict positivity, or the infinite-time \(t^{-1/2}\) asymptotic; those conclusions rely on the Bernstein-function and Tauberian arguments. The passive endpoint identity is prior work, not a new independent confirmation.
