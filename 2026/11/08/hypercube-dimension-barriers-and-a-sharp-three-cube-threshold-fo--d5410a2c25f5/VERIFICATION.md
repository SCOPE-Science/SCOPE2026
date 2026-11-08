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

# Reproducibility and limits

Run `python3 verify_hypercube.py` using Python 3.8 or later; there are no nonstandard Python dependencies. The expected stdout is `VERIFY_OK checks=1080`. The checks use `fractions.Fraction` and integer polynomial arithmetic, evaluate all Q3 radial entries against exact rational-function formulas, check the root bracket with exact fractions, independently verify \(D(h)T(h)=N(h)\) for five rational steps using full \(8\times8\) matrices, confirm row sums and sample signs, and check the large-step coefficient structure across multiple dimensions and stages.

The finite program does **not** prove that all dimensions or all step sizes have been exhaustively checked. Those universal properties require the Walsh spectral formula, Padé integral identity, binomial generating function and Descartes argument documented in `RESULT.md`. Independent review has not been performed. All edge rates equal one and arithmetic in the checks is exact rational arithmetic.
