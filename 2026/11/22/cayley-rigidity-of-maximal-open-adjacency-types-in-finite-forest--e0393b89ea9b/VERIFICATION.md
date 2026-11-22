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

Run `python3 CHECK.py` using Python 3 and only its standard library.

Checks actually executed:

- Exhaustive labelled-forest and nonempty-marked-set search through six total vertices: 194,363 tests; all satisfied the strengthened upper bound, with 19,112 equality instances satisfying the stated rigidity tests.
- Connected path-based witness constructions for all marked orders from one through seventeen: passed.
- All Prüfer-code labelled spanning trees for marked orders two, three, four and five yielded respectively one, three, sixteen and 125 different maximum-size trace families: passed.

Observed terminal status: `ALL_CHECKS_OK`.

The all-size inequality, equality classification, Cayley count and minimum-host result follow from the written proof. Exhaustive finite checks do not constitute an infinite proof; they may catch small counterexamples or implementation errors. Independent verification has not been performed.
