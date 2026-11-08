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

# Reproducibility and verification limits

Use a Python 3 interpreter with only the standard library and execute `python3 verify.py` in the same directory. The checker tests the independently coded original five-variable rules against the shift--involution--difference composition and exhaustively confirms the exact fiber-parity identity for every cyclic input and target on rings through ten sites. It also tests all one- and two-marker words on rings of seven through twelve sites. A successful execution prints `VERIFY_OK checks=15022`.

The mathematical proof of the all-ring theorem depends on the local Boolean factorization, the involutive trigger invariant, and the elementary image/kernel structure of the difference map. Finite tests are not a proof of any unbounded statement. Independent scientific audit, historical-priority determination, and a result about local eventual onto-ness have not been performed.
