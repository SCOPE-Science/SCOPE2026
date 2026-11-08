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

# Reproducibility and verification

Execute `python verify.py` with Python 3.10+; all imported modules are in the standard library. The script reconstructs the finite-contraction cumulant from the exact stationary product, compares with the dilogarithmic continuum integral and Euler–Maclaurin endpoint term, tests the unique Legendre optimizer and derivatives across scale parameters, and uses Fourier inversion of the independent product to check the actual one-sided tail against its sharp asymptotic. On the delivered source the program reported **289 deterministic diagnostic assertions passed**. The tail-to-prediction ratios at positive thresholds \(0.7\) and \(1.0\) increased toward one as \(\varepsilon\) decreased from \(0.2\) to \(0.05\).

The numerical tests are finite and cannot prove large-deviation, asymptotic or uniqueness statements. RESULT.md contains the complete analytic proof including the Euler–Maclaurin error, tilted density convergence and passage to a relative probability asymptotic. The literature comparison distinguishes the classical logarithmic weighted-sum LDP from the sharper probability coefficient. Independent scientific audit and independent validation have not been performed.
