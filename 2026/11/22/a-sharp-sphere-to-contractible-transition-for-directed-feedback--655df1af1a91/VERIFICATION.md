---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The corrected one-long-arm simplicial decomposition in `RESULT.md` excludes every two-edge diagonal that is a whole short arm. For example, with two forward arms of lengths 3 and 2, the short diagonal, that diagonal with the long arm's private arc adjoined, and the full long arm are exactly the three excluded faces in the forward degree complex. For one return arc, the count is 33 faces, including the empty face.

The supporting program `verify_mixed_feedback.py` and the recorded `verify_mixed_feedback_output.txt` are unchanged. Using Python 3, `python3 verify_mixed_feedback.py` enumerates arc subsets, checks the degree and cycle conditions against the global gluing model, and computes reduced mod-two Betti numbers for twelve examples. Neither the enumeration nor the homology checks constitute a general homotopy proof. The all-parameter classification uses the simplicial pushout and the two closed stars described in `RESULT.md`.
