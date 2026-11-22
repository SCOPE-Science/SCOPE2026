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

# Verification of finite periodic Fourier interpolation

The mathematical proof is in RESULT.md: a unitary polyphase decomposition followed by exact diagonalization of a symmetric \(3\times3\) Gram matrix, strict eigenvalue ordering, and a Taylor expansion at the three-node collision. The formula is valid for every integer \(m\ge1\) and every real \(0\le\varepsilon<1\); no computational enumeration is used as an infinite proof.

Run `python checker.py` with Python 3 and NumPy. The checker constructs full Fourier matrices for eight sizes and compares the first three spectral power sums against the predicted bands at eleven perturbation values, then tests the quarter-step degeneracy and three near-collision scalings. The recorded run passed 88 full-matrix cases and the additional checks. Numerical floating-point tolerances and finite sample sizes are not certificates for all real parameters.

The analytic collision rate is a limit with an explicit leading coefficient. The result concerns only consecutive integer frequencies, equal sampling weights and the specified three-periodic spatial pattern. Independent validation and historical completeness certification have not been performed.
