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

# Verification

For a rank-\(k\) paving matroid \(M\) on \(n\) elements, all \((k-1)\)-subsets are independent. A nonbasis \(k\)-subset is therefore contained in exactly one rank-\(k-1\) hyperplane. The submitted proof obtains an explicit nearest feasible point by uniformly averaging the one-element exchanges of the nonbasis with elements outside that hyperplane. A coordinate-sum inequality and Cauchy--Schwarz certify global optimality and uniqueness.

Run `python check_paving_metric.py` from the directory containing the script. The program needs Python, NumPy and SciPy. It enumerates full basis hulls for ten finite paving configurations, checks exact rational distance predictions and witness memberships, and independently minimizes Euclidean squared distance over convex combinations of every basis via constrained quadratic optimization. Observed result: `PAVING_HYPERPLANE_METRIC_PASS cases=10 total_ksets=444 nonbases=90 independent_QP=95`.

The analytic result covers all finite paving matroids of the stated ranks, including disconnected examples. The program does not enumerate all paving matroids, does not certify any infinite family on its own, and does not constitute an independent mathematical audit. Numerical optimizations use finite tolerances; the displayed projection lower bound is exact.
