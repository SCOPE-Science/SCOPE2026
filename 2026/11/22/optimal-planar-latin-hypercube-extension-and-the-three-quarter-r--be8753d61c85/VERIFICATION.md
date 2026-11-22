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

# Reproduction and verification limits

Run `python3 check_lhs.py`. The checker contains exhaustive small-case enumerations for independent-set equivalence, exact rational one-axis probability and mean-collision calculations, and seeded Monte Carlo diagnostics. At execution, it reported 46,948 successful assertions, including one broad simulation sanity bound, and a seeded mean deletion fraction of 0.24990 at sample size 500. These checks do not constitute independent validation, nor do finite tests prove the limit. The limit follows from the alternating-path counting and bounded-exploration concentration argument in `RESULT.md`.

No external datasets are needed. Source comparisons were performed for the original non-integral extension formulation and later algorithms; historical priority is not independently certified.
