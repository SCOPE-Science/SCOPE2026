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

With the hub grounded, the follower matrix is diagonal and the weakest k−1 leaves are exactly the remaining leaders up to weight ties. Without the hub the Schur complement is W, the total weight on grounded leaves. The inverse is diag(0,1/w_i for follower leaves)+11ᵀ/W. Its squared trace yields the two reciprocal-sum terms and (r+1)²/W². To rule out a misordered leader set, take the weakest unselected a and strongest selected b>a. If W≤(r+1)b, replacing b by the hub eliminates the rank-one cost, which exceeds the added b⁻² because the cross term is positive. Otherwise W=t+b with t>rb; swapping b for a changes the cross term, divided by b−a, by 2(A₀−t/(ab))/((t+a)(t+b))<0. The positive rank-one change divided by b−a is less than (a+3b)/(b²(a+b)²), which is smaller than (a+b)/(a²b²), the magnitude of the negative diagonal change. This gives strict improvement, ruling out additional tie types. The endpoint cases k=1 and k=m are covered, with k=m+1 the empty follower problem. In unit weights, cost comparison is governed by 2k²+2k−(m+1)²; equality gives u²−2v²=1 for (u,v)=(2k+1,m+1). Positive powers of 3+2√2 exhaust the positive solutions and give odd u; u≤2v−1 for v≥2 gives feasibility. The first solution v=2 is excluded, leaving (11,8),(69,49),(407,288) first. Sorting and prefix/suffix sums give optimal values and compact descriptions of optimal sets, not explicit enumeration of all tied subsets. The supplied rational checker was inspected, not executed; the proof does not depend on its finite cases.

## originality

PASS

The same two candidate shapes are known for the first inverse trace on exactly these weighted stars, but the objective cannot be switched using that theorem: the linear threshold differs and the optimizers can reverse. The closest read second-moment results optimize conductances instead of leaders, or treat different topologies at a fixed two-leader budget. The distinct claim is the exact arbitrary-positive-weight, all-budget inverse-square optimizer and its threshold, conditional on the bounded searches.

## value

PASS

The arbitrary-weight exact-budget objective is natural, and the strict two-action comparison replaces an exponential subset search with a sort and a two-value comparison per budget. It identifies every minimizer, including tied conductances, rather than supplying only a candidate or bound. The unit-weight reversal relative to the first moment makes the distinction consequential. Pell arithmetic precisely describes when the two competing hub decisions tie rather than just approximating the switching fraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
