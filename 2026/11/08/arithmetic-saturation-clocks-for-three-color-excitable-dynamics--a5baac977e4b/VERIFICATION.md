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

# Verification of exact cactus activity distributions

The theorem uses the published finite-graph circulation result and the explicit independent modular-increment argument in `RESULT.md`. The Poisson limit follows from the displayed exact fixed-deficit trinomial coefficient and the binomial zero-event formula, not numerical extrapolation.

The exact standalone source files are `exact_formula.py`, `dynamics_check.py`, `nonbouquet_check.py`, and `critical_check.py`. No external packages are used. Run them in that order from the directory containing these files; `dynamics_check.py` imports `exact_formula.py`. Their recorded standard outputs are `formula_output.txt`, `dynamics_output.txt`, `nonbouquet_output.txt`, and `critical_output.txt`.

For six bouquet/mixed examples, `dynamics_check.py` traverses every three-color initial configuration (up to 59,049 states per rule), iterates each synchronous automaton until it reaches a previously visited state, computes the root excitation fraction on that cycle, and checks the entire histogram against the coefficient formula. For three separately constructed nonbouquet cacti, `nonbouquet_check.py` does the same full-state check with a separate transition and coefficient implementation. `exact_formula.py` verifies the resulting total populations and near-endpoint coefficients. `critical_check.py` calculates exact endpoint coefficient expressions and the finite-binomial probabilities in all three residue classes.

Each program was rerun from files extracted from the delivered record, and each output was compared byte-for-byte with the corresponding embedded result. The package contains all dependencies needed for replay. The finite examples do not establish the all-graph result or the limiting theorem; those follow from the mathematical steps in `RESULT.md`.

Limits: the established quantities are asymptotic temporal excitation rates, not first-entry times or primitive period spectra. The independent audit status remains unperformed.
