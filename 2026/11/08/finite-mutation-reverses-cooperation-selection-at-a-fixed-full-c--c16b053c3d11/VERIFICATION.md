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

# Verification of the finite-mutation return comparison

The standalone `CHECK.py` requires only Python 3 standard-library facilities `fractions` and `math`. It reconstructs each conditional expectation from the three-person hypergeometric game and then constructs five-state detailed-balance weights. The source was executed against the same on-disk script packaged here and returned:

`PASS: 72 exact payoff/derivative comparisons and exact finite-selection witnesses`

`negative: 599130841/1318051952 positive: 141053/264124`

Each derivative comparison is performed with exact rational differentiation of the transition probabilities and the stationary weights at \(\delta=0\), not finite differencing. Each finite-strength witness uses the identity \(L(9\log(2)\Delta)=2^{9\Delta}/(1+2^{9\Delta})\) for the exhibited integer exponents, so the check is exact. The proof in `RESULT.md` establishes the formula for every real \(0<\mu<1\) and \(1\le r_2\le9\) as well as the all-strength reflection-neutral case. The 72 test combinations are supplementary reproducibility checks only, not an exhaustive parameter verification.

No independent audit or external certification was performed.
