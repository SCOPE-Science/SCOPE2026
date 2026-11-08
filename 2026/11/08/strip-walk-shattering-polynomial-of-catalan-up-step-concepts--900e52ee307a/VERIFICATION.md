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

# Computational verification

Using Python 3 standard library, run `python3 verify_catalan_shattering.py`. The checker independently enumerates all Dyck words of semilength one through seven, tests every possible support and every trace of each support, compares against the strip criterion, then matches counts with the transfer matrix. It additionally checks selected coefficient identities for semilengths eight through twenty-four.

Successful output terminates in `CATALAN_SHATTERING_CORRIDOR_PASS`. The finite test is not a proof for larger semilengths. All-order assertions rely on the exchange, reflection, greedy completion, and transfer arguments in RESULT.md. No independent audit has occurred.
