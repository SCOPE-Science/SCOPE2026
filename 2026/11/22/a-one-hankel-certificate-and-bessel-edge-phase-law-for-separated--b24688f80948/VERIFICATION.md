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

The proof is entirely analytic: exact comparison of signed polynomial moment energies for every \(n\ge0\), a finite generalized eigenvalue calculation for each \(k\), a standard fixed-exterior Legendre asymptotic, and a dominated coefficient-series argument for the inverse-square edge limit.

Run the standalone standard-library file `CHECKER.py` with `python CHECKER.py` to reproduce exact-rational checks: the first four Legendre kernels, 45 initial and shifted moment blocks, one negative determinant, 12 semidefinite-boundary blocks, and 312 positive polynomial-energy comparisons. The checker does not certify the all-index inequalities or asymptotics; those require the displayed arguments. The numerical checker is supplementary and no separate audit or independent validation has been performed.
