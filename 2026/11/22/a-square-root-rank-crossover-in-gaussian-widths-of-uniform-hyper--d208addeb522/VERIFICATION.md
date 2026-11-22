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

# Finite verification and analytic limits

Run `python3 check_uniform_width.py` with Python 3.10 or later. The checker has no external Python package dependencies. It checks exact rational quadratic identities (385 parameter/vector pairs), exact combinatorial fourth moments and nonnegative Hermite residual bounds for 55 parameter pairs, and sample-mean/variance consistency for 24,500 reproducibly seeded Gaussian widths over seven cases. Expected terminal marker: `UNIFORM_HYPERGRAPH_WIDTH_PASS`.

The infinite-rank Gaussian/chi-square laws, the exact finite variance in all dimensions, and the proportional-rank law are mathematical deductions in RESULT.md. No finite numerical experiment constitutes proof of those claims. The Gaussian samples supply finite diagnostic checks only; all primary proof steps are symbolic. Published-source equivalence remains subject to independent assessment.
