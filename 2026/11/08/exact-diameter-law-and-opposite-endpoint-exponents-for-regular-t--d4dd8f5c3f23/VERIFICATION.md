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

The proof derives a pointwise projected-edge identity, exact spherical Jacobian, one-dimensional distribution integral, and separate endpoint asymptotics. Reproducible independent numerical checks are provided in `check.py` (NumPy and SciPy required). The script directly enumerates projected edges and simulates spherical-uniform normals; finite tests corroborate but do not establish the continuum theorem.

Checks performed on the package's actual executable source: `python check.py`; output `TETRAHEDRAL_SHADOW_DIAMETER_OK 900000 90000 3 3`. The original article of Finch and the relevant original preprint of Böröczky–Henk were inspected in the sections listed in `RESULT.md`; the later broad width study was available only at abstract level. Priority and independent mathematical audit remain open.
