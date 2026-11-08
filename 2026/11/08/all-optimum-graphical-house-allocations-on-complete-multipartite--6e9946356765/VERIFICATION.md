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

# Verification procedures and limits

Execute `python3 verify.py` with Python 3 standard library. The checker uses a direct sum of absolute differences across all pairs of vertices of different parts and exhaustive enumeration of every possible part-label assignment word. It tests all sorted positive part-size multisets with total vertices between \(3\) and \(9\) and number of parts between \(3\) and \(5\), under two positive valuation-gap sequences per profile. It compares *sets* of minimizers, the minimum objective value, and the exact optimizer count. The observed output was `PASS 106 exact direct-cost instances; 215126 complete group-label assignments tested`.

This enumeration is complete only for the enumerated finite parameter domain. The full mathematical theorem for unbounded part sizes and arbitrary positive real value gaps is established by the cut-decomposition and simultaneous-priority-maximization proof in `RESULT.md`. No formal proof assistant, independent external audit, or general-case computational certificate is claimed. The priority comparison with an inaccessible pre-2023 path-wirelength source remains incomplete as documented in `REVIEW.md`.
