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

# Reproducibility

The ordinary Python 3 standard-library script `checks/cubic_legendre_bv.py` is included as a full standalone file. Execute `python3 checks/cubic_legendre_bv.py` from the containing folder. No network access, compiled dependencies or external packages are needed.

The script independently reconstructs the degree-three Legendre step derivative at five rational parameter values, sufficient to confirm the complete fourth-degree dependence on jump location. It covers the continuum of parameters from \(1/10\) to \(1\) by 45 intervals, each with five nonnegative degree-four Bernstein weights. Each coefficient is a quadratic in the evaluation variable with rational coefficients. Every quadratic's absolute integral receives an exact rational upper bound by monotonicity splitting, at most 40 rational bisections for each actual zero, exact antiderivative differences and a conservative isolation-error allowance. This is a finite exact algebraic continuum certificate, not a sample-grid convergence argument.

The strict near-centre derivative inequality and Stieltjes reduction are proved in RESULT.md and must be read alongside the script. A successful run proves the advertised 225 inequalities conditional only on standard integer/rational Python arithmetic and the documented root-isolation logic. The result has not undergone independent audit. Outside scope are other polynomial degrees, nonuniform weights, complex input, and absolute historical priority.
