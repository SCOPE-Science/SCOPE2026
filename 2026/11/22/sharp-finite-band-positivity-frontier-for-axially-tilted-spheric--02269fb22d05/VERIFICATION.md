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

For each fixed \(t>0\), `CHECKER.py` forms exact finite-band zonal adjacent weights \(2(\ell+1)\cosh(t(\ell+1))/\sqrt{(2\ell+1)(2\ell+3)}\), computes the leading eigenvalue of the associated symmetric tridiagonal matrix, compares all nonzonal magnetic-order blocks in tested small bands, and approximates the compact half-line Jacobi top eigenvalue \(\rho(e^{-t})\). It checks strict cutoff decrease and numerical agreement with the stated relative \(-1/(8L^2)\) correction for four heat times and multiple bandlimits. The code has no dependency on any external data files and uses Python 3, NumPy, and SciPy.

Run `python3 CHECKER.py` from the directory containing this file. Expected output begins with `PASS: zonal dominance`. The numerical checks are finite and do not certify strict increase for all bands or the infinite negative index. Those claims are established by harmonic recurrence, Perron variational comparison, disjoint negative subspaces, and a proved operator-norm limit in `RESULT.md`.

Limitations: fixed positive heat time; two-dimensional sphere; the compact Jacobi norm is implicit rather than elementary. No independent external scientific audit has been performed.
