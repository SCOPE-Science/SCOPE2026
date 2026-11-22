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

# Verification record

The result is a symbolic, finite-state, single-partition theorem with an all-integer parameter \(m\ge3\). The proof uses hypergeometric daughter allocations and explicit rational expressions; positive numerator factorizations establish all infinitely many inequalities.

`CHECK.py` uses only the Python standard library. Run `python CHECK.py` in the folder holding `CHECK.py`. In the recorded test, it printed `PASS: exact hypergeometric and assignment checks`. It performs three independent labeled-cell assignment enumerations at six cells, plus exact fractions for 147 parent half-sizes \(m=3,\ldots,149\), verifying formulas, all comparisons and prevalence-normalized inequalities. These finite tests support but do not establish the infinite claim; that depends on the algebra given in `RESULT.md`.

The calculation excludes new infection, daughter growth, stochastic transmission, size-dependent predation, and additional rounds of reproduction; these excluded processes were not simulated or certified. Independent audit has not been performed.
