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

# Reproduction and verification

Execute `python verification.py` in this directory using Python 3.10+ and SymPy 1.12+. The script constructs both 15-state transient Markov generators directly from the specified edge sets, performs exact symbolic inversion, and verifies the quoted rational expressions and their factorized difference identically. It uses an independently written exact-Fraction recurrence, ordered by occupied-set size and perturbation order, to check the first three series coefficients for each graph. An auxiliary collection of exact positive-rate substitutions is diagnostic only; the polynomial positive-coefficient argument proves the full infinite rate range.

The output must report `PASS`. The full-occupancy expected times at λ=1 are the rational values 1661/420 and 12659/3306, with gap 29081/231420, as cross-checks. The general small-rate formula is proved in RESULT.md, not inferred from the finite diagnostic test. The graph-motif proof uses formal inverse expansion and edge-pair permutation symmetry, not an exhaustive enumeration for arbitrary n. No independent external audit has been performed.
