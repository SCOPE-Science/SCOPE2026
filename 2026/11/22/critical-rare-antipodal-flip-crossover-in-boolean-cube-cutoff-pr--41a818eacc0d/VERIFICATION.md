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

# Reproducible verification

Run `python3 verify.py` using the Python standard library. The script evaluates 4,533 deterministic finite conditions, including exact-rational enumeration of sign configurations for dimensions one through seven, arbitrary subsets' Walsh coefficients, chi-square and total-variation identities, the monotonicity of finite-density mixtures at selected parameters, and large-binomial comparisons with independently evaluated Gaussian-limit integrals. The observed output is `VERIFY_OK 4533 exact and deterministic finite checks`.

These computations are diagnostics of finite formulas. They cannot prove arbitrary-dimensional convergence, strictness of the limiting profile for all parameters, or historical originality; the mathematical derivations appear in RESULT.md. The comparison integrals have numerical quadrature error, unlike the exact-rational identities.
