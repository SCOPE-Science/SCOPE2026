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

The standalone `verify.py` enumerates all consecutive-diagonal block partial maps for \(2\le n\le12\), independently determines each nonzero nilpotent's index by sparse-map composition, and compares full index multiplicities, cumulative tails, and first moments to the formulas. Additional arithmetic checks use the exact divisor sum for \(n=100,1000,10000\), and calculate second moments by offset/rank quotient blocks. All comparisons must pass for `VERIFY_OK` to be printed.

The verifier demonstrates exact finite agreement, not infinite certification. Asymptotic statements rely on the analytic proof in `RESULT.md`. No independent mathematical audit has been performed.
