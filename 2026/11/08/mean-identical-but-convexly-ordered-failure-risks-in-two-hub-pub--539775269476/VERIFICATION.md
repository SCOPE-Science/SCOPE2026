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
# Verification notes

The self-contained `verify.py` uses only the Python 3 standard library and independently constructs graph connected components from explicit edges for each sampled surviving set. It checks the closed-form expectation, convex hinge comparisons, variance differences, and percolation probability-generating functions.

Command: `python verify.py`

Actual successful run: 265 histogram/mean identities; 830 hinge inequalities; 98 variance-difference identities; 99 exact rational percolation-law comparisons. Tested \(4\le n\le9\), all ordered two-hub splits, all \(0\le m\le n\), and survival probabilities \(1/3\), \(1/2\), and \(3/4\).

The finite test is a check, not an exhaustive proof for unbounded orders. The general statements follow from the exact three-pattern decomposition and convexity of hypergeometric/binomial expectations in the hub-leaf count. No independent scientific audit was performed.
