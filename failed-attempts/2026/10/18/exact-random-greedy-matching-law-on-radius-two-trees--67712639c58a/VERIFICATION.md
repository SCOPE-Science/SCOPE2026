---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Until the center is matched, an arriving central edge can win exactly when it is first in its branch. In any branch a prior outer edge would have matched the branch vertex (unless this branch's central edge had already been accepted, which contradicts the center being vacant). Thus the earliest eligible edge is exactly the central winner. The subprobability density for branch i's eligible time t is (1−t)^{a_i}; integrating it against the independent branch survivals [a_j+(1−t)^{a_j+1}]/(a_j+1) gives p_i by y=1−t, and evaluating the product of survivals at t=1 gives p_empty. This includes a_i=0 (always eligible), the single-branch star, and the no-central possibility only when all branches have a leaf. The possible matchings are exactly those listed, and permutations of leaf labels act transitively in each class, giving the stated labeled law. For d≥2 and all a_i≥1 the class sizes are A and A/a_i with A=∏a_i; the difference in mass of the no-central event is the stated TV bound and is positive by the product cross terms. A separate exact permutation check reported agreement on 88 profiles (1,012,517 orders and 523 labeled outputs); at (1,1) the three masses are 1/4,3/8,3/8 and TV=1/12. The frozen script and recorded output under artifacts/ were inspected, not executed. Finite agreement supplements the argument, and no scientific correctness defect was found.

## originality

FAIL

The central-winner and complete labeled formulas are mechanically implied by Penrose–Sudbury's earlier general dimer RSA vertex-splitting coupling, not just computable by a generic brute-force recursion. Splitting the center produces independent stars. The published proof couples corresponding edge arrivals up to the first match of the split vertex; that first edge and its branch are the same pathwise. The minimum in each star gives exactly the finding's eligible-time distribution. The TV witness then uses its no-center probability and elementary counting. The priority defect is demonstrated by the earlier primary theorem and proof, not inferred from the same-day catalogue overlap or any inaccessible paper.

## value

FAIL

Explicit labeled probabilities are a useful objective, but for the claimed radius-two family the formula directly instantiates the published coupling on disjoint stars. After crediting that coverage, the TV statement is only the difference of probabilities of one already determined event versus a direct cardinality count; the strictness is the elementary cross-term inequality. There is no independently substantive new bound or classification left to retain under the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
