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

# Reproducibility
Run `python3 verify.py` with Python 3 and no third-party packages. The script implements a direct three-state continuous-time Markov chain using `fractions.Fraction`. It enumerates every Prüfer-labelled tree of orders two through five and samples 22 deterministically chosen Prüfer codes at each of orders six and seven. For each of three rate-ratio profiles it recomputes the exact chance of informing every vertex for every possible starting vertex and compares with the asserted product. It separately evaluates the sharp path bound for the checked trees. The actual execution reports:

```
PASS: 567 distinct tree/profile tests and 2958 independent root exact CTMC comparisons
```

The file is self-contained. All derived quantities are exact rational numbers; no Monte Carlo sampling is used. These tests are finite and do not certify an unbounded theorem. The written proof in RESULT.md establishes the general statement using competing hazards, local independence on trees, and paired-factor inequalities. In this code the tests for sizes six and seven are samples, **not** an exhaustive census; the all-tree assertion rests solely on the analytic proof.

The source inspection examined the open-access text of arXiv:1112.2239v1, arXiv:1202.4019v1 and arXiv:2005.11440. Source comparisons do not establish independent historical priority; possible equivalents in other publications remain a residual uncertainty. Independent audit has not been performed.
