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

# Reproducibility checks and their limits

Execute `python3 verify.py` in the same directory as this file. The script uses Python 3 with NumPy and SciPy. It computes the exact perimeter integral by adaptive one-dimensional quadrature, and evaluates the **unexpanded Euclidean distance** and exact arclength Jacobian on two-dimensional midpoint grids near each maximizing ordered pair. Symmetry enumeration covers all four ordered opposite tip pairs and branch combinations. No random seeds or external data files are needed.

The checker verifies the elementary perimeters \(L_{2/3}=6\), \(L_1=4\sqrt2\), \(L_2=2\pi\) and sharp coefficients \(2/9\), \(1/2\) and \(2/\pi\); then compares the finite-event probability against the proposed leading asymptotic for seven noncircular parameters and the exact circle formula. It prints each finite-threshold relative difference and ends in `ALL_CHECKS_PASSED` when its stated tolerances hold.

The proof itself is analytic. Quadrature and sample parameter values do **not** establish uniqueness among published statements or prove limits for all positive \(p\). Total-variation marked limits are obtained in `RESULT.md` from localization, Jacobian control and bounded homogeneous sublevel comparisons. No formal proof assistant, independent audit, or external mathematical certification was used.
