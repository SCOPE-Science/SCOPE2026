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

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy installed. The script verifies algebraic identities for the singular interaction matrix, the left/right null vectors, the exact positive diagonal multiplier, and the leading principal minors. It calculates the unique real root of the cubic cutoff and tests representative positive and indefinite quadratic forms. Four positive initial conditions are integrated with tight numerical tolerances; their limiting equilibria are predicted separately by conserved-level root solving.

Successful execution reported:

```
EXACT_MATRIX_IDENTITIES 11; certificate_root=1.574743073887
FINITE_TRAJECTORY a=1.10 limit_error=8.6e-13 conserved_error=2.4e-12 PSD_nonzero_min=1.1591
FINITE_TRAJECTORY a=1.30 limit_error=9.8e-13 conserved_error=3e-12 PSD_nonzero_min=1.1758
FINITE_TRAJECTORY a=1.50 limit_error=7.3e-12 conserved_error=2.7e-12 PSD_nonzero_min=0.52704
FINITE_TRAJECTORY a=1.56 limit_error=5.1e-13 conserved_error=4.9e-12 PSD_nonzero_min=0.11991
VERIFY_OK exact_kernel_and_minors=1 finite_trajectories=4 certificate_failure_checks=3
```

The symbolic algebra supports the explicit identities and finite examples support the predicted convergence. Neither a finite trajectory simulation nor the source's local stability discussion proves convergence for every positive initial condition; the proper entropy, LaSalle step, conserved-level uniqueness and local transverse estimate provide that proof. No external or independent audit has been conducted. At the endpoint \(a=\rho\), only the positive-semidefinite certificate is proved, not global convergence.
