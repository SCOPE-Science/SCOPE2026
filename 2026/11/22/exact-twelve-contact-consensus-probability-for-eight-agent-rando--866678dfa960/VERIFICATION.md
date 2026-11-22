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
# Verification of the twelve-contact count

All checks below were executed with Python 3 standard-library exact integers and rationals. Run `python3 verify.py`.

The forward recurrence gives, at depth 12, precisely one terminal state `(255,)*8` and 2,528,870,400 paths. A separately implemented memoized suffix count gives exactly the same integer (267,640 cached states). The reduced probability is `225/20661046784` from 28^12 equally likely sequences. As a cross-check of the mathematical interpretation, exhaustive rational 4×4 matrix products across all 6^4 possible four-contact words reach exact consensus for exactly 24 words, reproducing the published `1/54` probability.

The proof of exhaustive coverage is analytical: at the minimum event count every Jensen–Shannon information gain saturates, implying the precise equal-cardinality/disjoint-support transition rule. The computation verifies the resulting finite recurrence; it does not certify claims at larger network sizes, numerical floating-point equality, or independent mathematical validation. Literature priority beyond inspected material remains uncertain.
