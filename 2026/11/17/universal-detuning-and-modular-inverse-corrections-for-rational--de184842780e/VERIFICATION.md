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

The analytic proof appears in `RESULT.md`; the accompanying `verify_eos_general_detuning.py` supplies finite high-precision consistency tests. Run `python verify_eos_general_detuning.py` with `mpmath` installed. The actual successful execution prints:

`EOS_ALL_DENOMINATOR_DETUNING_OK cases=40 max_u_error=1.958776e-19 max_mult_error=2.5325941e-20 max_db_error=1.3377479e-18 max_arith_coeff_error=0.0075`

The script uses 105-digit arithmetic, tests 40 original-map cases with three denominators and multiple coprime numerators, checks periodic residuals and primitive itineraries, and tests the critical phase, multiplier and derivative expansion. The `max_db_error` measures the fixed-start partial derivative \(\partial_b F^n\), whose leading limit \(n\) combines with the multiplier identity to give the orbit sensitivity. The `max_arith_coeff_error` is the absolute error in the normalized \(q\)-coefficient; the predicted \(O(1/a+a q)\) convergence is checked. These examples are neither exhaustive nor sufficient for an infinite theorem; analytic uniform expansions prove the general statement.

The self-review checked the exact sign conventions, order of visiting the negative gate, the drift term \(t_*\sigma/n\), differentiability of exponential remainders, the limiting root and its normalized multiplier. Independent audit status is **not performed**.
