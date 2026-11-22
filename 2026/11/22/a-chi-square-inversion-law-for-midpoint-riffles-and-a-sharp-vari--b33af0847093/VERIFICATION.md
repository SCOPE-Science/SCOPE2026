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

# Verification record

All-size correctness rests on the reflection involution for midpoint-key comparisons, independent tie-coin contributions, the symmetric-binomial fourth-moment identity, the binomial CLT, and the Lindeberg triangular-array argument for classical GSR inversions. Each step is written out in `RESULT.md`.

Reproducible finite checks: execute `python3 checker.py` from this directory with Python 3 standard library. The captured `checker_output.txt` reports 472 passed exact-arithmetic assertions. The checker separately constructs all midpoint output permutations for all cuts at sizes 2--16, verifies the conditional binomial law and exact moments, and enumerates all GSR binary output words for sizes 2--13. It does not establish the infinite-size conclusions or independent certification.

The check does not audit the complete historical literature. The closest primary manuscript was inspected for its model, tie lemma, quantitative theorems and limitations; relevant indexed related results were compared by their scientific content. Historical precedence remains subject to independent review.
