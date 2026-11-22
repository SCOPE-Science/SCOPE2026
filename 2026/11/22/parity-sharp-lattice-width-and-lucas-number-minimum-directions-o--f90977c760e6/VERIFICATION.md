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

The proof is analytic and covers all integer dimensions \(n\ge3\) and integer weights \(w\ge2\). Its critical exceptional case is the exclusion of a three-symbol, range-two minimizing normal at \(w=2\) and odd \(n\); the five permitted adjacent transitions imply a constant word or a two-periodic one, so neither can occur under the exceptional hypotheses.

Run `python3 verify_width.py`. In the saved package, this standard-library script completed 306,168 bounded primitive-direction comparisons and 352 equality cases without assertion failure, over \(3\le n\le8\), \(2\le w\le5\), and coefficient ranges at most three. These computations are supplementary finite tests, not independent or infinite certification. The lower bound, equality cases, and Lucas-number count rely on the full written proof.
