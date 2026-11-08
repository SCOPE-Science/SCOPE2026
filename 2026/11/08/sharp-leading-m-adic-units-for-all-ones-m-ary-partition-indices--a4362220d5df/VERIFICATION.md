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

# Verification of the residue theorem

The attached `verify_partition_units.py` (Python standard library only) was executed to completion; its exact standard output is in `verify_partition_units_output.txt`.

The recurrence checker evaluates the uncolored partition counts with modulus \(m^{R+1}\) for each maximum tested depth \(R\), enough to test all lower depths. It checks all depths from two through nine for \(m=5\), through seven for \(m=7\), through five for \(m=11,13\), through four for \(m=25\), and through three for \(m=35,49\): 29 pairs. Four additional cases use unrelated exact, unrestricted coin-change dynamic programming. A binomial-basis checker confirms 24 integer change-of-basis identities, including the critical two leading coefficients. All tests passed.

The finite tests are not an infinite proof. The infinite argument is the operator identity and induction in `RESULT.md`. The check does not evaluate even bases, multiples of three, or arbitrary indices. No independent audit has been performed.
