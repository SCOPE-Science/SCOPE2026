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

# Reproduction and limitations

Run `python3 check_inverse_annuli.py` using Python 3, `mpmath` and optionally `sympy`. The checker recomputes exact incomplete-gamma moments independently of adaptive integration at 70-digit precision, verifies the weighted Vandermonde determinant against direct matrix determinants, checks endpoint moments and finite-difference derivatives, simplifies low-dimensional symbolic identities and produces two genuinely different two-annulus masks sharing three labelled Hermite moments but differing in the fourth.

Observed replay output:

```text
INVERSE_ANNULAR_STFT_PASS moment_cases=16 symbolic_dimensions=2,4 nonidentifiability_fiber=m2_two_sides boundary_moments=checked finite_difference_jacobian=checked max_integral_error=9.05568e-72 max_det_relative_error=2.54249e-66
```

The symbolic check covers 2-by-2 and 4-by-4 cases; numerical tests cover 16 examples with one through four rings. These checks do not establish the universal theorem. Global identification and the sharp minimality result rest on the polynomial sign-separation proof, the analytic Vandermonde identity and the finite-dimensional implicit-function theorem, as specified in `RESULT.md`. Independent scientific audit is not yet performed.
