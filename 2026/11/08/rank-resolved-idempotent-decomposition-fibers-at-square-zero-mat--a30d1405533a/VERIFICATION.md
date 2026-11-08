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

# Reproducible checks
Run `python3 squarezero_idempotent_sum_verify.py` with Python 3 and no third-party packages. It constructs the extension fields by irreducible polynomials, enumerates all labeled matrices of each tested size, directly verifies both idempotent equations, and computes ranks by finite-field elimination. The expected Gaussian-binomial formula is evaluated separately using integer arithmetic. Compare stdout byte-for-byte with `squarezero_idempotent_sum_verify.log`.

The tested cases are \(n=2\) with target ranks \(0,1\) over \(q=2,4,8\), \(n=3\) with target ranks \(0,1\) over \(q=2,4\), and \(n=4\) with target ranks \(0,1,2\) over \(q=2\). Every possible first summand is enumerated in each case, and the second is determined by the target. The pass marker is `ALL_SQUAREZERO_IDEMPOTENT_SUM_FIBERS_PASS`.

These are finite corroborations, not proofs of the general family. The mathematical proof is the block normal form and exact count in `RESULT.md`. Independent review has not been performed.
