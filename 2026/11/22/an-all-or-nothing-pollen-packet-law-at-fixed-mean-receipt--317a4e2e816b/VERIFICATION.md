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

From the result directory, run `python3 verification/check_packet.py` with any current Python 3 implementation. The script uses only the standard library and completed 143276 deterministic diagnostic assertions. It checks exact rational monotonicity of the normalized-difference coefficients, compares all intermediate packet sizes against the optimal endpoints across a large finite grid, brackets exact crossover values at four threshold sizes, and checks the approach to the normal-quantile asymptotic.

# Analytical limits

The exact infinite-domain claim is established by the proof in RESULT.md, not by the finite tests. The mathematical conclusions depend on independent Poisson arrivals of uniform packets under a fixed *expected* delivered-grain budget and an all-or-none event. No empirical validation, broad generalization, or independent mathematical audit was performed.
