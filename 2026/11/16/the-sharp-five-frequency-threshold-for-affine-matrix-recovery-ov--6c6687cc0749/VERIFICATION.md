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

# Verification and limits

Run `python3 verify_affine13.py` in this folder with Python 3 and no third-party modules. The checker uses integer/finite-field operations for all mathematical assertions, enumerates the entire relevant four-support domain, independently checks the affine classification, and computes the determinant of the exact witness matrix by fraction-free elimination, and independently proves full complex operator span by reducing the cyclotomic orbit-projector matrix modulo \(53\) and checking rank \(144\). It must print `AFFINE13_SPARSE_RECOVERY_PASS` and `AFFINE13_DIRECT_ORBIT_SPAN_PASS` on success. The calculation is finite and exhausts the finite scope claimed; it is not evidence for an all-primes generalization. The dependence on the published 2021 matrix-recovery criterion is explicit in `RESULT.md`. No independent external audit has been performed.
