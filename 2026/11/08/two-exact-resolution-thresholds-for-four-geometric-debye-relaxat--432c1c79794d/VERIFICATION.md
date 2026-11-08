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

# Reproduction checks and scientific limits

The executable `verify.py` is a standalone Python 3 source file requiring `sympy` and `mpmath`. Run `python verify.py` in a directory containing this file. It recomputes the exact derivative numerator from the normalized four-Debye formula, the discriminant identity, the central curvature polynomial, both shifted threshold polynomials, the rational three-root witness, and numerical stationary points directly against the physical dielectric-loss derivative. It also tests the large-separation asymptotic regime. The executed package code returned `VERIFY_OK checks=81`.

The exact all-parameter conclusions follow from the displayed symbolic identities, Descartes' one-positive-root criterion, root-continuation argument and derivative signs in `RESULT.md`. Finite numerical checks are only independent diagnostic evidence; they are not substituted for a universal proof. Four identical linear Debye components and exact geometric spacing are essential. No independent audit has been performed.
