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

# Mathematical verification

The central proof is an exact CRT counting argument. Independently reproduce the accompanying finite consistency checks with `python3 verify.py` (Python 3 standard library only). It prints six exact witness cardinalities and checks 600 deterministically generated configurations against the derived bound. These tests are finite samples and are not an exhaustive search over all possible residue selections or a substitute for the symbolic proof. The proof itself has no numerical assumptions beyond distinct odd primes.

The construction is fixed by the seven coordinate constraints specified in `RESULT.md`. Sample values include \(u(105)=35\) and \(u(385)=219\), in agreement with the published finite examples. No separate independent mathematical audit has been performed.
