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

The mathematical proof in `RESULT.md` proves the formula for all integers \(n\ge2\) and \(1\le k<n\). The accompanying `verify.py` performs exact finite checks independent of the symbolic covariance cancellation:

- Exhaustive generation of every uniform recursive tree for \(2\le n\le9\), totaling \(1+2+6+24+120+720+5040+40320\) trees, with exact expectations and cross moments.
- Direct conditional-regression checks at every admissible conditioning value and fringe size for those trees.
- Exact insertion recurrences for fringe-size means through \(n=120\).
- Independent two-colour urn distribution recurrences through \(n=120\).

`python verify.py` returned `PASS: 14728 exact rational assertions` from the standalone script. This finite evidence confirms the calculations but is not a substitute for the all-size analytical proof. No independent audit or external certification has been performed.
