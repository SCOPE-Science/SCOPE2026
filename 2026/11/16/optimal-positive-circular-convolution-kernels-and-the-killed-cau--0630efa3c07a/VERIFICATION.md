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

# Verification record

The standalone `CHECK.py` executed successfully with `numpy` and `scipy`: 248 finite consistency assertions passed. Tests reconstruct the Toeplitz coefficients from the first circular moment, compare direct numerical quadrature with the minimal eigenvalue, check that the positive minimizers are reversal symmetric, and test Rayleigh competitors. Large degree checks evaluate the scale \((n+1)C_n\) and compare it with the known Rivlin-type test-energy constant.

The analytical proof, not the checker, supports: (i) completeness and uniqueness of the minimizing class through Fejér–Riesz and Perron–Frobenius; (ii) spectral convergence through uniform Fourier tail and alias bounds plus smooth sampling; and (iii) strict comparison by the boundary logarithm of the restricted half-Laplacian acting on the sine test function. The numerical experiments are finite, approximate, and do not constitute exhaustive classification or infinite-dimensional certification.

No independent audit has been performed. The older Goldstein–McDonald paper could not be inspected in full and remains a publication-priority risk.
