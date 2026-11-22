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

# Verification record

Run `python3 checker.py` from the directory containing the complete artifact package. The checker uses Python's standard-library `fractions.Fraction`, `math.comb`, and `itertools.product`. Its 522 exact assertions verify the triangular-uniform interval integration, the conditional edge-count polynomial through six vertices for five specified rational coverage locations, the covariance and linear regression formulas, and the finite-sample correlation identity.

The mathematical proof covers every \(n\ge2\), every interior \(0<t<1\), and every feasible coverage \(0\le k\le n\). Finite enumeration is not used as a substitute for the general statement. The \(5/8\) limiting explained-variance fraction is obtained analytically from the exact expression, without a numerical extrapolation.

The original 1988 interval-graph article could not be inspected in full. Its later mathematical treatments were inspected for substantive comparison, but an independent historical-priority review has not occurred.
