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

All inverse-predecessor counts are established analytically by an exact scalar quadratic reduction and an exhaustive monotonicity argument on the two half-lines, including the parameter-threshold and output-boundary equalities. The Jacobian orientations follow from an exact derivative identity. There is no use of finite numerical tests as an infinite-domain proof.

Run `python3 check.py` with the Python 3 standard library to check rational examples by solving the actual branch quadratics and substituting all constructed plane preimages into the original map. The expected output is `FOLD_CREASE_VERIFY_OK`. This does not constitute independent mathematical validation.
