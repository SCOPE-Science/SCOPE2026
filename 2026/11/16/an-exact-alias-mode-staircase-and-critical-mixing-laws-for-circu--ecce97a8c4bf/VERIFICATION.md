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

# Verification information

Run `python3 CHECK.py` in the extracted directory. Only Python standard library is required. The same-file script executed and passed 311 finite checks, including exact adjacent-switch comparisons, Hilbert-space normalization of the explicit extremizer, periodic interpolation equations and the fixed-index two-mode transition profiles. The checker is not an infinite proof: critical analytic steps are in RESULT.md, including the explicit all-alias geometric tail bound and uniform Stirling estimates.

Exact assumptions: integer \(N\ge2\); positive real \(\rho\); unnormalized value-one data on a regular \(N\)-gon; fixed integer transition index and real critical-window offset. The formulas do not cover growing index or arbitrary perturbed nodes. The exact finite-weight decomposition and qualitative first vacuum transition occur in older circular-coherent-state literature; only the complete all-order critical classification is assessed here. The related 2024 circular-state article was not available in full, and independent audit has not occurred.
