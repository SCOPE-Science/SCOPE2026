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

The source `checks/spectral_projection_check.py` is self-contained and requires only Python 3's standard library. Execute `python3 checks/spectral_projection_check.py` from the directory containing the embedded files.

The checker performs 2035 supplementary assertions: exact rational tests of right/left eigenvector equations and pairwise biorthogonality; exact integer coefficient tests of the hypergeometric norm identity; floating-point comparisons of finite \(m\) with the sharp fixed-parameter prefactor; and direct series evaluations of the critical modified-Bessel profile.

The analytical proof in `RESULT.md`, not these finite checks, establishes the norm formula for all nonnegative integers, the asymptotic for all fixed positive couplings, the critical limit for all convergent bounded \(m t_m\), and the spectral-structure consequences. The checker does not establish a global novelty or independence certificate. The published eigenvector formulas are explicitly cited rather than independently attributed as new.
