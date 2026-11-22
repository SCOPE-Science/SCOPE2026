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

The included `check.py` was executed using SymPy and mpmath. It reported `PASS: 8617 algebraic, positive-density-grid, and numerical assertions`, with the explicit numerical outputs

- `b(-1)= 0.01109548253032186777382474`
- `asymptotic_variance= 0.01503693250994238296993934`
- `limiting_5pct_rejection_probability= 0.01718802635086213621530442`

The checker independently evaluates conditional-projection variance using high-precision quadrature and compares it with the polynomial-integrated exact expression. The infinite-domain positivity and uniqueness claims follow from inequalities proved in RESULT.md, not from grid tests. Nondegeneracy and the limiting power law use standard bounded-kernel U-statistic asymptotics, not simulation. The scope excludes censoring and unknown-support estimation. The exact family is not claimed to classify all nonuniform blind distributions.
