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

# Verification

Run `python3 verify.py` within this extracted package. It carries out independent numerical integration of the stationary OU angular covariance (27 trapezoidal comparisons), a composite Simpson computation of the Green–Kubo kernel, white-noise and first-inertia-slope checks, parity checks in chirality, monotonicity and Gaussian growth at zero chirality, and direct finite-chirality optimization. The supplied results include the values of \(\Omega^2	au_*\) and \(|\Omega|K_*\) for \(\Omega=0.3, 0.1, 0.03\) with \(D_r=1\).

These tests are numerical consistency checks only. The endpoint estimates and global all-maximizers asymptotics follow from the analytic argument in `RESULT.md`; the program does not independently certify the infinite theorem. The interacting/glassy-system literature comparison remains publication-priority qualified.
