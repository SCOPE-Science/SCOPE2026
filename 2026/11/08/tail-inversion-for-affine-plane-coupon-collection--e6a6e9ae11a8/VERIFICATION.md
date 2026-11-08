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

# Verification and limits

Run `python3 verify.py` with Python 3.10+ from this package. The script has no nonstandard imports. It constructs the affine incidence structures for orders \(3\), \(4\), and \(5\) (including \(\mathbb F_4\) arithmetic), checks every three-point incidence pattern, exhaustively sums the \(511\) nonempty point subsets at order three, and independently computes the first six tails by forward union-state dynamic programming. It also confirms the exact rational values of the crossover and published means. The recorded execution completed with 3,060 passing finite assertions.

These calculations are supplementary. For every affine plane of existing order \(q\ge3\), the infinite tail coefficient and the strict early/late sign contrast follow from the analytic inclusion–exclusion and line-counting proof in RESULT.md. The order-three all-time sign classification uses the verified finite coefficient table plus the explicit positive finite-difference inequality in Equation (10). No finite computational check is treated as a proof for arbitrary \(q\) or unbounded \(t\).

The result has undergone self-review only. An independent audit has not been performed. Historical-priority uncertainty about general block-design tail comparisons remains.
