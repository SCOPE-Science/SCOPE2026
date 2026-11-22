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

# Verification

Run `python3 verify_synchrony.py` beside the two JSON representative catalogues. The checker uses exact integers, independently enumerates every row-sum-two matrix, checks the spectral filter by Newton sums and the zero determinant, verifies canonical orbit sizes, tests all 52 partitions, and checks four-cell minimality. It reports the class-frequency distribution and the two primitive adjacency matrices.

The theorem concerns a finite family and has exhaustive computational proof together with a mathematical proof that the tests are sufficient. No numerical eigenvalue calculations are required. No independent mathematical audit has been performed.
