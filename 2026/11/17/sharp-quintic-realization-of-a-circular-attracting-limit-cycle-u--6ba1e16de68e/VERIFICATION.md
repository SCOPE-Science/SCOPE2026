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

The exact polynomial and all-parametric cofactor identities were independently expanded with symbolic polynomial arithmetic in `verify.py`. In particular, the two identities establish tangency to both prescribed circles without numerical tolerances. The degree-five and Kolmogorov-axis checks are algebraic. For the rational example, the code evaluates the original cofactor-period integral and the sign-definite paired integral at 55-digit precision and verifies their agreement; the computed transverse Floquet multiplier is approximately `0.9557320976678860489632374`.

The proof of strict attraction for every parameter under the theorem's hypotheses is analytic; the finite numerical trial is not presented as a universal proof. The nonexistence at polynomial degrees three and four is an explicitly cited prior theorem rather than a checker-derived impossibility certificate. Degree one and two are standard classical restrictions for Kolmogorov fields. Further historical-priority investigation of older comprehensive prescribed-circle treatments remains useful. Independent audit and independent mathematical validation have not been performed.

Reproduction: `python -m pip install sympy mpmath` followed by `python verify.py` in the directory containing the complete extracted files.
