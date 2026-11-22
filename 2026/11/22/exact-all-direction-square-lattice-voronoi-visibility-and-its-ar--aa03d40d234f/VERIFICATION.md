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

Run `python3 checker.py` in a directory containing `checker.py`. The present execution passed 675 independent exact cell-crossing cases, exhaustive height-rank probability comparisons for \(M=0,\ldots,6\), and all exact finite expected-degree identities for integer radii \(1\) through \(16\). For the first four radii, the calculated degrees are \(4\), \(28/3\), \(34/3\), and \(72/5\), respectively.

The mathematical proof for arbitrary integer radii is the five-part analytic argument in `RESULT.md`, including the half-integer crossing congruence, totient counting and derivative estimate for \(h(x)=1/[x(x+1)]\). These checks corroborate the proof but do not independently certify the infinite-radius asymptotic. No independent audit has been performed, and the residual historical-priority limitations are described in `REVIEW.md`.
