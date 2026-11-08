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

# Reproducibility and validation boundaries

Run `python3 verify.py` with Python 3 and the SymPy package installed. The symbolic module constructs, without importing precomputed fixation outputs, the six-state Markov first-step system for all four combinations of habitat placement and update rule. It compares exact solved fractions to the formulas in `RESULT.md`, then checks their two polynomial difference factorizations and the strictly positive coefficient list. A second independently coded Gaussian elimination solver with standard-library `fractions.Fraction` checks 96 cases on rational parameter pairs, including strict and equality cases.

The positivity of the displayed polynomial and positive denominators is an analytic proof for every pair of positive real parameters; a finite test grid is not substituted for this argument. No independent external audit, complete formal proof certification, or search-completeness guarantee is claimed. The result applies only to the stated small-graph model.
