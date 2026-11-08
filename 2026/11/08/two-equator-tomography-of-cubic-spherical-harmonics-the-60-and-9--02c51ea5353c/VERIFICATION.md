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

# Verification and scope

Run `python3 verify_two_equators.py` with SymPy available. It checks exact symbolic identities in dimensions 3 through 8 at five angles (orthogonal, the two signed \(60^\circ\) resonances, and two generic rational-cosine cases); the expected output is `TWO_EQUATOR_CUBIC_CHECKS_PASS 291`.

The checker reconstructs Laplacians of the explicit cubic products and the independent coefficient-constraint system for one-equator vanishing. These finite instances are not evidence that every dimension or every angle has been enumerated. The all-dimension, all-angle assertion rests on the polynomial-divisibility argument and exact three-sector diagonalization in RESULT.md. Neither numerical stability constants nor independent mathematical validation are claimed.
