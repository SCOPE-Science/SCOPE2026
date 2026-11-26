---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A copy indexed by I is exactly the part of the sum-k slice with x_i≥lambda on I and x_i≤1−lambda off I. For lambda≤1/2, a k-subset can be selected iff at least k coordinates reach lambda and at most k strictly exceed 1−lambda. Summing coordinates (and using complement symmetry) gives exact coverage at and below 1/(R+1). For k≤n/2 and in the open first phase, the low obstruction requires exactly k−1 coordinates at least lambda: with at most k−2 the sum is strictly less than k−2+(R+2)lambda≤k. For each eligible set H the coordinates are b−z, with b_i=1 on H and lambda off H, z≥0, sum z=t, and z_i>0 off H for uncovered points. Since 0<t<lambda, high entries stay strictly above the low range in the closures. The large-coordinate obstruction cannot occur in the unbalanced low orientation; in the balanced case each low-family closure has k+1 coordinates at most lambda<1−lambda, incompatible with the k+1 coordinates at least 1−lambda needed in any complemented closure. This proves disjointness and the component count. Edge vectors t(e_i−e_j) give volume √n t^(n−1)/(n−1)! and facet area √(n−1)t^(n−2)/(n−2)!; exactly m facets meet the interior as interfaces. Dividing by the Eulerian slice volume gives the missing fraction. At x=b−z any covered point must increase one low coordinate by at least a=min_{i notin H} z_i. In the sum-zero displacement plane that costs at least √(n/(n−1))a. Increasing one minimizing coordinate by a and decreasing each other by a/(n−1) stays feasible: remaining low values are at least lambda−t+(m−1−1/(n−1))a≥0 and high values stay above lambda. The reached copy uses H plus the raised coordinate, so the cost is exact. The maximum requires z_i=t/m off H and 0 on H, giving precisely the fixed face barycenters (and complements in the other orientation). In each simplex the tail event translates the m constrained coordinates and reduces the remaining mass to t(1−u), so its relative volume is (1−u)^(n−1), including u=0 and u=1. The volume extends to endpoints by almost-everywhere convergence away from the finitely many moving threshold hyperplanes, and the metric by continuity of the compact union of homothets in Hausdorff distance. This gives the claimed onset regularity but not a later-phase decomposition. The nested verification/check.py was found and inspected, not executed. Four independent exact deep-hole witnesses replay via python3 /workspace/reviews/evidence/reproduce.py, output 2; they are not a substitute for the general argument.

## originality

PASS

The threshold and exact pointwise membership test are covered by the rank–corank predecessor after translating its parameter. The same normalized Beta law and a closely related simplex-volume mechanism already occur for sparse-paving projection, not for this target union. Credit the distinct first-phase geometry, distance formula and deep-point identification for the homothetic vertex-copy union, from which the volume, interface and law follow. No independent priority is asserted for the Eulerian normalization or the simplex tail computation in isolation.

## value

PASS

The first loss of exact coverage is a natural stability regime after the known threshold. The resulting full-dimensional void shape and fixed deep points are a structural answer, and the formulas show a concrete mismatch between nearly full coverage in volume and a linear loss in worst-case distance. The exposed interface and conditional distribution quantify distinct aspects of the exact geometry across every nonsimplicial rank in the phase; the value is not a renewed threshold computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
