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

## Reproduction
Run `python3 verify.py` using Python 3 and only its standard library. The checker reconstructs the Gaussian moment polynomial by combinatorial integer expansion, verifies the second-moment orthogonality, differentiates the rational ratio algebraically, checks two exact positive/one-sign-change polynomial transforms for the root-count proof, and uses rational bracketing for the two critical values. Its successful final marker is `ALL_ODD_CUBIC_GAUSSIAN_CHECKS_PASSED`.

## Logical scope
The proof of existence and uniqueness of the real critical points uses Descartes' rule of signs applied to the explicitly provided exact polynomial transforms, rather than treating a numerical root search as exhaustive. Exact root brackets provide reproducible decimals, not proof of uniqueness. All coefficient vectors are addressed because the two Hermite coefficients form a complete real projective line. All results concern real functions and standard Gaussian measure only. A separate independent mathematical audit has not been performed.
