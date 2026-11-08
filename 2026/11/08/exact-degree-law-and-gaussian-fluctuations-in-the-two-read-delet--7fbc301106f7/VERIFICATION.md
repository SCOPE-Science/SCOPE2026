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

# Verification instructions

Extract `checker.py` alongside these documents and run `python3 checker.py` with the Python 3 standard library. The script constructs raw one-deletion balls, checks the size-two common-output adjacency independently of the alternating-word formula, compares complete degree histograms to the recurrence, then verifies exact rational mean and variance formulas. The actual execution returned the two PASS lines printed by the script. Exact graph cases cover \(q=2\) through length nine, \(q=3\) through length six, and \(q=4\) through length five (\(3478\) tested vertex instances). The recurrence-to-moment comparisons cover \(2\le q\le7\), \(1\le n\le23\).

All-length correctness is supplied by the written counting proof and the martingale central-limit argument; finite enumerations do not certify infinitely many cases. The source characterization of pairs with two common deletion descendants is cited in the scientific proof and was inspected as published text. Historical priority and independent validation remain unresolved.
