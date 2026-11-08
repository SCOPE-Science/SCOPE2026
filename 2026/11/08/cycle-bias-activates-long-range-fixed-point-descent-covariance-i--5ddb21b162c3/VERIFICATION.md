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

The proof uses a conditioning/deletion identity for the Ewens measure and explicit two-image probability counts. No infinite claim is based on finite enumeration.

Run `python3 verify.py` using Python 3 and only its standard library. The script exactly enumerates all permutations of orders \(3\) through \(8\), stratifies their weights by cycle count, evaluates seven rational positive choices of \(\theta\), and compares the entire fixed-point/ordinary-descent covariance matrix and both aggregate covariance formulas as rational numbers. Recorded execution: `PASS: 1252 exact rational checks; all permutations through n=8; seven theta values`.

Boundary checks include \(\theta=1\), both sides of the phase boundary, and \(n=3\), where the ordinary-descent covariance has the separate threshold \(1/4\). The proof explicitly addresses \(n=2\) only as an excluded elementary boundary case. A separate independent review has not been performed.
