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

The proof uses dihedral averaging of pseudometrics, two competing shortest paths, reduction of a one-variable affine-fractional expression to its breakpoints, and an explicit rotation-averaged arc-cut construction attaining every breakpoint. A separate coarea argument shows that the scalar and real \(L^1\) constants equal the largest cut ratio. No infinite claim is based solely on finite checks.

To run the independent finite diagnostics in the same directory: `python check_wheels.py`. The checker uses only Python's standard library and exact rational arithmetic and returns `WEIGHTED_WHEEL_EXACT_OK 99340 exact checks; r=4..159; all cuts r=4..13` when successful. It checks 10 rim sizes with all cuts for six conductance pairs, the optimized metric/cut formulas for 156 further rim sizes and six pairs, and explicit arc-cut distance identities. It cannot verify priority, the coarea theorem, or the general quantification over all sizes and weights.

Self-review: passed. Independent audit: not yet performed.
