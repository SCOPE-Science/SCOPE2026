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

The executable `CHECK.py` uses no external packages or data. It independently confirms all Weyl-element lengths by root inversions and independently recomputes all 396809 comparable-pair Kazhdan–Lusztig polynomials by left and right descent. It then checks the full membership profiles, every eligible denominator, every sharp maximum, every maximizer count, and the eleven ambient group bounds. The execution returned PASS on each check. This is an exhaustive computation on a finite group, not a proof of any proposed generalization to arbitrary Weyl groups.

The mathematical proof and exact reproducibility are in `RESULT.md` and `CHECK.py`. No independent mathematical audit has been performed.
