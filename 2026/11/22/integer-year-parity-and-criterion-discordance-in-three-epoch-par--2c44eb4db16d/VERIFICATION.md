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

# Reproducible verification

Run `python3 verify.py` in the directory containing `verify.py` and `RESULT.md`. The script requires only the Python standard library. It independently checks the nuisance-removing linear contrast, the rational minimum-variance lower bound at half-integer phases, the existence and uniqueness of the even-baseline root by monotone bisection, parallax-variance symmetry, sample-grid dominance, strict improvement among increasing even baselines, and asymptotic displacement. In the package-construction environment the unmodified script returned:

`PASS 124806 deterministic assertions; no infinite-proof claim.`

The core analytical fact is the sign change of \(\pi\cot(\pi v)-v/(3K^2/2+2v^2)\) on \((0,1/2)\). This is proved using the opposing strict monotonicities in `RESULT.md`; finite grid tests do not establish it. Model-based normal-theory variances assume independent equal-variance errors and known scalar annual phase. The all-integer optimum is not a result about general multicoordinate astrometric solutions.
