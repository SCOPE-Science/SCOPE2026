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

# Verification

The packaged `check_spacefill_F3.py` requires Python 3 with SymPy and runs solely exact finite-field operations over \(\mathbb F_3\): `python check_spacefill_F3.py`.

It checks the three affine charts covering \(X_0=0\), equality of the four-partial-derivative ideal with a three-element lexicographic Gröbner basis on \(X_0=1\), irreducibility and multiplicity of the two quadratics and the sextic, Hessian rank at each type of geometric point, and nonvanishing of the cubic coefficient along the Hessian null direction. It also checks the linear coordinate transformation between the two nonzero parameters.

A passing run establishes the finite polynomial identities used in RESULT.md. Standard algebraic implications—Euler's identity, the Jacobian criterion, irreducible finite-field orbit degrees, and the intersection of distinct projective surface components—are explained in RESULT.md. The checker does not constitute external or independent certification, and it does not establish analytic classification of the six wild singularities.
