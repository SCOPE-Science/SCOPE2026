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

# Mathematical verification notes

`check.py` is self-contained and requires Python 3 standard library only. Run `python3 check.py` in the directory containing this file. It enumerates all 24 strict rankings of a two-by-two matrix and all 362,880 strict rankings of a three-by-three matrix, comparing the resulting loss, arrival and mixed-moment fractions with the derived all-size formulas. It also evaluates both marginal probability-generating-function specializations using deterministic Simpson quadrature and verifies rational covariance arithmetic. In the inspected execution, all assertions passed.

These executable checks do not establish the infinite marked Poisson limit. That limit is proved by independent-column rare-point convergence, asymptotic independence of finitely many row-minimum tests, exponential truncation of remote columns, and an explicit first-point decomposition. Each argument and its hypotheses appear in `RESULT.md`. The full texts of two historically relevant sources were unavailable, which limits priority assessment, not the mathematical statement's proof.
