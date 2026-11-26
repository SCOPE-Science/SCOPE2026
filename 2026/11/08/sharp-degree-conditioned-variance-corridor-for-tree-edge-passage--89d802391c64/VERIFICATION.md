---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent first-step check decomposes each parent passage into a geometric number of failed child excursions and one final step. At a vertex with h children the failure count has mean h and variance h(h+1); a failed excursion chooses a uniform child and lasts 1+Z_c. Induction gives mean 2s_v−1 and the variance recurrence V_v=sum_c V_c+4sum_c s_c²+4(s_v−1)², equivalent to the frozen recurrence. Thus V_x=4s(s−1)+8sum_{v≠x}s_v(s_v−1), independent of the part beyond y. At fixed branch sizes the lower bound requires every proper descendant of a branch root to be a leaf; strict integer smoothing then gives the unique balanced size multiset. For the upper bound, induction on an unrestricted branch of size r gives maximum P(r)=(4/3)r(r−1)(2r−1), uniquely at the endpoint-rooted path: the child-size contributions F(u)=P(u)+4u(u−1) have strictly increasing increments, so concentrate all surplus on one child, and one child is best when the number is unrestricted. At x this same allocation at fixed k gives (s−k,1,…,1), including k=s−1, when all children are leaves. Substitution of s=2m+1, k=m verifies both polynomials and the ratio asymptotic m/6 with equal marked degrees, mean and order. Inspected VERIFICATION.md and verify.py without running the latter; the absorbing-chain check there is finite (s=2–8) and not needed for the proof. In its final m-loop it asserts the lower expression and U>=L rather than a separate upper-polynomial identity; the upper polynomial was checked by exact substitution above.

## originality

PASS

The adjacent-edge mean and exact variance are already available, including the fringe form by regrouping. The supported distinct claim is the sharp degree-and-size-conditioned corridor with both rooted equality classifications and its quantitative same-data consequence. Neither the exact predecessors nor the distinct indexed overlaps checked supply this optimization.

## value

PASS

The complete sharp optimization answers how much root-degree information restricts dispersion when the mean is already fixed by the size of the starting component. The equality shapes identify two competing mechanisms, and the unbounded matched-data ratio shows that any size-independent multiplicative prediction from those statistics fails. Credit rests on the sharp constrained classification, not on rediscovering the known moment formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
