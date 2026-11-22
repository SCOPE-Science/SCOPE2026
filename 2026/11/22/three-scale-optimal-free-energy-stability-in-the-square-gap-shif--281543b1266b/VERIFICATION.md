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

# Verification and reproducibility

Run `python verify.py` with Python 3 and `mpmath` installed. The script constructs its numerical partition functions directly from the return lengths \(j^2+1\) and alternates between a convergent direct sum and the modular theta transformation depending on the argument.

Checks executed against the packaged script:

- Four independently compared modular theta/direct-series values at positive arguments.
- Eight high-precision pressure roots with the equation \(Z(p_L)=e^L\), eight exact pressure-envelope equalities, and eight return-variance calculations.
- 408 finite candidate comparisons of the stability quotient with the alternating-orbit lower bound.
- Seven independently solved global-stationarity equations, with small residuals, strict improvements over the alternating-orbit quotient, and convergence tests for the density and the sharp second-order correction.

The precise asymptotic conclusions for infinitely large \(L\) depend on the proofs of entropy-envelope curvature, global maximizer concentration, the stationary equation, and a uniform two-return expansion. A finite parameter scan cannot establish a global maximum or a little-oh remainder. Numerical comparisons are diagnostics, not independent mathematical validation.
