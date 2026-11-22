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

# Reproduction

With Python 3, run `python3 verify_one_child.py` from the directory containing this file. The program uses only the standard library. Its final line must read `VERIFY_OK`, and the direct-versus-Apéry crosscheck must read `INDEPENDENT_CHILDREN_OK 1275`.

The script enumerates positive Kunz vectors under the exact genus equation, evaluates all inequalities, and compares primitive-generator counts against direct semigroup-membership/decomposition tests for every accepted vector with multiplicity two through six and eligible genus through sixteen. It also prints finite child-count profiles for multiplicity three through seven at selected genera. The proof of the asymptotic statement is mathematical and independent of these bounded computations.

Limitations: this is a reproducibility check and self-review; it is not independent validation or a machine proof of infinitely many cases.
