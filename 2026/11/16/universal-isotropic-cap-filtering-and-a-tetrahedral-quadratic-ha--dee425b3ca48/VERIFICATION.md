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

The included `verify_tetra_caps.py` executes with Python, NumPy and SymPy; install those dependencies from `requirements.txt` if missing. All analytical claims are reconstructed in `RESULT.md` and use the normalized entire-sphere Gram, not an unnormalized coordinate measure.

The exact checker symbolically verifies the degree-four Legendre-cap integral, the diagonal and mixed eigenbranches derived from center evaluations, their multiplicity trace identity, their difference factorization, the diagonal branch factor and positive factor, the precise tight radius, and the sharp condition-number limit. It then independently constructs a five-vector real orthonormal degree-two harmonic basis and performs ten-node Gauss–Legendre and 24-node azimuthal integration for all 25 Gram entries at six thresholds; the maximum absolute error was below \(1.3	imes10^{-15}\). It separately tests the universal formula for three distinct second-moment-isotropic center distributions: four tetrahedral centers, the three positive coordinate axes, and six antipodal coordinate axes.

Expected final marker: `ISOTROPIC_CAP_FILTER_PASS exact_symbolic=8 quadrature_radii=6 center_designs=3`.

The tests are not exhaustive over uncountably many center laws or all radii: the harmonic decomposition and exact algebra prove those quantifiers. Independent audit has not been conducted.
