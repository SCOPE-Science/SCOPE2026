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

# Reproducibility and verification limits

The standalone Python 3 standard-library program `check_gap.py` checks:

- 180 exact rational \(2\)-isometry identities for three positive parameters and 60 indices;
- 108 finite arithmetic-mean versus geometric-mean iteration identities across four iteration counts;
- 66 numerical scaled-limit and fixed-iteration tail checks, including a finite trace partial sum.

Observed output: `PASS 180 exact 2-isometry rational identities; 108 finite transform identities; 66 asymptotic sanity checks`.

The critical analytic steps are proved in `RESULT.md`: exact singular-weight identification, fixed-iteration fourth-order tail, compact-uniform binomial variance asymptotic, globally summable Efron–Stein bound and resulting dominated-limit calculations. Finite checks do not establish the infinite claims; they are supplementary. The result is not independently validated.
