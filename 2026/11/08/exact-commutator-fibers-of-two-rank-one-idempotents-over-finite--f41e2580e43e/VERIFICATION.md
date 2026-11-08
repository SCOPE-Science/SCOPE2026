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

The package includes `scripts/check_commutator.py`, which implements finite-field arithmetic, exhaustive rank-one idempotent construction, literal matrix multiplication and commutator evaluation, then verifies every prescribed target over fields of orders \(2,3,4,5,7,8,9,11\). For the three extension fields, the arithmetic is implemented using irreducible defining polynomials rather than assuming prime-field arithmetic. Actual standard output is saved in `checks/checker_output.txt`.

Run `python scripts/check_commutator.py` at the package root. The recorded final marker is `ALL_PROJECTION_COMMUTATOR_CHECKS_PASS`. The case-by-case paper proof covers every finite field and is not inferred from finite enumeration.

The independent mathematical audit and historical-priority certification have not been performed. The 2002 original characterization article could not be read in full; accessible descriptions and newer primary texts were compared without asserting that inaccessible content is absent.
