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

# Verification of the mathematical statement

Execute `python verification.py` in an environment with Python 3, SymPy and mpmath. It performs an exact symbolic determinant comparison to the tilted Markov generator of the four-level exponential specialization, checks first three implicit derivatives and the single-dark-channel limiting formula, compares forty sets of independently computed numerical three-cumulant rates, and tests deterministic dark residence and a heavy-tailed Pareto residence. All checks completed successfully on the file supplied in this package. The rigorous statements for all positive parameters, arbitrary finite channel count and general almost-surely finite dark sojourns follow from the displayed renewal proof and strict Laplace-transform monotonicity, not finite enumerations. The public paper comparisons do not amount to independent validation or an exhaustive priority guarantee.
