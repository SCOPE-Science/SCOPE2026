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

Run `python3 verify.py` with Python 3 and no dependencies beyond the standard library. It independently enumerates every labeled tournament of orders two through six, including \(32{,}768\) tournaments at order six, and checks the full ordered-pair obstruction list. The probability of each individual obstruction, both shared-coordinate two-obstruction probabilities, the count and weight of such pairs, and the first and second Bonferroni bounds are checked exactly as rational numbers.

The same script tests every possible triple of distinct ordered Boolean implication constraints on up to six coordinates, including a star attaining the proved bound \(9/16\). It executed successfully with 5,740 exact assertions. The proof's conclusions for all larger orders follow from the analytical product structure and finite implication classification; no finite exhaustive experiment is treated as a proof of the infinite asymptotic limit.

The originality comparison is limited by unavailable full text of Maurer's 1980 source. Independent audit is not performed.
