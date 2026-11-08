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

# Reproducible verification

Run `python3 check.py` with the Python standard library only. It enumerates all Cayley trees via Prüfer words for \(n=4,5,6,7,8\), computes their degree-one counts and sibling-leaf-pair counts, and performs exact rational comparisons to the analytic formulas. It separately constructs the complete cherry-size-biased distribution from the uniform smaller tree and checks its identity at each attainable leaf count.

The actual run on the included source reported **PASS, 631 exact assertions**: exhaustive reconstruction of 280388 labeled trees, and exact rational positivity and second-moment checks for all integers \(9\le n\le200\). The count 631 includes 35 basic small-size equalities, the distribution support comparisons, and 576 additional integer-size assertions.

The computations do not certify the all-size claim, independence, or literature novelty. The all-size statements require the marked-cherry bijection, Prüfer absence probabilities, and asymptotic derivations supplied in `RESULT.md`. No independent audit has been performed.
