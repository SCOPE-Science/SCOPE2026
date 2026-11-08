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

# Verification evidence

The accompanying `checker.py` was executed against the packaged mathematical definitions. SymPy symbolically recomputes the zero-mean trigonometric polynomials, two exact return coefficients, two original-time period coefficients, squared-radius constants and stability signs. SciPy numerical integrations locate the positive-section periodic orbit near both equilibria for detuning \(2\cdot10^{-5}\), with measured period-drift ratios 0.9999896884 and 1.0000347870 compared with the derived leading constants. The corresponding section-radius ratios are 0.9957472190 and 1.0021028818. These ratios are expected to converge to one as detuning tends to zero.

The analytical proof in `RESULT.md`, not the finite integrations, establishes the two asymptotic expansions for all sufficiently small positive detunings. The coordinate normalizations, boundary directions and limits are stated there. No full global-period claim, independent audit or external certification is asserted.
