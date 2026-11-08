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

The exact physical-time mean is derived by a finite-state renewal equation with an independently resampled jump rate, not by a continuum-limit approximation. The killed tridiagonal generator has the stated mixed absorbing/reflecting eigenbasis. Its fractional resolvent makes the physical-time correction nonnegative and at most \(\tau\alpha/(1+\alpha)\). The volume and window asymptotics follow from dominated mode sums and singular midpoint Riemann sums. These analytic steps are provided in RESULT.md.

With NumPy and SciPy installed, `OPENBLAS_NUM_THREADS=1 python verification/check.py` produced `PASS: 951 finite-matrix, correction and asymptotic numerical checks`. The script diagonalizes the finite killed generator independently, checks its values against the stated explicit spectral eigenvectors, and evaluates finite-volume limits. The script is supplemental; it does not constitute an exhaustive proof for infinitely many \(N\), an originality certificate, or independent validation. The boundary uses suppressed outward jumps, and only fixed initial position and refresh duration are covered by the asymptotic theorem.
