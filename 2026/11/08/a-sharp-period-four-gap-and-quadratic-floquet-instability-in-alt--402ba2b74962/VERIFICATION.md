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

# Reproduction and scope

The accompanying `verify.py` requires only Python 3 standard-library modules `fractions` and `math`. Run `python3 verify.py`. It constructs the exact rational-center square with radius \(10^{-8}\) and uses rational interval operations for four updates, the Jacobian of the four-step displacement, an inverse point Jacobian, and the Newton self-map. The verified sup-norm Jacobian contraction is below \(1.893\times10^{-5}\), and the full image lies strictly inside the square. Consequently, the exact four-step fixed point exists by the Banach theorem, and interval propagation places its four population coordinates in pairwise disjoint subsets of \((0,1)\) while keeping all effective logistic parameters in \((0,4)\).

Successful output contains `CERTIFIED_PERIOD_FOUR` followed by `VERIFY_OK rational_interval_existence=1 analytic_floquet_cases=9`. Nine independent rational coupling values check the exact two-step matrix trace and determinant; the global odd-period obstruction and two-cycle census are analytic and do not rely on finite sampling. The code does not check existence for other couplings, classify all longer cycles, or compute stochastic escape rates. Independent audit has not been performed.
