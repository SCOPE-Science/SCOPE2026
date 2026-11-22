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

Run `python3 verify.py` using a standard Python 3 interpreter. The recorded output is `VERIFY_OK exhaustive_targets 3066 rank_polynomial_cutoff 16`.

The program computes direct fibers by iterating candidate input subsets and independently computes their rank-generating polynomials from directional runs. It enumerates all target subsets containing the origin within one-dimensional grids of lengths two to nine and a two-dimensional three-by-three grid, with several step vectors. It separately verifies coefficientwise extremality for all positive run compositions through cardinality sixteen and checks the Fibonacci evaluation. It is bounded finite testing: the universal theorem rests on the injective concatenation and run-localization proof. No independent audit has been conducted. The verified checks do not establish novelty or exclude unindexed prior equivalent formulations.
