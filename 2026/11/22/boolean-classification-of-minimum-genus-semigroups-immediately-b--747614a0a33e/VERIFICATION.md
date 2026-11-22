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

## Checks and limitations

The proof explicitly establishes the two Kunz-coordinate classifications and verifies all inequalities for arbitrary admissible multiplicities. `verify.py` enumerates every compatible Kunz tuple for the first line from multiplicities 2 through 11 and the second line from multiplicities 3 through 11, selects minimum genus, and compares exact tuples with the theorem. It independently reconstructs the finite semigroups and checks additive closure, genus, multiplicity and Frobenius numbers. Successful execution ends with `TWO_LINE_KUNZ_VERIFY_OK 19`.

The enumeration is bounded and cannot alone certify an infinite claim. No independent mathematical audit has been performed.
