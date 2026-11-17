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

# Reproducibility and limits

`RESULT.md` supplies a self-contained proof for every fixed \(0<n<1\), based on an explicitly given ODE, its non-capturing circle equilibrium, a stable two-dimensional variational equation and exact harmonic matching. `verify.py` uses independent ODE shooting and Fourier quadrature at eight finite cases, together with symbolic algebra for the maximizer. Run `python verify.py` with numpy, scipy, sympy installed. A run passes only when it prints `VERIFY_OK`.

Computational checks are corroboration, not an infinite proof and not an independent audit. The formula is a local \(\varepsilon\)-expansion, is not uniform near endpoint speed ratios, and is tied to the chosen evader phase rather than an arbitrary timing of the same curve.
