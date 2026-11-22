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

# Verification and limits

The theoretical certificate is the analytic Neumann-resolvent plus homogeneous-flux-corrector derivation of the exact current. The strictly increasing function \(z\mapsto z\tanh(\eta z)\) yields a strict derivative sign of the source-boundary ratio, and the ratio endpoints give uniqueness of every claimed reset-rate crossing. These analytic arguments hold over entire continuous parameter ranges and arbitrary eligible Borel source laws; no finite data are relied upon for global uniqueness.

The accompanying `verify_biased_membrane.py` is standalone Python 3 requiring NumPy and SciPy. Executing the supplied actual file yielded `PASS 877 checks: classification, endpoint laws, exact uniform threshold, independent finite-volume solver`. The script verifies biased boundary identities for discrete and mixed sources, opposite-side sign classifications, uniform half-source arcosh root formulas by independent numerical quadrature, and five independently discretized stationary elliptic problems on 120-, 240-, and 480-cell meshes. These are numerical diagnostics rather than an independent proof of all real parameter values.

Full external independent review has not been performed. The stationary-current classification does not apply to arbitrary two-sided reset sources or to flux definitions that include instantaneous reset jumps.
