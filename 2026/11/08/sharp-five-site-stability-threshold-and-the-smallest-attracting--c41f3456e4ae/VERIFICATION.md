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

# Verification and reproducibility

Run `python verify.py` with Python 3 and SymPy installed. The script reconstructs the five-site Fourier mode characteristic polynomials symbolically from the original Jacobian formula rather than checking only displayed coefficients. It then reconstructs all stated Routh–Hurwitz expressions, validates the unique positive-root sign pattern and rational isolating bracket, checks strict coefficient positivity on the stable side, proves exclusion of winding-two/four and nontrivial winding for smaller network sizes, and reports the numerical threshold and imaginary-pair frequency.

The observed command output for the current package was:

```
VERIFY_OK five_cycle_fourier_blocks=2 exact_hurwitz_identites=12 unique_positive_root=1 first_stable_size=5 full_five_winding_classes=5 critical_g=1.207479509457 critical_tau=0.526742030488 transverse_frequency=0.712195392328
```

The analytic proof supplies the universal quantifiers. The symbolic computation checks the specific algebraic identities and sign reductions; it is not an independent audit and does not certify any nonlinear bifurcation or global basins. The exact algebraic root is defined by the polynomial and isolating interval, not by decimal output.
