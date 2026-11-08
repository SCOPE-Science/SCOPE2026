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

The analytic proof treats every positive integer layer-size sequence. The forward projection solves a strictly convex simplex-budget problem by a scalar Karush–Kuhn–Tucker multiplier. The reverse projection uses exact isotonic least squares at each characteristic antichain vertex. The key comparison bounds every reverse candidate by the forward squared distance and proves strictness when at least three layers are present.

The accompanying `check_hausdorff.py` enumerates all vertices of both polytopes for 33 finite parameter profiles and solves independent constrained Euclidean minimizations using NumPy and SciPy. Executing it returned `LAYERED_ORDER_CHAIN_HAUSDORFF_CHECKS_PASSED profiles= 33`. It tests both directed maxima as well as the closed formulas. This is a finite diagnostic computation, not a proof of the quantified theorem.

The displayed case \((1,2,3)\) is exactly rational: the common forward squared Hausdorff distance is \(11/5\); reverse squared distances for \((1,2,3)\) and \((3,2,1)\) are \(6/5\) and \(3/2\). The equal-layer family analytically gives a directed-distance ratio \(\sqrt{k-1}\) for every integer \(k\ge2\).

No independent audit has been performed. The relationship to earlier research may need additional external historical validation; the selected documents do not supply the two directed Euclidean distances.
