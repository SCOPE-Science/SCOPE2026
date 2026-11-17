---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For arbitrary nonzero real 4×4 A and Haar SO(4), the quaternion S³×S³ double cover yields E F²=S/4 and E F⁴=(5S²−2U)/24+det A. A separately implemented quaternion-bilinear fourth-moment computation confirmed the invariant formula exactly on 20 integer matrices; the package checker compares all monomial coefficients of the 16-variable quartic identity. In oriented signed singular values, the positive three-square lower deficit yields ratio>=2, with equality precisely rank-one or determinant-negative conformal matrices. Cauchy–Schwarz and arithmetic–geometric mean yield upper 4, equality proper conformal matrices. Averaging arbitrary Euclidean norm squared under left/right SO(4) reduces to Frobenius, establishing globally minimal Banach–Mazur distortion 2^(1/4), not merely one chosen Euclidean comparison.

## originality

PASS

Best-of-knowledge original sharp orientation-sensitive real SO4 full matrix-coefficient fourth-moment range, two distinct lower equality geometries, exact three-square deficit and globally optimal Hilbert distortion. Standard quaternion covers and Weingarten integration are explicitly known.

## value

PASS

The full 16-dimensional matrix-coefficient space of classical compact SO(4) is canonical, not an arbitrary spectral slice. Orientation introduces rank-one and improper-conformal minimizers at a shared sharp lower bound, with a distinct proper-conformal upper class; exact positive remainders and optimal Euclidean distortion make this a meaningful complete norm-geometry classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
