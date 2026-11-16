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

# Reproducible verification

Execute `python verify_spectrum.py` with NumPy, SciPy, and SymPy. The script uses independent two-variable vector-field Gram construction from Sobol-distributed Gaussian sphere samples, and compares all eigenvalues against Gaussian order-statistic quadratures. It also checks exact \(d=3\) moment identities, the theoretical trace, and symbolic determinant identities.

Actual checks passed: at dimensions 2, 3, 4, 6, maximal eigenvalue residuals were respectively \(8.10\times10^{-6}\), \(3.35\times10^{-5}\), \(4.72\times10^{-5}\), and \(4.08\times10^{-4}\). The predeclared QMC comparison tolerance is \(0.0018\). Each dimension also passed its cell-fraction and trace tolerances; both analytic three-dimensional moment checks and the two formal SymPy identities passed.

Limit: QMC is numerical corroboration, not an all-dimensional proof, a certificate of uniqueness in literature, or an independent audit. The infinite-dimensional parameter assertions rest on the detailed analytic proof in RESULT.md.
