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

# Reproduction and evidence boundaries

Run `python verify_edge.py` with Python 3.10+, NumPy and SciPy. The checker reconstructs the implicit Thomas–Fermi scale by monotone root finding, compares it with independent initial-value ODE integration, verifies the exponential-moment constants exactly, and evaluates age covariances with deterministic Gauss–Laguerre quadrature. It samples reset-rate ratios \(r/\omega\in\{0.1,0.4,1,3,10,40\}\) and positive scaled lags, and checks both asymptotic limits at representative small and large rate ratios.

Expected output concludes with `PASS: ODE + energy, exact factorial coefficient, 36 shape/bounds cases, two limiting profiles, integrated limits`. The results verify implementation consistency on finite cases only. The proof of strict bounds over all positive rates and lags, exact tail amplitude, and limiting spectral laws is the analytical argument in `RESULT.md`; this numerical checker does not provide interval-arithmetic certification or an independent audit.

The observable represents the hydrodynamic condensate support edge and excludes microscopic boundary-layer and finite-particle corrections. No experimental data are claimed.
