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

# Verification record

The companion `verify_census12.py` was executed against the attached `census12.json` with ordinary Python 3. Its exact cyclotomic calculation enumerated 66 translated five-set classes and all 4,356 class pairs, giving rank counts 27/757/3,572; the corresponding 627,264 raw pairs have ranks 3/4/5 with counts 3,888/109,008/514,368. A second finite-field rank calculation at a primitive twelfth root modulo 1,009 found zero discrepancies. Two row-translation classes yield fully invertible five-column sampling.

The exact cyclotomic computation, together with the determinant/minor and orbit-reduction proofs, establishes this **finite** theorem. Finite-field agreement alone cannot establish characteristic-zero rank, and no all-order extension or infinite claim is made. External independent audit has not been performed.
