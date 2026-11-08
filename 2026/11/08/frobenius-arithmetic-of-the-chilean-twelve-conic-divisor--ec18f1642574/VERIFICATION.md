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

The exact standard-library program `verify.py` independently computes 84 dual Hesse triple determinants in the integer Eisenstein ring and confirms that all their prime-to-three degeneracy factors divide the forbidden Hesse parameter divisors. It enumerates the complete group of 432 affine permutations of the nine-point affine plane, generates the five relevant incidence sets, finds exactly ten cycle signatures, and verifies each asserted ground-field count polynomial. It enumerates \(E_5(\mathbb F_5)\) and \(E_7(\mathbb F_7)\), checks their \(j\)-invariants, and verifies the two extremal Frobenius cycle profiles and all stated extension formulas.

Execution: `python3 verify.py`. The expected final line is `CHILEAN_ARITHMETIC_CERTIFICATE_OK`.

The geometric construction and normalization identities are mathematical arguments documented in `RESULT.md`; the finite computations corroborate rather than replace them. The classification of all 432 affine transformations is exhaustive in its finite domain; the calculation does not claim that all these transformations arise as Frobenius for any given base field. The literal polynomial and finite-field examples are reproducible without external software packages.
