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

# Reproduction and limitations

Run `python3 verify.py` in the extracted directory; it recomputes the exact logit and probability maps, checks the nonzero cubic and mixed Taylor coefficients, and checks bounded numerical residuals of the proposed first-exit laws for several initial centers and perturbation scales. A successful run prints `PASS`. Python's standard library is sufficient for the numerical tests; SymPy, when installed, is used for the additional symbolic coefficient checks.

The proof concerns *all* sufficiently small perturbations for each fixed eligible start, whereas the checker tests finitely many. The analytic ingredients required beyond numerical evidence are: the exact tanh coordinate recurrence; uniform small-tube Taylor bounds; the geometric pre-exit bound on the imbalance squares; the positive reciprocal-square Gronwall estimates; the summable double-series bound; and the exact inversion of the resulting logarithmic multiplier sum. The full derivation appears in RESULT.md. Neither source inspection nor local tests constitute independent validation.
