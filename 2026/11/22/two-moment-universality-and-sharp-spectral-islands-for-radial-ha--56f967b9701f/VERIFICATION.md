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

The analytical proof proceeds by an exact rank-one Toeplitz-calculus defect, spectral identification of a two-sided moment-weighted shift, and rank-one inversion with an exhaustive root-position case split. For the mixed-root case, the nonvanishing derivative establishes algebraic simplicity. The proof applies to every radial probability measure described in RESULT.md, including singular measures.

Reproduction: run `python3 verify.py` from the extracted package. The standard-library checker yields `RADIAL_QUADRATIC_CHECK_OK 2182` and uses exact fractions to check projection identities, the rank-one determinant algebra, and concrete contrasting measures. This is supplementary finite algebra, not a numerical replacement for the infinite-dimensional proof.

Bibliographic limitation: the 2021 unweighted quadratic article was compared through its accessible abstract and later explicit descriptions, not its complete text; the inspected 2026 full text treats the normalized area measure. Publication priority in more general radial settings is not independently certified.
