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

# Reproduction and boundaries

Execute `python3 verify.py` with Python 3 in the same folder as this document. The program directly constructs periodic words, examines each possible start phase, tests equality of all \(q\) constituent Parikh vectors, and compares both phase counts and distinct-factor counts against the displayed formulas.

Observed output:

```
PASS cases=24464; phase-start comparisons=404329; exhaustive a,b=1..12, q=3..8, k=1..2(a+b); randomized=2000
```

The exhaustive range is finite, while the theorem quantifies over arbitrary positive \(a,b,k\) and \(q\ge3\). The proof in `RESULT.md` supplies the infinite argument. No independent scientific audit has been performed.
