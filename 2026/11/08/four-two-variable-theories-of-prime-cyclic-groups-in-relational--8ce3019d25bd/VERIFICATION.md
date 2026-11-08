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

The proof uses an indefinitely maintainable two-pebble atomic-profile relation for all prime orders at least seven. Explicit two-variable sentences separate orders two, three, and five, and a three-variable recursion expresses any fixed integer multiple in the ternary group relation.

The executable `verify_prime_logic.py` checks 91 pair comparisons among fourteen prime-order structures and 49 evaluations of three-variable prime-torsion sentences for the first seven primes. It builds complete atomic profiles using all 27 triples of terms from the named identity and the two variables, and verifies the one-pebble replacement closure conditions. The expected output is included as `verification_output.txt`.

For reproducibility, run `python3 verify_prime_logic.py` and compare stdout with the recorded output. The finite checks are corroborative and do not establish the infinite family or unlimited logical depth; these follow from the written proof.

Independent mathematical audit: not performed.
