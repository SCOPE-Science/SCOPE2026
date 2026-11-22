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

# Reproducibility and scope

Run `python3 CHECK.py` with Python 3.10 or later; no third-party packages are necessary. The checker performs 4,421 exact structural or deterministic quadrature assertions: Fibonacci coordinate reconstructions and coefficients for sample sizes 3 through 11, closed constants for sizes three and four, exact three-stick probability at shape index one, the dilogarithmic integral and numerical approach at both shape endpoints. These checks verify algebra and selected finite approximations, not the infinite asymptotic statements.

The large-shape result is proved by an exact unit-Jacobian change to nonnegative slacks, an integrable bound uniform in shape indices at least two, dominated convergence and Scheffé's lemma. The small-shape result uses independent exponential log-spacings, integrable second-order expansions, pairwise collision bounds and another Scheffé argument. No external certificate or independent mathematical validation is asserted. The sample size remains fixed throughout both limits.
