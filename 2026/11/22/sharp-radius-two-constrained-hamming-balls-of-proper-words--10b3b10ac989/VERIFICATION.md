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

Running `python verify.py` performs a separately written changed-coordinate enumeration and compares with the displayed local formula. The tested pairs are \((q,n)\) with \(q=3,2\le n\le9\); \(q=4,2\le n\le8\); \(q=5,2\le n\le7\); and \(q=6,2\le n\le6\). All 65,376 tested centers passed, including sharp bound and equality-count checks whenever \(n\ge5\). The computation is finite corroboration, not a proof for arbitrary lengths. The proof in `RESULT.md` uses disjoint classification by changed positions and strict local-comparison inequalities for the arbitrary-length statement. Independent audit has not been performed.
