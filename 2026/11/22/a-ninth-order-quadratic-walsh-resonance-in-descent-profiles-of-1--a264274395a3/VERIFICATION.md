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

# Exact checks and limits

`checker.py` is executable with the Python 3 standard library. It builds the actual \(132\)-avoider descent-profile histogram by independently iterating all permutations through order nine, checking for the forbidden pattern directly, and applying an integer Walsh–Hadamard transform. Separately, it evaluates every Walsh character via maximum-element Catalan recursion. It asserts equality character by character, the exact weight-two vanishing set and absence of singleton zeros at order nine, absence of weight-two zeros in orders two through eight, and the claimed two-character Catalan formula from orders four to 34. The run completed with `PASS: independent brute, two-coordinate table and infinite-formula finite replay`.

The symbolic derivation in `RESULT.md`, not this finite replay, establishes the formula for arbitrarily large orders. Exhaustion of small orders does not prove the absence of further weight-two zeros at larger orders; no such claim is made. Source priority remains subject to additional historical scholarship.
