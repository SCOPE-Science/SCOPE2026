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

Run `python3 verify_offset.py` from this directory. The checker needs Python's standard library only and independently evaluates the exact Bernoulli cell matrix and permutation covariance. For small sizes it enumerates all coordinate permutations, computing the conditional jitter contribution separately. This tests the closed polynomial with exact fractions for many rational offsets and verifies the reflection law and diagonal case.

Recorded run: 733 exact-rational assertions, all passed. The finite checker does not prove the all-\(n\) identity, the uniform remainder, or density of irrational rotations; their proofs are in `RESULT.md`. No external scientific validation or separate audit is asserted.
