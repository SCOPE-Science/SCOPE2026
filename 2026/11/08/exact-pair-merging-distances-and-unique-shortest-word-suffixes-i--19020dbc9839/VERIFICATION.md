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

Run `python3 verify.py` from the directory containing the attached standalone verifier. The script reconstructs reverse BFS distances without using the claimed formula as the BFS oracle for \(2\le n\le80\), and independently checks the potential-step inequalities, all rank multiplicities, unique decreasing transitions, and the explicit longest-word spelling for \(2\le n\le400\). An execution returned `PASS` and counted 10,666,600 pair instances. No exhaustive computation over all positive \(n\) is asserted; the mathematical proof supplies that universal quantifier. The literature comparisons identify an earlier odd-state pair transition graph, so novelty requires cautious interpretation. Independent audit: not performed.
