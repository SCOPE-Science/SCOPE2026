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

Run `python3 check_rank_dimensionalities.py` with Python 3, with no third-party dependencies. The program enumerates every binary matrix in sizes two and three, verifies the attainable product-rank intervals for all pairs of factor ranks, enumerates every set partition of ranks for each size from two through nine, and checks equality of the directly saturated and structurally classified partition sets. The final success marker is `MATRIX_RANK_NUMERICAL_SEMIGROUP_CHECKS_OK`.

These finite calculations test the structural deductions but do not prove the general theorem. The proof in `RESULT.md` establishes the classification for arbitrary fields and arbitrary matrix dimensions at least two. Historical priority has only been assessed against the cited and searchable literature, not independently verified.
