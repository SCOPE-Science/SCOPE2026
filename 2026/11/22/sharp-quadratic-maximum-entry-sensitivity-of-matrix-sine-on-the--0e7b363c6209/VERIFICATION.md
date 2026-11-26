---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python verify_sine_b2.py` in an environment with SymPy, NumPy and SciPy. The script checks the exact symbolic cubic rows, the two-eigenvalue diagonal-row identity and the rational bounds used in its optimization. It also checks a rational Sturm root count, interior finite-difference comparisons and 400 pseudorandom Taylor-remainder samples.

The bounds over positive band widths and all admissible matrices in the specified two-dimensional spectral problem follow from the analytical proof in `RESULT.md`, not the finite tests. The originality evidence is a qualified comparison rather than historical certainty.
