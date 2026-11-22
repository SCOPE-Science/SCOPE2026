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

# Reproducible checks and logical limits

The companion `verify.py` runs with Python's standard library and was executed with `python verify.py`. It produced:

`VERIFY_OK 1481 exact-rational assertions; exact iid growth and stable alternating witness`

The code independently evaluates the proximal and dual updates in Cartesian coordinates, verifies that the reduced two-component matrix matches these updates for several distinct rational line geometries, checks that the primal and dual iterates remain on their respective subspaces, and verifies the exact conditional squared-norm identity for reciprocal two-point laws. It also enumerates binary switching words through length five as a finite diagnostic; no general claim rests on this enumeration. It checks the exact Schur trace, determinant, endpoint identities and the rational witness with iid growth factor \(801/800\) and alternating conjugate eigenvalue modulus \(9/10\).

The full universal claim instead follows analytically from \(\mathbb E[T(m)^\top T(m)]=\lambda I\), independent fresh draws, the scalar factorization \(\lambda-1=-(1-p)(1-(v-1)p)\), and the degree-two Schur criterion. Inaccessible related literature and possible equivalent older formulations remain originality limitations. Independent audit and external validation have not been performed.
