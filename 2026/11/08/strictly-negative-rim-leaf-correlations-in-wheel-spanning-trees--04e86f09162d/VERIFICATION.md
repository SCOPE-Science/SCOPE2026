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

# Verification of wheel rim-leaf formulas

The standalone artifact `check_wheel_leaves.py` uses only the Python 3 standard library and exact integer/rational arithmetic. Run `python3 check_wheel_leaves.py` in the same directory as this file.

A successful run on the packaged artifact prints `PASS: 2718 exact assertions; brute spanning-tree enumeration m=3,...,8; all-size-claim instances m=3,...,100.` It independently enumerates edge subsets without cycles, counts all spanning trees of \(W_{m+1}\) for \(3\le m\le8\), and compares prescribed single- and double-leaf counts to the Fibonacci–Lucas formulas. It then checks the strict negative covariance and distance-ordering inequalities for every permitted integer distance up through \(m=100\). Exact fractions rather than floating-point approximations are used throughout.

These are finite checks, not an infinite proof. The all-size result instead follows from the leaf-grafting bijections, matrix-tree identities, and explicit Binet inequalities in `RESULT.md`. The fixed-distance limit follows algebraically as the small root \(t=(3-\sqrt5)/2\) is raised to growing powers. No extrapolation of machine output is used for the theorem.

No validation has been performed for weighted wheels, hub-leaf correlations or arbitrary graphs. Independent audit is not yet performed.
