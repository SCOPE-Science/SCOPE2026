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

# Reproduction and scope

Run `python3 verify.py` with Python 3.9 or later. It uses only the standard library and deterministically prints `VERIFY_OK 119` if all checks pass.

Checks include exact-fraction inversion of the full graph Laplacian on the mean-zero space, exact comparison against the cycle tensor-product trace, exact resolvent identities, floating evaluation of the trigonometric/coth-type resolvent, and finite-size sign/asymptotic consistency. In particular, at unit conductances the direct index values at cycle sizes \(3,4,5,6\) equal the independently published prism values \(47/5,58/3,655/19,279/5\).

The universal proof does not rely on floating-point calculations. The code does not assert an infinite or exhaustive computational certificate. The mathematical proof is given in RESULT.md. No independent mathematical audit has been performed.
