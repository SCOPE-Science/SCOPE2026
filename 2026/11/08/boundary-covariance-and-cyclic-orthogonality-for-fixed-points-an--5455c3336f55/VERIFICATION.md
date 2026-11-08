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

# Reproducibility and limits

Run `python verify.py` with Python 3 standard library in the same directory. The verifier calculates the covariance by direct enumeration over permutations of orders 2 through 7 and compares it with the boundary formula for every allowed pattern of length 2 through 4. It separately checks all cyclic pattern covariances vanish and directly checks each anchored conditional probability for smaller sample sizes. Finite binomial/Vandermonde identities, strict extremizer criteria and the length-three sign and minimizing-pattern transition are verified over larger parameter ranges. The checker passed 13,254 exact assertions.

The mathematical proof in `RESULT.md` establishes all statements for arbitrary integers in the stated ranges; computations are independent small-case checks only. No numerical approximation, simulation, external certification, or independence claim is required.
