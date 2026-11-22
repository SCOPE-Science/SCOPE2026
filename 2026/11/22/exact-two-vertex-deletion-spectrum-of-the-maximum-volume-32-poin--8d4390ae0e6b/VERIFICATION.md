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

The exact-coordinate `checker.py` verified the original 60 supporting facets and their volumes. The standalone `deletion_certificate.py` executed successfully, outputting 14 exact determinant and support certificates, 120 full-icosahedral symmetry maps, the exact pair-distance partition, and five loss values over 496 vertex pairs. The included `certificate_output.txt` records the resulting checks.

Dependencies: Python 3, NumPy, SciPy. Floats are used to propose face triangulations, never to certify exact support inequalities or volume comparisons. The checker proves the finite exhaustive claim, not priority or independent audit status.
