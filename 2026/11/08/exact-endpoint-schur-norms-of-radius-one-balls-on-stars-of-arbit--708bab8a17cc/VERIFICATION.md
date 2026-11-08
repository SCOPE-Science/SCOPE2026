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

# Reproduction and proof limits

Run `python3 checks/star_ball_checker.py` using the Python standard library. The checker verifies 15 exact rational assertions in each of 1024 finite degrees and prints `STAR_BALL_EXACT_CERTIFICATES_OK 15360`. The rank-two trace eigenvalue identities and two positive-semidefinite block determinants are also calculated symbolically in the written proof. The countably infinite case follows from an explicit completely positive kernel decomposition plus the supremum of finite corner norms, not from numerical extrapolation. The equality of ordinary and completely bounded norms follows from a matching ordinary lower witness and completely bounded upper decomposition. Source priority is not independently certified; the previously known three-vertex value is credited.
