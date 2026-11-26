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

Fix an evaluation leaf. Multiplying the signed kernel by the current path mass gives state t; a normalized Haar product across the next two children is minus the inverse parent mass. Thus the omitted sibling contributes (1−p)|t−e| to the absolute row integral and the new state is pt+(1−p)e; the final leaf contributes |t_d|. Every state lies in [−1,1], and the finite operator norm is exactly the maximum absolute row integral. Changing a selected p to q≥p decreases the current term by (q−p)|t−e| while moving the next state by the same distance. With suffix signs fixed, its Lipschitz coefficients telescope to one, so the row cannot increase; maximizing over signs preserves this comparison. For r≤1/2, substitution into the suffix value A+B|t| reduces maximization to choosing the sign opposite to t since (1−r)−rB≥0 for 0≤B≤1. This gives the recurrence and the sharp upper envelope, attained on a consistent minority path of the homogeneous tree. Fair splits give B=1/3+(2/3)(−1/2)^k with k remaining splits, and summing yields F_d. A one-level defect shifts A and B at level j by (1+B_{j+1})δ; through the earlier fair levels the B shift gains successive factors −1/2 and the A increments are half of the incoming B shift. Summing gives precisely C_{d,j}δ. A path through the largest first bias can take all subsequent minority children; monotonicity compares it with the isolated defect. For a single biased node the other paths are fair or take its majority child and cannot exceed the defect value. This proves uniqueness of the fair minimum including depth one. The four two-step rows give 5/2, 5/2, 27/10, and 11/10, so the unique norming leaf is majority-first.

## originality

PASS

The fair constant overlaps exactly with a distinct same-day record, which even covers ragged fair trees. No priority or originality credit is assigned here to the fair constant or the product recurrence as standalone results. The material distinct claim is monotonic comparison for arbitrary nodewise splits and its sharp consequences: the level-minimum envelope, quantitative first-bias rigidity with equality, and failure of a norming-leaf greedy rule. The strongest inspected comparables do not cover that claim.

## value

PASS

A sharp comparison usable with only the minimal child probabilities on each generation controls a natural endpoint norm without enumerating all signs or evaluating every leaf. The first-bias coefficient gives a quantitative, attained rigidity statement that the fair endpoint value alone cannot give. The small greedy counterexample clarifies what the comparison does not compute for an individual tree, rather than serving as an isolated curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
