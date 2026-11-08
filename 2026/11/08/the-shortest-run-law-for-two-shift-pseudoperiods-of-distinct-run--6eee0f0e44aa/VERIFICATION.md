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

The complete proof, including the treatment of shortest-run boundaries, the converse for all run lengths and the bijective count of shift pairs, is in `RESULT.md`.

Run `python verify.py` using Python 3 standard library. The script generates all 19,525 profiles with between two and six distinct run symbols and run lengths from one through five; it directly tests the defining pseudoperiod relation at every period position for all shift pairs strictly smaller than the period, and independently generates the predicted pairs. All set comparisons passed. The observed output was:

```
PASS 19525 exhaustive run profiles (q=2..6, lengths=1..5)
```

The executable code and reported finite check do not certify the theorem for arbitrary lengths. The unbounded claim instead follows from the fully quantified proof. The prior-work comparison is best-knowledge and cannot establish absolute priority; independent review remains unperformed.
