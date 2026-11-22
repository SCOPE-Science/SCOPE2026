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

Exact field-uniform verification is performed by running `python3 cuboctahedron_barriers_verify.py` with Python 3 standard library only. The two geometric graph constructions agree, all 4096 spin assignments are enumerated without floating-point arithmetic, the exact local stability counts and ground-state lower envelope are checked, and 88 ground-reaching paths are independently constructed under endpoint inequalities. The four affine barrier branches are thereby proved on entire field intervals rather than on test points. The stated output line appears on success.

The verifier proves a finite-graph combinatorial theorem; it does not provide independent scientific audit, a kinetic-time simulation, or historical-priority certification.
