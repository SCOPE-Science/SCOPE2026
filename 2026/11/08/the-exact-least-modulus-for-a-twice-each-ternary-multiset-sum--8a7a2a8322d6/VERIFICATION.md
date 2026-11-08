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

# Verification scope

The ternary coin-count lemma is proved by greedy carrying and successive splittings. Substituting the proposed modulus into the difference formula excludes negative and positive candidate collisions. Minimality is established for every smaller modulus through the explicit competing targets, including the odd high-modulus parity case.

The embedded `verify_ternary_twice.py` uses exact Python integers and independently computes difference sets by direct weak-composition enumeration and by a coin-count/dynamic-programming construction. It exhaustively checks all possible moduli through the predicted minimum for each \(n=2,\ldots,8\) and checks elementary parameter inequalities through \(n=1000\). Reproduce using `python3 verify_ternary_twice.py`.

The finite enumerations do not establish the all-\(n\) theorem. No independently performed mathematical audit or historical priority certification is asserted.
