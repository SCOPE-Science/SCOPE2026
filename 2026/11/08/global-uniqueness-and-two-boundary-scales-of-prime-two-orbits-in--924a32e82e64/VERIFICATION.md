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

# Verification evidence and limits

The mathematical proof uses five independent steps: unimodality of \(H(x)=x^2(1-x)(c+mx)\), algebraic elimination of the two cycle coordinates, exact discriminant and interval-boundary signs, strict global monotonicity of the parameter function, and two distinct leading-order asymptotic expansions. All assumptions and equality/endpoint cases are stated in `RESULT.md`.

`verify.py` is a standalone Python checker requiring `sympy` and `mpmath`. It was executed against the exact code included in this package with the result:

`VERIFY_OK symbolic_identities=5 high_precision_cycle_and_boundary_cases=54 precision_digits=65`

The five symbolic identities include the equal-weighted-orbit divided difference, product elimination, sum-orbit relation, discriminant, and complementary-product factor. The 54 high-precision tests span six parameter pairs, seven post-threshold growth factors, and two large-growth boundary regimes. They evaluate the **original** cubic recurrence rather than only its reduced scalar equation.

Finite examples, numerical residuals, and CAS simplifications are not replacements for the analytic all-parameter theorem. The checker does not establish that other published authors have not independently obtained an equivalent result. The theorem is restricted to nonnegative \(c,m\), positive interior primitive two-cycles, and fixed-coefficient large-growth limits; no stability or physical full-interval invariance claim is made.
