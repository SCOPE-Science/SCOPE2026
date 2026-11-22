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

# Verification instructions and limits

Run `python3 check.py` under ordinary Python 3. No third-party dependencies or downloads are needed. The program enumerates every perfect matching of \(2n\) ranked endpoints for \(2\le n\le7\), verifies the exact universal-vertex and complete-graph probabilities, checks the equivalence between diameter at most two and universal vertices, and checks the adjacent-dominating-pair implication and a rational-grid version of the deterministic covering lemma. The count of endpoint-pairing order types is 146,598.

These tests verify finite cases and the program's local invariants only; the proof in RESULT.md is necessary for all \(n\) and the asymptotic statement. The exact universal-vertex value is an established published result; the inaccessible 1990 full text remains a historical-priority limitation. Independent audit: not performed.
