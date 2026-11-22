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

The attached `verify_0011.py` independently reconstructs the underlying pattern-avoidance suffix automaton and all reachable subset families. It checks the quotient partition, rational identities, max-plus identity, and independent exhaustive support decisions at lengths zero through twelve. The exact mathematical certificate is `state_certificate.txt`. All computations are integer-exact and require only standard Python.

The exhaustive tests do not claim to prove infinitely many cases. The all-length claims follow from the two deterministic automata, their finite transition certificates and the algebraic matrix identities in `RESULT.md`. No independent external audit or formal machine-proof process has been performed.
