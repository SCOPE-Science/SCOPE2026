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

# Reproduction of exact checks

Run `python check_kernel.py` with an installation of SymPy. The checker verifies six monomial moments of each source rule, derives exact sixth-order Peano kernels from the rule on truncated fifth powers, checks their factorizations and sharp extremal-ratio constants, verifies the unique optimal midpoint blend, and checks 57 polynomial functions whose sixth derivatives have nonnegative Bernstein coefficients. Its successful result is `VERIFY_OK`.

The derivation printed in `RESULT.md` proves the infinite-dimensional claim by applying a positive-weight integral to an exact pointwise kernel ratio. Finite symbolic tests are auxiliary consistency checks, not a numerical proof of an infinite claim. Smooth bump sequences establish that the stated constants cannot be improved. No interval-arithmetic or finite-precision floating-point certification is claimed. There is no independent mathematical audit.
