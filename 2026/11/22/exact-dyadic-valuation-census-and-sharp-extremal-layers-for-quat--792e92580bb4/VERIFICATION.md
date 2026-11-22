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

The source checker uses Python 3 standard-library arithmetic. It verifies the six-state carry transition against the digit formula for all indices below \(2^{14}\), checks the exact polynomial recurrence and extreme coefficients at all fourteen tested depths, and independently computes exact Fuss–Catalan binomial values at depths through eight. Executing `python3 checker.py` on the embedded checker yields `CHECK_OK 623 exact assertions levels=0..13`.

The infinite assertions are supported by Legendre's digit-sum formula, the explicitly specified carry automaton, exact rational matrix elimination, and formal coefficient extraction. No computational enumeration is asserted to prove the infinite generality by itself. No independent audit has been performed.
