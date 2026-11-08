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

# Reproducibility and verification

Run `python check.py` in the same directory with Python 3.10+ and SymPy 1.10+. No downloads, hidden data files, stochastic sampling, or other dependencies are required.

The checker reconstructs both eight-state generator matrices, solves both invariant-vector equations exactly, checks normalization and all four displayed rational probabilities, factors the two critical differences, checks positivity of the regional comparison polynomial, proves the full-occupancy polynomial's one positive root by coefficient signs, and brackets that root with exact rational evaluations. For a structurally separate check, it uses principal-minor stationary weights at seven rational positive rate values, comparing eight coordinates for each of two source placements: 112 exact comparisons. This finite comparison is not used as proof of the all-parameter statement.

The mathematical argument is self-contained using generator balance, exact polynomial algebra, Descartes' rule, and continuity; the attached code permits reproduction of the nontrivial algebra. Empirical calibration, external expert validation, a general-network result, and independent audit remain outside the verification performed here.
