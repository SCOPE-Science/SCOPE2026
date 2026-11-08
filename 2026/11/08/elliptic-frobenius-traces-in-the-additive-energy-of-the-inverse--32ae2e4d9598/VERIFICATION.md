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

# Verification details

The unrestricted argument is the direct algebraic collision classification in `RESULT.md`. Its nonstandard steps are the factorization of the two-value collision equation, explicit exclusion of the fixed/extraneous points, conversion of the off-diagonal count to a quadratic-character sum, and its interpretation as an elliptic trace in characteristic at least five. The proofs for characteristics two and three avoid invalid elliptic smoothness assumptions.

Execute `python3 verify.py` from a directory containing that standalone script. It uses only the standard library and constructs finite fields as polynomial quotients by explicit irreducible polynomials; it verifies that every nonzero field element has its asserted inverse. The program enumerates the two-point sum multiplicities and squares them to compute the actual ordered energy. It compares those counts with the formulas in the result for 23 prime fields and nine proper extension fields, and checks the Frobenius recurrence in two quadratic extensions.

Expected successful output is `VERIFY_OK prime_field_cases=23 extension_cases=9 direct_energies=32 Frobenius_recursions=2 characteristic_branches=2,3,>=5`. This is a finite cross-check of the formulas, not a proof for all finite fields. The elliptic trace recurrence uses the standard Frobenius-eigenvalue theorem for elliptic curves; its proof is not recreated here. Historical uniqueness is not certified, and no independent mathematical audit has been performed.
