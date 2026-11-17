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

# Reproducibility and evidence

Run `python verify_refresh_gini.py` with Python 3 and no external packages. The program uses exact rational arithmetic and a fixed integer random seed for its supplementary finite rational tests.

Observed output:

```text
EXACT_BINARY_REFRESH_AND_CUT_PAIRS_PASSED 86360
RATIONAL_INTERIOR_RATE_AND_INPUT_BOUNDS_PASSED 2632
EXACT_SHARP_SINGLETON_WITNESSES_PASSED 399
ALL_POSITIVE_SITE_RATE_AMPLIFICATION_WITNESSES_PASSED 97
ALL_HETEROGENEOUS_REFRESH_GINI_CHECKS_PASSED
```

The full binary experiment uses every nontrivial input cut and every zero-or-one rate profile for each dimension from two through eight, evaluating output variation directly and comparing with the proposed algebraic cut formula. The rational interior tests exercise the full-rate bound in dimensions two through twelve. The extremizer and positive-kernel tests exercise explicit constructions up to dimensions 400 and 100 respectively. None of these finite tests establishes the theorem for arbitrary dimensions; Steps 1–6 in `RESULT.md` supply the all-dimensional proof and exact quantifiers.

The analytical cut formula, integer maximization and strictly positive entrywise lower bound have been checked independently of the numeric output text. The closest literature uses oscillation or total-variation norms, not the Gini seminorm used in the claim. An independent mathematical audit has not been performed.
