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

# Reproducibility and limitations

Run `python3 verify.py` using the Python 3 standard library. The checker independently enumerates exact Bernoulli source-state probabilities, sensor-output equivalence classes, and optimal coordinatewise posterior decisions; it tests every sensor subset and every two-element submodularity inequality at finite rational parameter grids. It also checks the general all-sizes root-marginal formula for one through five sources, exact threshold equalities and strict inequalities for two and three sources, and the \(3/200\) obstruction at \(p=1/10\). All tested quantities use `fractions.Fraction`, avoiding floating-point sign mistakes. The mathematical proof of the continuum statement is in `RESULT.md`; the finite test grid is not exhaustive for real-valued parameters.

The output is not externally certified, not independently audited, and not a real-world validation of wastewater sensing or a bound on a greedy algorithm's observed performance.
