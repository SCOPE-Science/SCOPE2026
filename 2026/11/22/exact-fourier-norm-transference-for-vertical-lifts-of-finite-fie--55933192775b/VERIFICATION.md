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

Run `python3 CHECK.py` with Python 3 and no third-party packages. The checker directly forms every Fourier coefficient of each tested finite-field support and independently computes pair-sum additive energy, comparing these to the stated transfer formula. It covers six prime fields and one degree-two extension field. The observed output is `PASS 100 independent norm and energy comparisons including F9`.

These floating-point experiments are supplementary. The infinite family of odd prime powers and the asymptotic conclusions are established only by the proof in `RESULT.md`. The finite checker does not assert a formal certificate, or any independent external mathematical audit.
