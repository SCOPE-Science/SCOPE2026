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

The standalone `verify_wheel.py` exhausts all \(2^{n+1}\) labeled action profiles for each \(3\le n\le15\) in each of four hub/rim type families. Each profile is directly tested against the payoff best-response definition, and equilibrium strictness is checked separately. It also evaluates an exact-rational expression for the number of maximal independent sets of each cycle and compares it against the Perrin recurrence.

Command: `python3 verify_wheel.py`

Observed output:
```
CHECK_OK: 52 exact wheel/type cases; 524224 complete action profiles;
Perrin MIS identity checked for n=3..15; both total and strict equilibrium counts confirmed.
```

The proof covers every integer \(n\ge3\). Finite enumeration is only a cross-check, and the implementation makes no claim to certify all infinitely many cases. No independent scientific audit is represented by this record.
